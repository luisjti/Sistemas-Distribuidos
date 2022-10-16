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
        linha = arquivo.readline()
        linha = float(linha)
        linha2 = arquivo.readline()
        linha2 = float(linha2)
        mensagem = float(mensagem)
        if mensagem >= linha:
            aprovado= '2'
        elif mensagem >= linha2:
            aprovado = '1'
        else:
            aprovado = '0'
       
        con.send(aprovado.encode())
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
