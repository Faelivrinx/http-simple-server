import socket

HEADER_LENGTH=10
IP='127.0.0.1'
PORT=8080

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)

server_socket.bind((IP, PORT))
server_socket.listen()

print('socket is listening on port', PORT)

socket_list = [server_socket]

clients = {}



