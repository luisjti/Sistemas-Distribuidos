import socket
import random
import time

host = 'localhost'
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

while True:
    aux = input('Digite 1 se deseja consumir: ')
    s_client.send(aux.encode())
    consumed = s_client.recv(1024).decode()
    if consumed == 'Buffer vazio':
        print('Buffer vazio, aguarde')
    else:
        print('Consumido {}'.format(consumed))
    time.sleep(1)

s_client.close()
