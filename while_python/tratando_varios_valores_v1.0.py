# programa que leia varios numeros no teclado e so pare quando usuario digitar 999, no fim mostre
#-> quantos numeros foram digitados
#-> a soma entre os numeros

numero = int(input('digite um numero [999 para parar]: '))
cont = 0
soma = 0
while numero != 999:
    cont = cont + 1
    soma = soma + numero
    numero = int(input('digite um numero [999 para parar]: '))
print('foram digitados {} numeros e a soma deles é {}'.format(cont,soma))