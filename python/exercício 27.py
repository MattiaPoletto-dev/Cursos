'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.'''

#não consegui
'''nome = str(input('Digite seu nome completo: ')).strip().title()
conv1 = nome.split()[0]
conv2 = nome.split()
print(f'Primeiro nome: {conv1}')
print(f'Último nome: {}')'''


nome = str(input('\033[93mDigite seu nome completo: ')).strip().title()
n1 = nome.split()
n2 = len(n1) - 1
n3 = nome.split()[n2]
print('\033[97mMuito prazer em te conhecer!')
print(f'Seu primeiro nome é \033[92m{n1[0]}\033[97m.')
print(f'Seu último nome é \033[92m{n3}\033[97m.')
