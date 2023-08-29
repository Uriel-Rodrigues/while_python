#programa que simula o funcionamento de um caixa eletronico, no inicio pergunte ao usuario qual o valor a ser retirado
#(numero inteiro) e depois informe quantas cedulas de cada valor serão entregues
#OBS: o caixa possui cedulas de R$50, R$20, R$10 e R$1

valor = int(input('digite o valor da retirada:R$ '))
total = valor
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total = total - cedula
        cont = cont + 1
    else:
        if cont > 0:
            print('{} cedulas de {}'.format(cont, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break
