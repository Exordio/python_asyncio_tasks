# -*- coding: utf-8 -*-

import socket

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        client(client_socket)
        
def client(client_socket):
    while True: 
        print('Before .recv()')
        request = client_socket.recv(4096)
        
        if not request:    
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    client_socket.close()

server()
