import socket
import _thread
import threading
host = "localhost"
port = 5000

lock = threading.Lock()

def handle_thread (con) :
    while True:
        mensagem = con.recv(1024).decode()

        if not mensagem:
            lock.release()
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

s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_server.bind((host, port))

s_server.listen(3)

while True:
    con, addr = s_server.accept()
    print('Conectado')
    lock.acquire()
    _thread.start_new_thread(handle_thread,(con,))
con.close
