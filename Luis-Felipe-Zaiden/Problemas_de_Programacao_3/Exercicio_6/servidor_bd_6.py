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
        if mensagem.upper() == "A":
            linha = arquivo.readlines()[0]
            con.send(linha.encode())
        elif mensagem.upper() == "B":
            linha = arquivo.readlines()[1]
            con.send(linha.encode())
        elif mensagem.upper() == "C":
            linha = arquivo.readlines()[2]
            con.send(linha.encode())
        elif mensagem.upper() == "D":
            linha = arquivo.readlines()[3]
            con.send(linha.encode())
        arquivo.close()

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
