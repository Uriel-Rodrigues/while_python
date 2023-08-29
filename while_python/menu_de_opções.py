#programa que leia dois valores e mostre um menu
#[1] somar
#[2] multiplicar
#[3] novos numeros
#[4] sair do programa
#o programa deve realizar a operação escolhida
from time import sleep

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

resposta = 0

while resposta != 5:
    print('agora escolha o que deseja fazer')
    print('------------ MENU -------------')
    print('| [1] somar os numeros        |')
    print('| [2] multiplicar os numeros  |')
    print('| [3] ver o maior dos numeros |')
    print('| [4] digitar novos numeros   |')
    print('| [5] sais do programa        |')
    print('-------------------------------')
    resposta = int(input('qual sua escolha?: '))

    if (resposta == 1):
        soma = n1+n2
        print('a soma dos numeros é {} \n'.format(soma))
        sleep(2)

    elif (resposta == 2):
        multi = n1 * n2
        print('a multiplicação dos numeros digitados é {} \n'.format(multi))
        sleep(2)

    elif (resposta == 3):
        if (n1 > n2):
            print('o numero {} é maior que o numero {}\n'.format(n1, n2))
            sleep(2)
        elif (n2 > n1):
            print('o numero {} é maior que o numero {}\n'.format(n2, n1))
            sleep(2)
        elif (n1 == n2):
            print('os numeros digitados são iguais\n')
            sleep(2)

    elif (resposta == 4):
            n1 = n1nv = int(input('digite o novo primeiro numero: '))
            n2 = n2nv = int(input('digite o novo segundo numero: '))
    elif (resposta == 5 ):
        print('finalizando o programa')
        sleep(2)
        print('programa finalizado com sucesso, programa offline...')
    else:
        print('opção invalida, tente novamente')
