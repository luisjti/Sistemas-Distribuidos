import zmq, time
HOST = '*'
PORT = '8000'

context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
s.bind("tcp://*:8000")

while True:
    time.sleep(2) 
    salario = 'SALARIO JOSE PROGRAMADOR 1000'
    s.send_string(salario)

    time.sleep(2) 
    maioridade = 'MAIORIDADE JOSE MASCULINO 20'
    s.send_string(maioridade)
     
    time.sleep(2) 
    notas = 'NOTAS 10 6 3'
    s.send_string(notas)
     
    time.sleep(2) 
    peso = 'PESO 1.76 MASCULINO'
    s.send_string(peso)

    time.sleep(2) 
    classe = 'CLASSE 10'
    s.send_string(classe)

    time.sleep(2) 
    salario = 'SLIQUIDO JOSE A 1000 2'
    s.send_string(salario)

    time.sleep(2) 
    aposentar = 'APOSENTAR 56 35'
    s.send_string(aposentar)
    
    time.sleep(2) 
    saldo = 'SALDO 300'
    s.send_string(saldo)
