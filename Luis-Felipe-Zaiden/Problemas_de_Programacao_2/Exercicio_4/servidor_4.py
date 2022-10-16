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

        altura, sexo = mensagem.split(' ')

        altura = float(altura)


        if sexo.lower() == "masculino":
            peso_ideal = (72.7*altura) - 58
        elif sexo.lower() == "feminino":
            peso_ideal = (62.1*altura) - 44.7

        peso_ideal = str(peso_ideal)
        con.send(peso_ideal.encode())

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
