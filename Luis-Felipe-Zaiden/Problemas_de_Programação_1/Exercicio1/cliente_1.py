import socket

host = socket.gethostname()
port = 5000

s_client = socket.socket()
s_client.connect((host, port))

nome = input(" Digite o nome do funcionario: ")
salario = input(" Digite o salario do funcionario: ")
cargo = input(" Digite o cargo do funcionario: ")

nome = (nome + ' ')
salario = (salario + ' ')

s_client.send(nome.encode())
s_client.send(salario.encode())
s_client.send(cargo.encode())

mensagem = s_client.recv(1024).decode()
nome,salario,cargo = mensagem.split(' ')
print('Nome: ', nome, '\nSalario: ' ,salario)

s_client.close()

