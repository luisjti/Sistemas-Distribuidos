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
        idade, tempo = mensagem.split()
        idade = int(idade)
        tempo = float(tempo)
        linha = arquivo.readline()
        linha = int(linha)
        linha2 = arquivo.readline()
        linha2 = int(linha2)
        linha3 = arquivo.readline()
        l3,l4= linha3.split(' ')
        l3 = int(l3)
        l4 = int(l4)
        print(l3,l4)
        if  idade >= linha :
            aposentar = '1'
        elif tempo >= linha2:
            aposentar = '1'
        elif idade >= l3 and tempo >= l4:
            aposentar = '1'
        else:
            aposentar = '0'

        con.send(aposentar.encode())
        arquivo.close()

           
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
