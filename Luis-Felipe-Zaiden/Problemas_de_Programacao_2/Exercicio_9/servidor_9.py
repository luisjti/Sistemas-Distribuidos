import socket
import _thread
import threading
host = "localhost"
port = 5000

lock = threading.Lock()

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def nome(self):
        valor_carta = {1: 'As', 2: 'Dois', 3: 'Tres', 4: 'Quatro', 
        5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove',
        10: 'Dez', 11: 'Valete', 12: 'Dama', 13: 'Rei'}
        naipe_carta = {1: 'Ouros',2:'Pus',3: 'Copas',4: 'Espadas'}
        nome_carta = 'A sua carta e: ' + valor_carta[self.valor] + ' de ' + naipe_carta[self.naipe]
        return (nome_carta)

def handle_thread (con) :
    while True:
        mensagem = con.recv(1024).decode()

        if not mensagem:
            lock.release()
            break

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
