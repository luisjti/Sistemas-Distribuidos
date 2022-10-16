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

    nome, sexo, idade = mensagem.split(' ')

    idade = float(idade)
    maioridade = 0

    if sexo.lower() == "masculino":
        if idade >= 18:
            maioridade = 1
    elif sexo.lower() == "feminino":
        if idade >= 21:
            maioridade = 1
    
    maioridade = str(maioridade)
    con.send(maioridade.encode())

con.close()



