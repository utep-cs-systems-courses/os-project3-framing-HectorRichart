#! /usr/bin/env python3
from http import client
import socket, sys, re, os, time
sys.path.append("../lib")       # for params
import params
from Archive import *

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets
#Fork on every call to get a child that 
while True:
    conn, addr = s.accept() # wait until incoming connection request (and accept it)
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        path = "sockets.txt"
        if os.path.exists(path):
            encoded_file = archive(path)
            size = len(encoded_file)
            totalsent = 0
            while totalsent < size:
                sent = conn.send(encoded_file[totalsent:])
                if sent == 0:
                    raise RuntimeError("Socket connection broken.")
                totalsent += sent
                unarchive("received file from client" + str(addr[1]) + ".txt", encoded_file)
            time.sleep(0.25);       # delay 1/4s
            conn.shutdown(socket.SHUT_WR)
            sys.exit(0)


# import socket
# from _thread import *

# #Creates the socket
# ServerSocket = socket.socket()
# #Create the addresses
# host = '127.0.0.1'
# port = 1233
# #set to listen from income connections
# ThreadCount = 0
# try:
#     ServerSocket.bind((host, port))
# except socket.error as e:
#     print(str(e))

# print('Waiting for a Connection..')
# ServerSocket.listen(5)

# #Function to send the info to the client
# def threaded_client(connection):
#     #open the file
#     bio_text = open("sockets.txt")
#     connection.send(str.encode('Welcome to the Server'))
#     #read the file
#     buffer = bio_text.read()
#     #Sends 1024 bytes at the time to the client 
#     while len(buffer) > 0:
#         connection.send(buffer[:1024].encode())
#         buffer = buffer[1024:]
#     #close the conncetion
#     connection.close()

# #Creates new threads for every connection
# while True:
#     Client, address = ServerSocket.accept()
#     print('Connected to: ' + address[0] + ':' + str(address[1]))
#     start_new_thread(threaded_client, (Client, ))
#     ThreadCount += 1
#     print('Thread Number: ' + str(ThreadCount))
# ServerSocket.close()