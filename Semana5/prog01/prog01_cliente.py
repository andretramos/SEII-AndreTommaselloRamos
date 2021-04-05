import sys
import socket

porta = "80"
ip = "127.0.0.1"
nomearq = "teste2.txt"


porta = int(porta)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), porta))
msg = s.recv(2048)
print(msg)
out = msg.decode("utf-8")
file = open(nomearq,'w')
file.write(out)
file.close()