import socket
import _thread
import threading
host = "localhost"
port = 5000
port2 = 8000
lock = threading.Lock()

def handle_thread (con) :
    while True:
        saldo_medio = con.recv(1024).decode()

        if not saldo_medio:
            lock.release()
            break

        s2_client = socket.socket()
        s2_client.connect((host, port2))
        s2_client.send(saldo_medio.encode())  
        mensagem2 = s2_client.recv(1024).decode()
        saldo_medio = float(saldo_medio)
        n = float(mensagem2)
        credito = saldo_medio * n
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
