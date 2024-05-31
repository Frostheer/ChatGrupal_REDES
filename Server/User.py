import uuid
from utils.ColorEnum import Color

class User:
    def __init__(self, address, nombre):
        self.user_id = uuid.uuid4()  # Genera un UUID único para cada usuario
        self.address = address
        self.nombre = nombre
        self.admin = False
        self.superAdmin = False
        self.comandos = []  # comandos por el usuario
        self.messages = []  # mensajes enviados por el usuario, es un array de tuplas (grupo, mensaje)
        self.grupo = None  # grupo actual del usuario
        self.messageColor = Color.DEFAULT

    def adminOn(self):
        self.admin = True
        
    def superAdminOn(self):
        self.superAdmin = True
    
    def añadirRegistroComando(self, comando):
        self.comandos.append(comando)
    
    def añadirRegistroMensaje(self, mensaje):
        self.messages.append((self.grupo, mensaje))
    
    def cambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def ingresarGrupo(self, grupo):
        self.grupo = grupo
    
    def enviarMensajeGrupo(self, grupo, mensaje):
        if self.grupo == grupo:
            return f"\n{self.messageColor.value}{self.nombre} en {grupo}: {mensaje}{Color.DEFAULT.value}"
        return None
