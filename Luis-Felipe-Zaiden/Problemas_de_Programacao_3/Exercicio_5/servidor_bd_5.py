import socket
import _thread
import threading
host = "localhost"
port = 8000

lock = threading.Lock()

def handle_thread (con) :
    while True:
        mensagem = con.recv(1024).decode()

        if not mensagem:
            lock.release()
            break
        arquivo = open("bd.txt","r")
        idade = int(mensagem)
        if idade > 4 and idade < 8:
            linha = arquivo.readlines()[0]
        elif idade > 7 and idade < 11:
            linha = arquivo.readlines()[1]
        elif idade > 10 and idade < 14:
            linha = arquivo.readlines()[2]
        elif idade > 13 and idade < 18:
            linha = arquivo.readlines()[3]
        elif idade >=18:
            linha = arquivo.readlines()[4]
        arquivo.close()
        linha = linha.strip()
        con.send(linha.encode())
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
