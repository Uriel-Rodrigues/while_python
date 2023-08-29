# programa que leia varios numeros inteiros e mostre:
    # media dos valores
    # valor maior
    # valor menor
# o programa deve perguntar se ele quer ou nao continuar digitando

parada = ''
soma = 0
maior = 0
menor = 0
cont = 0
while parada in 'NAO':
    numero = int(input('digite um numero: '))
    parada = str(input('gostaria de parar [sim/nao]: ')).upper()

    soma = soma + numero
    cont = cont + 1
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma/cont
print('---------- DIAGNOSTICO ----------')
print(' você digitou {} numero e a media dos numeros digitados é {}\n'.format(cont, media))
print('dos numeros digitados o maior é {} e o menor é {}'.format(maior, menor))



