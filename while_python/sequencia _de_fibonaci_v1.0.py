#programa que leia um numero N qualquer e mostre os N primeiroelementos de uma sequencia de fibonacci

#sequencia possui '1' como seus dois peimeiros termos e depois os proximos, são dados pela somados dois anteriores
#ex: 1,1,2,3,5,8,13,14.....

print('-*-*-*-*-*-> SEQUENCIA DE FIBONACCI <-*-*-*-*-*-\n')
n = int(input('quantos termos você quer mostrar? '))
inicio = 0
while inicio != n+1:
    termo = (((1.618034) ** inicio) - ((1 - 1.618034) ** inicio))/5 ** (1/2)
    formatar = int(termo)
    print('{} -> '.format(formatar),end='')
    inicio = inicio + 1
print('FIM')
print('o seu {} termo corresponde a {}'.format(n, int((((1.618034) ** n) - ((1 - 1.618034) ** n))/5 ** (1/2))))
