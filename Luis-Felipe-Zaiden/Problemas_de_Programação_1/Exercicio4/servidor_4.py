import socket

host = socket.gethostname()
port = 5000

print('Aguardando conexão de um cliente')

s_server = socket.socket()
s_server.bind((host, port))

s_server.listen(1)
con, addr = s_server.accept()

while True:
    mensagem = con.recv(1024).decode()

    if not mensagem:
        break

    altura, sexo = mensagem.split(' ')

    altura = float(altura)


    if sexo.lower() == "masculino":
        peso_ideal = (72.7*altura) - 58
    elif sexo.lower() == "feminino":
        peso_ideal = (62.1*altura) - 44.7

    peso_ideal = str(peso_ideal)
    con.send(peso_ideal.encode())

con.close()



