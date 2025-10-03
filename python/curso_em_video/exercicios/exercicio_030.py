'''Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.'''

'''n = int(input('Digite um número inteiro: '))
conv = n % 2
if conv1 == 0:
    print(f'O número {n} é PAR!')
if conv1 == 1:
    print(f'O número {n} é ÍMPAR!')'''


n = int(input('\033[93mDiga-me um número quualquer: '))
conv = n % 2
if conv == 0:
    print(f'\033[97mO número {n} é \033[94mPAR')
else:
    print(f'\033[97mO número {n} é \033[95mÍMPAR')
