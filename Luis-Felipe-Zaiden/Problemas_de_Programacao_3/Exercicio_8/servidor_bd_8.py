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
        saldo_medio = float(mensagem)
        if saldo_medio <=200:
            n = 0
        elif saldo_medio >200 and saldo_medio<=400:
            n = arquivo.readlines()[0]
        elif saldo_medio >400 and saldo_medio<=600:
            n = arquivo.readlines()[1]
        elif saldo_medio >600:
            n = arquivo.readlines()[2]

        arquivo.close()
        con.send(n.encode())

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
