import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

idade = input(" Digite a idade: ")
tempo = input(" Digite o tempo de servico: ")


idade = (idade + ' ')

s_client.send(idade.encode())
s_client.send(tempo.encode())

mensagem = s_client.recv(1024).decode()

if mensagem == "1":
    print("O funcionario pode se aposentar")
else:
    print("O funcionario nao pode se aposentar")

s_client.close()

