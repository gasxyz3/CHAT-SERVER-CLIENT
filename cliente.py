import socket
import threading
import os

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            break

host = "127.0.0.1"
port = 8888

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

username = input("Ingresa tu nombre de usuario: ")
client.send(username.encode("utf-8"))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

os.system("clear")
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
                                            
Chat hecho por Gasxyz
""")

while True:
    message = input()

    # Dar color al nombre de usuario en tus mensajes
    colored_message = f"\033[94m{username}\033[0m: {message}"
    client.send(colored_message.encode("utf-8"))
