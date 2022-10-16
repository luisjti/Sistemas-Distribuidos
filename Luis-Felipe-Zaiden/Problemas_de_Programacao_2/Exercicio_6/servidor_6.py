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

        nome, nivel, salario_bruto, nd = mensagem.split(' ')

        salario_bruto = float(salario_bruto)
        nd = float(nd)

        if nivel.upper() == "A":
            if nd > 0:
                salario = salario_bruto - (salario_bruto * 0.08)
            if nd == 0:
                salario = salario_bruto - (salario_bruto * 0.03)
        if nivel.upper() == "B":
            if nd > 0:
                salario = salario_bruto - (salario_bruto * 0.1)
            if nd == 0:
                salario = salario_bruto - (salario_bruto * 0.05)
        if nivel.upper() == "C":
            if nd > 0:
                salario = salario_bruto - (salario_bruto * 0.15)
            if nd == 0:
                salario = salario_bruto - (salario_bruto * 0.08)
        if nivel.upper() == "D":
            if nd > 0:
                salario = salario_bruto - (salario_bruto * 0.17)
            if nd == 0:
                salario = salario_bruto - (salario_bruto * 0.1)
    

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
