import socket

host = socket.gethostname()
port = 5000

print('Aguardando conexão de um cliente')

s_server = socket.socket()
s_server.bind((host, port))

s_server.listen(1)
con, addr = s_server.accept()

while True:
    idade = con.recv(1024).decode()

    if not idade:
        break

    idade = int(idade)

    if idade > 4 and idade < 8:
        mensagem = "Infantil A"
    elif idade > 7 and idade < 11:
        mensagem = "Infantil B"
    elif idade > 10 and idade < 14:
        mensagem = "Juvenil A"
    elif idade > 13 and idade < 18:
        mensagem = "Juvenil B"
    elif idade >=18:
        mensagem = "Adulto"
        
    con.send(mensagem.encode())

con.close()



