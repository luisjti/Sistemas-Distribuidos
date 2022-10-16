import socket
import _thread
import threading
host = "localhost"
port = 8000

lock = threading.Lock()

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def nome(self):
        arquivo = open("bd.txt","r")
        content = arquivo.readlines()
        valor_carta = content[self.valor-1]
        valor_carta = valor_carta.strip()
        naipe_carta = content[self.naipe+12]
        naipe_carta = naipe_carta.strip()
        nome_carta = 'A sua carta e: ' + valor_carta + ' de ' + naipe_carta
        arquivo.close()
        return (nome_carta)

def handle_thread (con) :
    while True:
        mensagem = con.recv(1024).decode()

        if not mensagem:
            lock.release()
            break
        print(mensagem)
        valor, naipe = mensagem.split(' ')
        valor = int(valor)
        naipe = int(naipe)
        carta = Carta(valor, naipe)
        mensagem = carta.nome()
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
