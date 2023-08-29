# programa que leia numeros do teclado e mostre um somatorio no final sem considerar o flag
# so para quando o usuario digitar 999 (condição de parada)

cont = soma = 0
while True:
    numero = int(input('digite um numero: '))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero

print(f'a quantidade de numeros digitados foi {cont} e o somatorio desses numeros é {soma}')


