import socket
import _thread
import threading
import random
import time

host = "localhost"
port = 5000

lock = threading.Lock()
mutex = 1
full = 0
empty = 5
buffeer = []

def producer_thread (con) :
    global full, empty, mutex 
    print ('PRODUTOR ONLINE')
    while True:
        produced = con.recv(1024).decode()

        #print (produced)
        if not produced:
            break

        if mutex == 1 and full < 5:
            mutex = mutex - 1
            empty = empty - 1

            buffeer.insert(full, produced)
            print('Produzido {}'.format(buffeer[full]))

            mutex = mutex + 1
            full = full + 1
         
        else :
            print('Buffer cheio, aguarde')
            while (full >= 5) :
                time.sleep(6)
                
    con.close()

def consumer_thread (con) :
    global full, empty, mutex 
    print ('CONSUMIDOR ONLINE')
    while True:
        msg = con.recv(1024).decode()
        if msg == '1'  :
         if mutex == 1 and empty < 5 :
      
            mutex = mutex - 1
            full = full - 1

            x = buffeer [full]
            buffeer.remove(x)
            con.send(x.encode())

            mutex = mutex +1
            empty = empty + 1
            time.sleep(2)
  
         else:
            con.send('Buffer vazio'.encode())
            while (empty >= 5):
                time.sleep(6)
        
s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_server.bind((host, port))

s_server.listen(3)

while True:
 con, addr = s_server.accept()
 aux = input('Digite 1 para conectar um produtor e 2 para um consumidor: ')
 aux = int(aux)

 if aux == 1:
  _thread.start_new_thread(producer_thread,(con,))

 if aux == 2:
  _thread.start_new_thread(consumer_thread,(con,))
 
con.close
