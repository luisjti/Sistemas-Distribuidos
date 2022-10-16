import socket
import _thread
import threading
host = "localhost"
port = 5000

lock = threading.Lock()

def handle_thread (con) :
    while True:
        idade = con.recv(1024).decode()

        if not idade:
            lock.release()
            break
        
        idade = int(idade)

        if idade > 4 and idade < 8:
            mensagem = "Infantil A"
        elif idade > 7 and idade < 11:
            mensagem = "Infantil B"
        elif idade > 10 and idade < 14:
            mensagem = "Juvenil A"
        elif idade > 13 and idade < 18:
            mensagem = "Juvenil B"
        elif idade >=18:
            mensagem = "Adulto"
        
        con.send(mensagem.encode())
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
