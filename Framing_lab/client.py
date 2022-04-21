#! /usr/bin/env python3

import socket
from Archive import*
import os

#Gets a socket object
ClientSocket = socket.socket()
#create address parameters
host = '127.0.0.1'
port = 50001

#It tries to connect to the server
print('Waiting for connection (Client side)...')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Opens the file a and receives a 1024 bytes from the server MAX
Response = ClientSocket.recv(1024)
#Create the file
clientid = str(ClientSocket.getsockname()[1])
count = 1
old_name = "Received file[" + clientid +"]" + "-" + str(count) + ".txt"
new_name = "Received file[" + clientid +"]" + "-" + str(count) + ".txt"
if os.path.isfile(old_name):
    print("This file already exists by another client, renaming file")
    text_file = open(new_name,"a")
else:
    text_file = open(old_name,"a")
count +=1
#Write the file as long as you are receiving it from server
while len(Response) > 0:
    Response = ClientSocket.recv(1024)
    text_file.write(Response.decode())

    print(Response.decode('utf-8'))
    
#Close
ClientSocket.close()