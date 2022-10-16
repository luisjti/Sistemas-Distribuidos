import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

nome = input(" Digite o nome: ")
sexo = input(" Digite o sexo: ")
idade = input(" Digite a idade: ")

nome = (nome + ' ')
sexo = (sexo + ' ')

s_client.send(nome.encode())
s_client.send(sexo.encode())
s_client.send(idade.encode())

mensagem = s_client.recv(1024).decode()
if mensagem == "1":
    print('A pessoa ja atingiu a maioridade')
else:
    print('A pessoa ainda nao atingiu a maioridade')

s_client.close()

