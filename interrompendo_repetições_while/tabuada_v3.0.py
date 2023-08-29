# programa que mostre a tabuada dos numeros solictados pelo usuario um de cada vez, e só pare
# quando o numero digitado for negativo

print('- - - - - - - - - - GERADOR DE TABUADAS - - - - - - - - - -')

while True:
    numero = int(input('digite um numero para ver a tabuada [numeros negativos para parar]: '))
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    if numero < 0:
        break

    for c in range(1,11):
        print('{} x {} = {}'.format(c, numero, c*numero ))
    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('GERADOR DE TABUADA ENCERRADO ')
