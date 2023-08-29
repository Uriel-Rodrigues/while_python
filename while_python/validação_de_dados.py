# progama que leia o sexo de uma pessoa mas so aceite S ou M cado esteja errado faça a digitação novamente ate
# estar correto

sexo = str(input('digite o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos, por favor digite o seu sexo M para masculino e F para feminino '))
#if sexo in 'MmFf':
#   print('dados registados com sucesso!')
print('dados registrados com sucesso!')