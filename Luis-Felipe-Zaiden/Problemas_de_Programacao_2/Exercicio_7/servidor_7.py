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

        idade, tempo= mensagem.split(' ')
 
        idade = int(idade)
        tempo = int(tempo)

        if idade >=65:
            aposentar = "1"
        elif tempo >=30:
            aposentar = "1"
        elif tempo >=25 and idade >= 60:
            aposentar = "1"
        else :
            aposentar = "0"


        con.send(aposentar.encode())
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
