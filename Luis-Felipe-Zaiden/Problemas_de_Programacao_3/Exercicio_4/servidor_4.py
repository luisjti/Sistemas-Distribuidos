import socket
import _thread
import threading
host = "localhost"
port = 5000
port2 = 8000
lock = threading.Lock()

def handle_thread (con) :
    while True:
        mensagem = con.recv(1024).decode()

        if not mensagem:
            lock.release()
            break

        altura, sexo = mensagem.split(' ')

        altura = float(altura)

        s2_client = socket.socket()
        s2_client.connect((host, port2))
        s2_client.send(sexo.encode())  
        mensagem2 = s2_client.recv(1024).decode()

        n1,n2 = mensagem2.split(' ')
        n1 = float(n1)
        n2 = float(n2)
        peso = (n1*altura) - n2

        peso = str(peso)
        con.send(peso.encode())

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
