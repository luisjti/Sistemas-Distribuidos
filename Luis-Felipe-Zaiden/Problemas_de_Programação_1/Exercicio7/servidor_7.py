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

    idade, tempo= mensagem.split(' ')
 
    idade = int(idade)
    tempo = int(tempo)

    if idade >=65:
        aposentar = "1"
    elif tempo >=30:
        aposentar = "1"
    elif tempo >=25 and idade >= 60:
        aposentar = "1"
    else :
        aposentar = "0"


    con.send(aposentar.encode())

con.close()



