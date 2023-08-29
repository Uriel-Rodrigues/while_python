#refazer o desafio 51, lendo o primeiro termo e a razão de uma PA, postrando os 10 primeiros termos da progressão
#usando while

ptpa = int(input('digite o primeiro termo da PA: '))
razao = int(input('digite a razão da PA: '))
termo = int(input('digite qte qual termo que ver: '))

primeiro = ptpa
cont =1

while cont != termo:
    if cont != termo:
        print('{} -> '.format(primeiro), end='')
        primeiro = primeiro + razao
        cont = cont + 1
    if cont == termo:
        print(ptpa + ((termo +1) * razao))

