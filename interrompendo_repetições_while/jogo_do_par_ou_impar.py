#programa que jogue par ou impar com o computador, o jogo para quando o jogador perder
#mostrando o total de vitoria consecutivas no fim do jogo
from random import randint
vitoria = 0
print('-*-*-*-*-*-*-*-*-*- JOGO DO IMPAR OU PAR -*-*-*-*-*-*-*-*-*-')
nome = str(input('qual o seu nome jogador?: ')).upper()
while True:
    jogador = int(input('escolha um numero entre 0 e 10: '))
    computador = randint(0, 10)
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR?: ')).strip().upper()[0]
    if tipo == 'P':
        if soma%2 == 0:
            print('voce escolheu {}, computador escolheu {}, o resultado foi {}'.format(jogador, computador, soma))
            print('{} GANHOU!'.format(nome))
            vitoria = vitoria + 1
        else:
            print('voce escolheu {}, computador escolheu {}, o resultado foi {}'.format(jogador, computador, soma))
            print('COMPUTADOR GANHOU!')
            break
    elif tipo == 'I':
        if soma%2 == 1:
            print('voce escolheu {}, computador escolheu {}, o resultado foi {}'.format(jogador, computador, soma))
            print('{} GANHOU'.format(nome))
            vitoria = vitoria + 1
        else:
            print('voce escolheu {}, computador escolheu {}, o resultado foi {}'.format(jogador, computador, soma))
            print('COMPUTADOR GANHOU!')
            break
print('fim do programa [PAR OU IMPAR] você ganhou {} vezes'.format(vitoria))