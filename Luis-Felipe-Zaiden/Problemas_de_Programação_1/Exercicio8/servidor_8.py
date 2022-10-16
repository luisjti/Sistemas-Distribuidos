import socket

host = socket.gethostname()
port = 5000

print('Aguardando conexão de um cliente')

s_server = socket.socket()
s_server.bind((host, port))

s_server.listen(1)
con, addr = s_server.accept()

while True:
    saldo_medio = con.recv(1024).decode()

    if not saldo_medio:
        break

    saldo_medio = float(saldo_medio)

    if saldo_medio <=200:
        credito = 0
    elif saldo_medio >200 and saldo_medio<=400:
        credito = saldo_medio *0.20
    elif saldo_medio >400 and saldo_medio<=600:
        credito = saldo_medio *0.30
    elif saldo_medio >600:
        credito = saldo_medio *0.40


    saldo_medio= str(saldo_medio)
    credito = str(credito)

    saldo_medio = (saldo_medio + ' ')

    con.send(saldo_medio.encode())
    con.send(credito.encode())

con.close()



