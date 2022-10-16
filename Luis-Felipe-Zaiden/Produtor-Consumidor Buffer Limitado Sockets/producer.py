import socket
import time

host = 'localhost'
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

while True:
    dado = input('Digite o valor a ser produzido: ')
    dado = str(dado)
    s_client.send(dado.encode())
    time.sleep(1)

s_client.close()
