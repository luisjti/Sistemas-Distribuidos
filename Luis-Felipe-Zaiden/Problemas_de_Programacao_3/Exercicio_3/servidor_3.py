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

        n1, n2, n3 = mensagem.split(' ')

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
    
        m = (n1+n2)/2
        m2 = str(m)
    
        s2_client = socket.socket()
        s2_client.connect((host, port2))
        s2_client.send(m2.encode())  
        mensagem2 = s2_client.recv(1024).decode()

        if mensagem2 == '2':
            aprovado = '1'
        elif mensagem2 == '1':
            if (n3 + m)/2 >= 5:
                aprovado = '1'
            else:
                aprovado = '0'
        else:
            aprovado = '0'
        
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
