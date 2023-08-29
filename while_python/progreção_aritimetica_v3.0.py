#melhorar o desafio 61 perguntando ao usuario se ele gostaria de mostrar mais alguns termos
#o programa termina quando o usuario disse que quer mostrar 0 termos

#ptpa = int(input('digite o primeiro termo da PA: '))
#razao = int(input('digite a razão da PA: '))

#termo = ptpa
#cont = 1
#total = 0
#mais = 10

#while mais != 0:
#    total = total + mais
#    while cont <= total:
#        print('{} -> '.format(termo),end='')
#        termo = termo + razao
#        cont = cont + 1
#    print('PAUSA')
#    mais = int(input('quantos termos voce que vera mais? '))
#print('PAUSA')


primeiro = int(input('digite o primeiro termo da PA: '))
razao = int(input('digite a razão da sua PA: '))
termo = int(input('digite o ultimo termo que quer ver: '))

cont = 1
mais = termo
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(primeiro),end='')
        primeiro = primeiro + razao
        cont = cont + 1
    print('FIM')
    mais = int(input('quer ver mais termos?: '))
print('laço finalizado...')
