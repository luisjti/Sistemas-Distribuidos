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

s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_server.bind((host, port))

s_server.listen(3)

while True:
    con, addr = s_server.accept()
    print('Conectado')
    lock.acquire()
    _thread.start_new_thread(handle_thread,(con,))
con.close
