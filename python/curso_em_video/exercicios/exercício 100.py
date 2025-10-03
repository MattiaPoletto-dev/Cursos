'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A
primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.'''

#Minha resolução
from random import randint
from time import sleep

def sorteio(x):
    for c in range(1,6):
        x.append(randint(0,10))
    print('Sorteando números... ', end = '')
    sleep(0.5)
    for i,v in enumerate(x):
        print(v, end = ', 'if i < len(x) - 1 else '')
        sleep(0.75)
def somaPar(y):
    soma = 0
    for i,v in enumerate(y):
        if v % 2 == 0:
            soma += v
    print(f'\nSomando os valores pares temos {soma}')


     #Programa principal
start = str(input('Pressione enter para começar:'))
numeros = list()
sorteio(numeros)
somaPar(numeros)
