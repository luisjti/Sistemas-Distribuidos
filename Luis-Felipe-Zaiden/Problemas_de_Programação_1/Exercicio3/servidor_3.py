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

    n1, n2, n3 = mensagem.split(' ')

    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    
    m = (n1+n2)/2
  
    if m >=7:
        aprovado = 1
    elif m > 3:
        if (n3 + m)/2 >= 5:
            aprovado = 1
    else :
        aprovado = 0
   
    aprovado = str(aprovado)
    con.send(aprovado.encode())

con.close()



