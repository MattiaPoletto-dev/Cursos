'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma sequência de Fibonacci.'''

#Não consegui fazer
print('\033[96m-' * 60)
print('|                  \033[97mSequência de Fibonacci                  \033[96m|')
print('-' * 60)

n = int(input('\033[93mQuantos termos quer que seja mostrado (n > 1)? '))
t1 = 0
t2 = 1
print(f'\033[97mSequência de Fibonacci:\n (\033[96m{t1}, {t2},', end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' {t3}', end = ','if cont < n else '\033[97m)')
    t1 = t2
    t2 = t3
    cont += 1
