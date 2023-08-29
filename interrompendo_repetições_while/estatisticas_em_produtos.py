#programa que leia o nome, o preço de varios produtos, programa deve perguntar se o usuario vai continuar ou nao
#no final mostre
# 1 - total gasto na compra
# 2 - quantos produtos custam mais de 1000
# 3 - nome do produto mais barato


soma = 0
contpreço = 0
contprod = 0
menor = 0
barato =' '
while True:
    produto = str(input('nome do produto comprado: ')).strip()
    preço = float(input('preço do produto comprado: '))

    contprod = contprod + 1
    soma = soma + preço #aqui calculamos o total gasto

    if preço > 1000: #aqui vai adicionar 1 todas as vezes que o produto for maior que 1000
        contpreço = contpreço + 1
    if contprod == 1 or preço < menor:
        menor = preço
        barato = produto


    fim = str(input('deseja para de registrar as compras? [SIM/NAO]: ')).strip().upper()
    fimerro = ' '

    if fim not in 'SIMNAO':
        while fimerro not in 'SIMNAO':
            fimerro = str(input('resposta incorreta, deseja para de registrar as compras? [SIM/NAO]: ')).strip().upper()

            if fimerro in 'SIM':
                break
    if fim in 'SIM':
            break
print('\n---------- FIM DO REGISTRO ----------')
print('total gasto {} R$'.format(soma))
print('\n{} produtos acima de 1000 R$'.format(contpreço))
print('\nproduto mais barato -> {} no valor de -> {} R$'.format(barato, menor))
