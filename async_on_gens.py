# -*- coding: utf-8 -*-
# Основано на докладе Dabid Beazley
# 2015 pycon
# Конкурентность питона с 0 в живую
import socket

tasks = []


to_read = {}
to_write = {}


def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    
    while True:
        
        yield ('read' ,server_socket)
        client_socket, addr = server_socket.accept() # read
        
        print('Connection from', addr)
        client(client_socket)
        
def client():
    while True: 
        yield ('read', client_socket)
        
        request = client_socket.recv(4096) #read
        
        if not request:    
            break
        else:
            response = 'Hello world\n'.encode()
            
            yield ('write', client_socket)
            client_socket.send(response) #write

    client_socket.close()

def event_loop():
    
    while any([tasks, to_read, to_write]):
        
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

tasks.append(server())
