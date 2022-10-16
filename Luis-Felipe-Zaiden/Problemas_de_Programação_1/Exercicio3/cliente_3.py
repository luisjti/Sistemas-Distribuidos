import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

n1 = input(" Digite a N1: ")
n2 = input(" Digite a N2: ")
n3 = input(" Digite a N3: ")

n1 = (n1 + ' ')
n2 = (n2 + ' ')

s_client.send(n1.encode())
s_client.send(n2.encode())
s_client.send(n3.encode())

mensagem = s_client.recv(1024).decode()

if mensagem == "1":
    print('O aluno foi aprovado')
else:
    print('O aluno nao foi aprovado')

s_client.close()

