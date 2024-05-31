import socket
import threading

host = '127.0.0.1'
port = 9999

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
                if "Servidor cerrandose" in message:
                    print("Desconectado del servidor. Cerrando aplicacion...")
                    client_socket.close()
                    break
        except:
            print("Ha ocurrido un error!")
            client_socket.close()
            break

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(nombre.encode())

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        if message:
            try:
                client_socket.send(message.encode())
            except:
                break
