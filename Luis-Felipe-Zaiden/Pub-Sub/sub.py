import zmq
HOST = '*'
PORT = '8000'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
s.connect("tcp://localhost:8000") # how and where to communicate

questao = input("Digite o numero da questao: ")
questao = int(questao)
msgs = ['SALARIO','MAIORIDADE','NOTAS', 'PESO', 'CLASSE','SLIQUIDO','APOSENTAR','SALDO']
sub = msgs[questao-1]

s.setsockopt_string(zmq.SUBSCRIBE, sub) # subscribe 

while True: 
    dados = s.recv(1024).decode() # receive a message

    if not dados:
        break

    if questao == 1:
        aux,nome, cargo, salario = dados.split(' ')

        salario = float(salario)

        if cargo.lower() == "programador":
            salario = salario * 1.18
        elif cargo.lower() == "operador":
            salario = salario * 1.2

        salario = str(salario)
        print('Nome: {} \nSalario reajustado: {}'.format(nome, salario))

    if questao == 2:
        aux, nome, sexo, idade = dados.split(' ')

        idade = float(idade)
        maioridade = 0

        if sexo.lower() == "masculino":
           if idade >= 18:
               maioridade = 1
        elif sexo.lower() == "feminino":
           if idade >= 21:
               maioridade = 1
    
        maioridade = str(maioridade)
        if maioridade == '1' :
            print('A pessoas ja atingiu a maioridade')
        if maioridade == '0' :
            print('A pessoas ainda nao atingiu a maioridade')

    if questao == 3:
        aux, n1, n2, n3 = dados.split(' ')

        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
    
        m = (n1+n2)/2
        if m >=7:
            aprovado = 1
        elif m > 3:
            if (n3 + m)/2 >= 5:
                aprovado = 1
   
        if aprovado == 1:
            print('O aluno foi aprovado')
        else:
            print('O aluno foi reprovado')

    if questao == 4:
        aux, altura, sexo = dados.split(' ')

        altura = float(altura)

        if sexo.lower() == "masculino":
            peso_ideal = (72.7*altura) - 58
        elif sexo.lower() == "feminino":
            peso_ideal = (62.1*altura) - 44.7

        peso_ideal = int(peso_ideal)
        print('O peso ideal e: {}'.format(peso_ideal))

    if questao == 5:
        aux, idade = dados.split()
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
        print('A categoria e {}'.format(mensagem))

    if questao == 6:
        aux,nome, nivel, salario_bruto, nd = dados.split(' ')

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
        print('Nome: {} \nNivel: {}\nSalario Liquido: {} '.format(nome,nivel,salario))

    if questao == 7:
        aux, idade, tempo= dados.split(' ')
 
        idade = int(idade)
        tempo = int(tempo)

        if idade >=65:
            aposentar = "1"
        elif tempo >=30:
            aposentar = "1"
        elif tempo >=25 and idade >= 60:
            aposentar = "1"
        else :
            aposentar = "0"

        if aposentar == '1':
            print('O funcionario ja pode se aposentar')
        if aposentar == '0':
            print('O funcionario nao pode se aposentar')

    if questao == 8:
         aux, saldo_medio = dados.split(' ')
 
         saldo_medio = float(saldo_medio)

         if saldo_medio <=200:
             credito = 0
         elif saldo_medio >200 and saldo_medio<=400:
             credito = saldo_medio *0.20
         elif saldo_medio >400 and saldo_medio<=600:
             credito = saldo_medio *0.30
         elif saldo_medio >600:
             credito = saldo_medio *0.40

         print("Saldo medio: {} \nValor do credito: {:.2f}".format(saldo_medio, credito))
