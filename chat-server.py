import socket
import threading
import os

os.system("clear")

# Códigos de escape ANSI para los colores
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

print("""
                    @@@@@@@@@@@                   
               @@@@@@@@@@@@@@@@@@@@@              
           ,@@@@@@@@@         @@@@@@@@@           
         @@@@@@@@@               @@@@@@@@&        
        @@@@@@@@@                 @@@@@@@@@       
       @@@@@@@@@@                 @@@@@@@@@@      
      @@@@@@@@@@@@               @@@@@@@@@@@@     
      @@@@@@@@@@@@@@           @@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@        .@@@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@     
       @@@@@@@@@@@@@@         @@@@@@@@@@@@@@      
        @@@@@@@@@@@@           @@@@@@@@@@@@       
         @@@@@@@@@@@           @@@@@@@@@@@        
           @@@@@@@@            @@@@@@@@@          
              @@@@@@@@@@@@@@@@@@@@@@@             
                  %@@@@@@@@@@@@@#                 
                                            
Hecho por Gasxyz
""")

clients = []
lock = threading.Lock()  # Agregamos un bloqueo para evitar problemas de concurrencia

def handle_client(client_socket, username):
    print(f"{COLOR_GREEN}{username}{COLOR_RESET} se ha unido al chat.")

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"{message}")  # No imprimimos el nombre de usuario en el servidor
            # Enviar mensaje a todos los otros clientes conectados
            with lock:
                for client in clients:
                    if client != client_socket:
                        client.send(message.encode("utf-8"))
        except:
            break

    print(f"{COLOR_GREEN}{username}{COLOR_RESET} se ha desconectado.")
    with lock:
        clients.remove(client_socket)
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen(5)

print("Esperando conexiones en el puerto 8888...")

while True:
    client_socket, _ = server.accept()
    username = client_socket.recv(1024).decode("utf-8")
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()

