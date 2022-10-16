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

    nome, nivel, salario_bruto, nd = mensagem.split(' ')

    salario_bruto = float(salario_bruto)
    nd = float(nd)

    if nivel.upper() == "A":
        if nd > 0:
            salario = salario_bruto - (salario_bruto * 0.08)
        if nd == 0:
            salario = salario_bruto - (salario_bruto * 0.03)
    if nivel.upper() == "B":
        if nd > 0:
            salario = salario_bruto - (salario_bruto * 0.1)
        if nd == 0:
            salario = salario_bruto - (salario_bruto * 0.05)
    if nivel.upper() == "C":
        if nd > 0:
            salario = salario_bruto - (salario_bruto * 0.15)
        if nd == 0:
            salario = salario_bruto - (salario_bruto * 0.08)
    if nivel.upper() == "D":
        if nd > 0:
            salario = salario_bruto - (salario_bruto * 0.17)
        if nd == 0:
            salario = salario_bruto - (salario_bruto * 0.1)
    

    salario = str(salario)

    nome = (nome + ' ')
    nivel = (nivel + ' ')

    con.send(nome.encode())
    con.send(nivel.encode())
    con.send(salario.encode())

con.close()



