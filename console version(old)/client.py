import socket                   # Import socket module
import os

s = socket.socket()             # Create a socket object
host = input("host ip:")  #Ip address that the TCPServer  is there
port = 25575                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
welcomemsg="Hello server!"
s.send(bytearray(welcomemsg,"utf-8"))

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(16384)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully got the file')
s.close()
print('connection closed')
filename=input("name of received file:")
ext=input("extension of file received(.txt,.docx,etc):")
os.rename("received_file",filename+ext)