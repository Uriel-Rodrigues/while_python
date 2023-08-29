#programa que le a idade, sexo e nome de varias pessoas, no fim de cada pessoa cadastrada o programa deve perguntar se
# a pessoa quer continuar e no, fim deve aparecer
# 1 - quantas pessoas tem mais de 18 anos
# 2 - quantos homens foram cadastrados
# 3 - quantas mulheres tem menos de 20 anos

contidade = 0
contsexo = 0
contmulheres = 0
print('------------- REGISTRO DE PESSOAS -------------')
while True:
    sexo = str(input('digite o sexo para registro [MASCULINO/FEMININO]: ')).strip().upper()
    idade = int(input('\ndigite a idade para registro: '))
    nome = str(input('\ndigite o nome compreto para registro: ')).strip()

    if idade > 18:
        contidade = contidade + 1
    if sexo in 'MASCULINO':
        contsexo = contsexo + 1
    if sexo in 'FEMININO' and idade < 20:
        contmulheres = contmulheres + 1

    fim = str(input('deseja parar os registros? [SIM/NAO]: ')).strip().upper()
    fimcond = ' '
    if fim not in 'SIMNAO':
        while fimcond not in 'SIMNAO':
            fimcond = str(input('\nresposta incorreta, deseja parar os registros? [SIM/NAO]: ')).strip().upper()

            if fimcond in 'SIM':
                break
    if fim in 'SIM':
        break

print('-------------- RESULTADO DO REGISTRO --------------')
print('[1] - registradas {} pessoas maiores de 18 anos    '.format(contidade))
print('[2] - registrados {} homens                        '.format(contsexo))
if contmulheres == 1:
    print('[3] - resgidtrada {} mulher com menos de 20 anos'.format(contmulheres))
else:
    print('[3] - resgidtradas {} mulheres com menos de 20 anos'.format(contmulheres))
print('---------------------------------------------------')