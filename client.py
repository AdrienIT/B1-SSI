import os
import shutil
import socket

s = socket.socket()
port = 3000
host ="IP SERVER"
s.connect((host, port))

print("Connected")

while 1:
    command = s.recv(1040)
    command = command.decode()
    print("commande recu")
    if command == "1":
        filePath = s.recv(50000)
        filePath.decode()
        file = open(filePath, "rb")
        data = file.read()
        s.send(data)
        print("Fichier envoye ")
    else:
        print("Commande inconnu")

    print("")