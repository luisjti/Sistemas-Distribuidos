import socket

host = 'localhost'
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

valor = input(" Digite o valor da carta: ")
naipe = input(" Digite o naipe da carta: ")

valor = valor + ' '
s_client.send(valor.encode())
s_client.send(naipe.encode())
mensagem = s_client.recv(1024).decode()

print(mensagem)

s_client.close()
