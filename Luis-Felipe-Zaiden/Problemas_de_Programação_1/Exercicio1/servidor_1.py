import socket

host = socket.gethostname()
port = 5000

s_server = socket.socket()
s_server.bind((host, port))

s_server.listen(1)
con, addr = s_server.accept()

while True:
    mensagem = con.recv(1024).decode()

    if not mensagem:
        break

    nome, salario, cargo = mensagem.split(' ')

    salario = float(salario)

    if cargo.lower() == "programador":
        salario = salario * 1.18
    elif cargo.lower() == "operador":
        salario = salario * 1.2

    salario = str(salario)
    nome = (nome + ' ')
    salario = (salario + ' ')

    con.send(nome.encode())
    con.send(salario.encode())
    con.send(cargo.encode())

con.close()



