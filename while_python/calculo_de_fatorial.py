#programa que leia um numero e mostre o seu fatorial

n = int(input('digite um numero: '))
c = n
f = 1
print('calculando {} fatorial {}! = '.format(n,n),end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ',end='')
    else:
        print(' = ',end='')
    f = f * c
    c = c - 1
print('{}'.format(f),end='')

