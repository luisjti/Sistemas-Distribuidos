import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

nome = input(" Digite o nome: ")
nivel = input(" Digite o nivel: ")
salario_bruto = input(" Digite o salario bruto: ")
nd = input(" Digite o numero de dependentes: ")

nome = (nome + ' ')
nivel = (nivel + ' ')
salario_bruto = (salario_bruto + ' ')

s_client.send(nome.encode())
s_client.send(nivel.encode())
s_client.send(salario_bruto.encode())
s_client.send(nd.encode())

mensagem = s_client.recv(1024).decode()

nome, nivel, salario_liquido= mensagem.split(' ')


print('Nome: ', nome, "\nNivel: ",nivel,"\nSalario Liquido: ",salario_liquido)

s_client.close()

