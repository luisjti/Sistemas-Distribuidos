import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

saldo_medio = input(" Digite o saldo medio: ")


s_client.send(saldo_medio.encode())

mensagem = s_client.recv(1024).decode()

saldo_medio, credito = mensagem.split(" ")

credito = float(credito)
print("Saldo medio: ", saldo_medio, "\nValor do credito: {:.2f}".format(credito))

s_client.close()

