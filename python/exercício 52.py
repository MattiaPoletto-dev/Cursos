'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

print('\033[93m-_' * 20)
print('¡\033[97m       Leitor de números primos       \033[93m!')
print('-_' * 20)

num = int(input('Digite um número inteiro: '))

tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[92m', end = ' ')
        tot += 1
    else:
        print('\033[91m',end = ' ')
    print(f'{c}',end = ' ')
print(f'\n\033[97mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} NÃO é primo')
