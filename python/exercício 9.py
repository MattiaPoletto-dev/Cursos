'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.'''

########## Não funciona bonitinho pois algumas respostas ficam com 1 dígito.
'''n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 24)
print(f'{n} x  0 = {n * 0}   {n} x 10 = {n * 10} \n{n} x  1 = {n * 1}   {n} x 11 = {n * 11} \n{n} x  2 = {n * 2}   {n} x 12 = {n * 12} \n{n} x  3 = {n * 3}   {n} x 13 = {n * 13} \n{n} x  4 = {n * 4}   {n} x 14 = {n * 14}')
print(f'{n} x  5 = {n * 5}   {n} x 15 = {n * 15} \n{n} x  6 = {n * 6}   {n} x 16 = {n * 16} \n{n} x  7 = {n * 7}   {n} x 17 = {n * 17} \n{n} x  8 = {n * 8}   {n} x 18 = {n * 18} \n{n} x  9 = {n * 9}   {n} x 19 = {n * 19} ')
print('-' * 24)'''


n = int(input('Digite um número para ver sua tabuada: '))
print('\033[93m-' * 14)
print(f'\033[96m{n}\033[97m x  0 = \033[92m{n * 0} \n\033[96m{n}\033[97m x  1 = \033[92m{n * 1} \n\033[96m{n}\033[97m x  2 = \033[92m{n * 2} \n\033[96m{n}\033[97m x  3 = \033[92m{n * 3} \n\033[96m{n}\033[97m x  4 = \033[92m{n * 4} ')
print(f'\033[96m{n}\033[97m x  5 = \033[92m{n * 5} \n\033[96m{n}\033[97m x  6 = \033[92m{n * 6} \n\033[96m{n}\033[97m x  7 = \033[92m{n * 7} \n\033[96m{n}\033[97m x  8 = \033[92m{n * 8} \n\033[96m{n}\033[97m x  9 = \033[92m{n * 9} ')
print(f'\033[96m{n}\033[97m x 10 = \033[92m{n * 10}')
print('\033[93m-' * 14)
