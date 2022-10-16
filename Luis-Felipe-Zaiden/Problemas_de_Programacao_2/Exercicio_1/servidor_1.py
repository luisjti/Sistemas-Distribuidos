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

        nome, cargo, salario = mensagem.split(' ')
       
        salario = float(salario)

        if cargo.lower() == "programador":
            salario = salario * 1.18
        elif cargo.lower() == "operador":
            salario = salario * 1.2

        salario = str(salario)
        con.send(salario.encode())

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
