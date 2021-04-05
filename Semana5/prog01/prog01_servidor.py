import sys
import socket

porta = "80"
nomearq = "teste.txt"

print(porta)
door = int(porta)

with open(nomearq,'r') as file:
    data = file.read()
print(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), door))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    print(f"Conexão de {address} realizada.")
    clientsocket.send(bytes(data,"utf-8"))
    clientsocket.close()