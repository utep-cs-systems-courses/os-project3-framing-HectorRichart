#! /usr/bin/env python3

import socket

#Gets a socket object
ClientSocket = socket.socket()
#create address parameters
host = '127.0.0.1'
port = 50001

#It tries to connect to the server
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Opens the file a and receives a 1024 bytes from the server MAX
Response = ClientSocket.recv(1024)
#Create the file
clientid = str(ClientSocket.getsockname()[1])
text_file = open("received file by server[" + clientid +"].txt","a")
#Write the file as long as you are receiving it from server
while len(Response) > 0:
    Response = ClientSocket.recv(1024)
    text_file.write(Response.decode())
    print(Response.decode('utf-8'))
    
#Close
ClientSocket.close()