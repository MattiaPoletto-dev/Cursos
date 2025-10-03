'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

#Minha resolução
from random import randint
B = '\033[97m'
M = '\033[95m'
Ac = '\033[96m'
Verde = '\033[92m'
print(f'{M}-=-' * 23)
print(f'|                   {B}Gerador de números aleatórios                   {M}|')
print(f'-=-' * 23)

print(f'{B}De quanto até quanto deseja? ')
x = int(input('De: '))
y = int(input('A: '))

a = randint(x, y)
b = randint(x, y)
c = randint(x, y)
d = randint(x, y)
e = randint(x, y)
tupla = (a,b,c,d,e)
print(f'{B}Os 5 números gerados foram: {Ac}', ', '.join(map(str, tupla)))
while True:
    print(f'{M}-' * 30)
    print(f'{B}Opções:\n[ 1 ]Maior valor\n[ 2 ]Menor valor\n[ 3 ]Sair do programa')
    z = int(input('Escolha: '))
    conv1 = sorted(tupla)
    if z == 1:
        print(f'O maior valor é {Ac}{conv1[-1]}')
    elif z == 2:
        print(f'O menor valor é {Ac}{conv1[0]}')
    elif z == 3:
        break
print(f'{M}-' * 30)
print(f'{Verde}Programa finalizado. Tenha um ótimo dia!!')
