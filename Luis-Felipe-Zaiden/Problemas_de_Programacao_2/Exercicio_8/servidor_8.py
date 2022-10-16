import socket
import _thread
import threading
host = "localhost"
port = 5000

lock = threading.Lock()

def handle_thread (con) :
    while True:
        saldo_medio= con.recv(1024).decode()

        if not saldo_medio:
            lock.release()
            break

        saldo_medio = float(saldo_medio)

        if saldo_medio <=200:
            credito = 0
        elif saldo_medio >200 and saldo_medio<=400:
            credito = saldo_medio *0.20
        elif saldo_medio >400 and saldo_medio<=600:
            credito = saldo_medio *0.30
        elif saldo_medio >600:
            credito = saldo_medio *0.40


        credito = str(credito)

        con.send(credito.encode())

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
