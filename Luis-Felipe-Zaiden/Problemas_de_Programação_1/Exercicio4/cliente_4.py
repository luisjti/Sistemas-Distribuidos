import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

altura = input(" Digite a altura: ")
sexo = input(" Digite o sexo: ")

altura = (altura + ' ')

s_client.send(altura.encode())
s_client.send(sexo.encode())

mensagem = s_client.recv(1024).decode()

mensagem = float(mensagem)
print("Peso ideal:{:.2f} " .format(mensagem))

s_client.close()

