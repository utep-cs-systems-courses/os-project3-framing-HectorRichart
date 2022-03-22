#! /usr/bin/env python3

# Echo client program
import socket, sys, re, time
sys.path.append("../lib")       # for params
import params
from Archive import *

switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--delay'), 'delay', "0"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)

delay = float(paramMap['delay']) # delay before reading (default = 0s)
if delay != 0:
    print(f"sleeping for {delay}s")
    time.sleep(int(delay))
    print("done sleeping")

#clients receives and figures out file size, extension and where they end and start, output file will contain
#all the files restored correclty
while 1:
    data = s.recv(1024).decode()
    print("Received '%s'" % data)
    if len(data) == 0:
        break
print("Zero length read.  Closing")
s.close()

# import socket

# #Gets a socket object
# ClientSocket = socket.socket()
# #create address parameters
# host = '127.0.0.1'
# port = 1233

# #It tries to connect to the server
# print('Waiting for connection')
# try:
#     ClientSocket.connect((host, port))
# except socket.error as e:
#     print(str(e))

# #Opens the file a and receives a 1024 bytes from the server MAX
# Response = ClientSocket.recv(1024)
# #Create the file
# clientid = str(ClientSocket.getsockname()[1])
# text_file = open("received_file_[" + clientid +"].txt","a")
# #Write the file as long as you are receiving it from server
# while len(Response) > 0:
#     Response = ClientSocket.recv(1024)
#     text_file.write(Response.decode())
#     print(Response.decode('utf-8'))
    
# #Close
# ClientSocket.close()