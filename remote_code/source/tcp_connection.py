import json
import socket

file = open("./settings/communication.json", "r")
settings = json.load(file)

# define the server"s address and port
server_address = settings["tcp ip"]
server_port = settings["tcp port"]

class tcp_client:
    client_socket = None  

    def __init__(self):
        # create a socket object
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to the server
        self.client_socket.connect((server_address, server_port))

    def forward_message(self, modbus_frame):
        # send data to the server
        self.client_socket.sendall(bytes(modbus_frame))

    def receive_response(self):
        # receive reponse from drive
        return self.client_socket.recv(1024)

    def close_connection(self):
        # close the socket
        self.client_socket.close()
  
