'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

#Resolução minha
'''n = int(input('De qual número deseja saber o fatorial? '))
x = 1
fat = 1
while x != (n + 1):
    fat *= x
    x += 1
print(f'Calculando: {n}! = ', end = '')
for c in range(n, 1, -1):
    print(c, end = ' x ')
print('1 =', fat)'''

#Resolução minha 2.0
'''from math import factorial
n = int(input('De qual número deseja saber o fatorial: '))
f = factorial(n)
print(f'Calculando: {n}! = {f}')'''

#Resolução do vídeo
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(c, end = '')
    print(' x 'if c > 1 else ' = ', end = '')
    f*= c
    c -= 1
print(f)
