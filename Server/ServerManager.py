import socket
import threading
import uuid
from User import User
from utils.ColorEnum import Color
from utils.HelpMessages import HelpMessages  # Importar el enum

class ServerManager:
    
    # Contraseña para Admin
    contraseñaAdmin = "password1234"
    
    # Contraseña para super Admin
    contraseñaSuperAdmin = "contraseñaSuperAdmin1234"

    def __init__(self, host='127.0.0.1', port=9999):
        self.clients = []  # Guarda pares (User, socket)
        self.grupos = ["General", "Privado"]
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.bind((host, port))
        self.server.listen()
        self.running = True  # Bandera para controlar el estado del servidor

    def broadcast(self, message, grupo, sender_socket):
        for user, client_socket in self.clients:
            if user.grupo == grupo and client_socket != sender_socket:
                try:
                    client_socket.send((message).encode())
                except:
                    self.clients.remove((user, client_socket))

    def handle_client(self, client_socket, user):
        welcome_message = (
            "\nBienvenido al chat! Para ver la lista de comandos disponibles, escribe /help\n"
        )
        client_socket.send(welcome_message.encode())
        
        while self.running:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break

                if message.startswith("/"):
                    self.handle_command(message, user, client_socket)
                else:
                    user.añadirRegistroMensaje(message)
                    formated_message = user.enviarMensajeGrupo(user.grupo, message)
                    if formated_message:
                        self.broadcast(formated_message, user.grupo, client_socket)
            except:
                self.clients.remove((user, client_socket))
                client_socket.close()
                break

    def handle_command(self, message, user, client_socket):
        # Añadir el comando al historial del usuario
        user.añadirRegistroComando(message)

        if message.startswith("/nombre"):
            nuevo_nombre = message.split(" ", 1)[1]
            user.cambiarNombre(nuevo_nombre)
            client_socket.send(f"Nombre cambiado a {nuevo_nombre}\n".encode())

        elif message.startswith("/ingresar"):
            grupo = message.split(" ", 1)[1]
            if grupo in self.grupos:
                user.ingresarGrupo(grupo)
                client_socket.send(f"Ingresado al grupo {grupo}\n".encode())
            else:
                client_socket.send(f"Grupo {grupo} no existe\n".encode())

        elif message.startswith("/ver_mensajes "):
            args = message.split(" ", 1)[1]
            target_user = self.find_user(args)
            if target_user:
                for grupo, msg in target_user.messages:
                    client_socket.send((f"Grupo {grupo}: {msg}\n").encode())
            else:
                client_socket.send(f"Usuario {args} no encontrado\n".encode())
                
        elif message.startswith("/ver_comandos "):
            args = message.split(" ", 1)[1]
            target_user = self.find_user(args)
            if target_user:
                for comando in target_user.comandos:
                    client_socket.send((comando + "\n").encode())
            else:
                client_socket.send(f"Usuario {args} no encontrado\n".encode())
        
        elif message.startswith("/color "):
            color_name = message.split(" ", 1)[1].upper()
            if color_name in Color.__members__:
                user.messageColor = Color[color_name]
                client_socket.send(f"Color de mensaje cambiado a {color_name}\n".encode())
            else:
                client_socket.send("Color no valido. Colores disponibles: DEFAULT, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE\n".encode())
                
        elif message.startswith("/admin "):
            password = message.split(" ", 1)[1]
            if password == self.contraseñaAdmin:
                user.adminOn()
                client_socket.send("Ahora eres administrador.\n".encode())
            elif password == self.contraseñaSuperAdmin:
                user.superAdminOn()
                user.adminOn()
                client_socket.send("Ahora eres super administrador.\n".encode())
            else:
                client_socket.send("Contraseña incorrecta.\n".encode())  

        elif message.startswith("/crear_grupo ") and user.admin:
            nuevo_grupo = message.split(" ", 1)[1]
            if nuevo_grupo not in self.grupos:
                self.grupos.append(nuevo_grupo)
                client_socket.send(f"Grupo '{nuevo_grupo}' creado exitosamente.\n".encode())
            else:
                client_socket.send(f"El grupo '{nuevo_grupo}' ya existe.\n".encode())
                
        elif message.startswith("/grupos"):
            grupos_disponibles = ", ".join(self.grupos)
            client_socket.send(f"Grupos disponibles: {grupos_disponibles}\n".encode())        

        elif message.startswith("/shutdown") and user.superAdmin:
            for user, client_socket in self.clients:
                client_socket.send("Servidor cerrandose...\n".encode())
            self.shutdown()
        
        elif message.startswith("/help"):
            if user.superAdmin:
                client_socket.send(HelpMessages.SUPER_ADMIN_HELP.value.encode())
            elif user.admin:
                client_socket.send(HelpMessages.ADMIN_HELP.value.encode())
            else:
                client_socket.send(HelpMessages.USER_HELP.value.encode())

    def find_user(self, identifier):
        # Verificar si el identificador es un UUID
        try:
            uuid_obj = uuid.UUID(identifier)
            return next((u for u, s in self.clients if u.user_id == uuid_obj), None)
        except ValueError:
            # No es un UUID, buscar por nombre de usuario
            return next((u for u, s in self.clients if u.nombre == identifier), None)

    def shutdown(self):
        self.running = False
        self.server.close()
        for user, client_socket in self.clients:
            client_socket.close()
        print("Servidor cerrado.")

    def startServer(self):
        print("Servidor Iniciado")
        while self.running:
            try:
                client_socket, client_address = self.server.accept()
                nombre = client_socket.recv(1024).decode()
                user = User(address=client_address, nombre=nombre)

                # Todos los usuarios ingresan al grupo general por defecto
                user.ingresarGrupo("General")
                print(f"New connection: {user.nombre} from {client_address}, ID: {user.user_id}")
                self.clients.append((user, client_socket))
                threading.Thread(target=self.handle_client, args=(client_socket, user)).start()
            except Exception as e:
                print(f"Error al aceptar conexiones: {e}")
                break

if __name__ == "__main__":
    server = ServerManager()
    server.startServer()
