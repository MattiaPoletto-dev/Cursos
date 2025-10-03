'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Case esteja errado,
peça a digitação novamente até ter um valor correto.'''

#Minha resolução
'''s = ' '
nome = str(input('Nome: '))
while s not in 'MmFf':
    s = str(input('Sexo [M/F]: '))
    if s not in 'MmFf:':
        s = 'a'
if s in 'Mm':
    print(f'{nome} é do sexo masculino')
elif s in 'Ff':
    print(f'{nome} é do sexo feminino')'''

#Resolução igual ao do vídeo
print('----- DADOS -----')
nome = str(input('Nome: '))
idade = int(input('Idade: '))
sexo = str(input('Sexo [M/F]: ')).strip().upper()
while sexo not in 'M' and sexo not in 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
if sexo == 'M':
    print(f'Seu nome é {nome}, tem {idade} anos de idade e é do sexo masculino')
elif sexo == 'F':
    print(f'Seu nome é {nome}, tem {idade} anos de idade e é do sexo feminino')
