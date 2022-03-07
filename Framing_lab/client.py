
import socket
from urllib import response

#Creates sockec object
ClientSocket = socket.socket()
#addresses for client
host = '127.0.0.1'
port = 1233

#Connecting to the server with same host and port
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

#Opens the file a and receives a 1024 bytes from the server MAX
Response = ClientSocket.recv(1024)
#Create the file
clientid = str(ClientSocket.getsockname()[1])
text_file = open("received_file_[" + clientid +"].txt","a")
#Write the file as long as you are receiving it from server
while len(Response) > 0:
    Response = ClientSocket.recv(1024)
    text_file.write(Response.decode()) #decoding the file since its sent as bytes
    print(Response.decode('utf-8'))
    
#Close connection
ClientSocket.close()