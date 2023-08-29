#melhorar o jogo do desafio 28
#jogador deve jogar ate adivinhar o numero escolhido e no final o comudador mostras quantas vezes o usuario errou

import random
from time import sleep
lista = [0,1,2,3,4,5,6,7,8,9,10]

print('quer jogar de novo? adivinhe o numero de 0 a 10 que eu escolhi ')
escolha = random.choice(lista)
print('ja escolhi meu numero qual voce acha que foi ?')
resposta = int(input('digite sua resposta: '))

cont = 0

while resposta != escolha:
    resposta = int(input('tente de novo: '))
    cont = cont + 1
    if resposta > escolha:
        print('menos.... tente mais uma vez')
    if resposta < escolha:
        print('mais... tente mais uma vez')
print('agora sim! voce acertou mas levaram {} tentativas'.format(cont))

