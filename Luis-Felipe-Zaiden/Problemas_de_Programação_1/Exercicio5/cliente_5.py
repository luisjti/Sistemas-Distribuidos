import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

idade = input(" Digite a idade: ")

s_client.send(idade.encode())

mensagem = s_client.recv(1024).decode()


print("A categoria e: ", mensagem)

s_client.close()

