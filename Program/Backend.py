import os
import socket
import time
import port_forward_3
#import py7zr
from AdvancedOptions import Ui_Form
from PyQt5 import QtWidgets

def receiveFile(bufferStr,host,filename,ext,isEncrypted,passwd):
        
    startRecv=time.perf_counter()
    if bufferStr=="":
        buffer=32000
    else:
        buffer=int(bufferStr)
    s = socket.socket()             # Create a socket object
    port = 25575                     # Reserve a port for your service every new transfer wants a new port or you must wait.

    s.connect((host, port))
    welcomemsg="Hello server!"
    s.send(bytearray(welcomemsg,"utf-8"))

    with open('received_file', 'wb') as f:
        print('file opened')
        #self.textEdit.append('receiving data...')
        while True:
                
            data = s.recv(buffer)
            #print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    endRecv=time.perf_counter()
    finalTimeRecv=endRecv-startRecv
    s.close()
    print('connection closed')
    if isEncrypted==True:
        os.rename("received_file","received_file.7z")
        with py7zr.SevenZipFile("received_file.7z", mode='r', password=passwd) as z:
            z.extractall()      
        os.remove("received_file.7z")  
    else:
      os.rename("received_file",filename+ext)
    return finalTimeRecv


    
def sendFile(localHost,filepath,bufferStr,isEncrypted,passwd):
   #isEncrypted,passwd=initOptions().ui.isEncrypted()
    #passwd=initOptions().passwd
    if "file:///" in filepath:
        filepath=filepath.replace("file:///","")
    if localHost==False:
        openPort = port_forward_3.EnablePort(25575)
        if isEncrypted==True:
            with py7zr.SevenZipFile(os.path.basename(filepath+"_compressed.7z"), 'w', password=passwd) as archive:
                archive.writeall(filepath, os.path.basename(filepath))
            filepath=os.path.basename(filepath+"_compressed.7z")
    else:
        print("xd")

    if bufferStr=="":
        buffer=32000
    else:
        buffer=int(bufferStr)

    port = 25575                    # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()             # Create a socket object
    host = ""   # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.settimeout(float(20))
    s.listen(5)                     # Now wait for client connection.
       

    i=0
        

    while i==0:
        conn, addr = s.accept()     # Establish connection with client.
        startSend=time.perf_counter()

        data = conn.recv(buffer)
        #self.textEdit.setText('Server received' + str(repr(data)))
        

        filename=filepath #In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename,'rb')
        l = f.read(buffer)
        #self.textEdit.append('Sending file ')
        while (l):
            conn.send(l)
                
            l = f.read(buffer)
        f.close()
        endSend=time.perf_counter()

        finalTimeSend=endSend-startSend

           
        conn.close()
        if localHost==False:
            closePort=port_forward_3.DisablePort(25575)
        else:
            xd=1
        i=1
    if isEncrypted==True:
        os.remove(filepath)   
    return addr,finalTimeSend
