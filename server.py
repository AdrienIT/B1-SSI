import socket
import os
import shutil

def download():
    conn.send(command.encode())
    filePath = input(str("Chemin vers le fichier + le nom du fichier : "))
    conn.send(filePath.encode())
    file = conn.recv(500000)
    fileName = input(str("Nom du fichier a ecrire : "))
    newFile = open(fileName, "wb")
    newFile.write(file)
    newFile.close()
    print("\nDone !")


s = socket.socket()
host = socket.gethostname()
port = 3000
s.bind((host, port))
print("")
print("Le server tourne sur @",host)
print("En attente de connections")
s.listen(1)

conn, addr = s.accept()
print(addr, " s'est connecté")
print("")

while 1:

    print("1: Download File")
    print("")
    command = input(str("commande >> "))
    if command == "1":
        path=input("dir to download (pliz use pwd) : ")
        if not os.path.exists(path):
            os.mkdir(path)
            print("Directory " , path ,  " Created ")
            download()
            shutil.move("/home/adrien/Bureau/ssi/masterized/logs.txt", path)
        else:    
            print("Directory " , path ,  " already exists")
    else:
        print("Invalid Command")
    print("")
