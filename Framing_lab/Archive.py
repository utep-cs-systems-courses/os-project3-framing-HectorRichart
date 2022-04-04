
#Encodes the information in the given file
def archive(file_name):
    with open(file_name, "rb") as file: #rb = readBytes mode
        byteArray = bytearray()
        byteArray += file.read()  #appending the file to the byte array and method returns that
        return byteArray

#restores the encoded file (byte array file)
def unarchive(file_name, encoded_data):
        with open(file_name, "wb") as file: #opening in read bytes mode, automatically decodes data
            file.write(encoded_data) #putting encoded data in the output file

#Testing
encoded = archive("sockets.txt")
print(encoded)



#TODO: