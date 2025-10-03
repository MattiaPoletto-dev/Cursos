'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
     A)Quantas vezes apareceu o número 9
     B)Em que posição foi digitado o primeiro valor 3
     C)Quais foram os números pares.'''

#Minha resolução
Am = '\033[93m'
B = '\033[97m'
Ac = '\033[96m'
Verde = '\033[92m'
M = '\033[95m'

n1 = int(input(f'{Am}Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
cont = 1
tupla = (n1,n2,n3,n4)
print(f'{M}-' * 40)
print(f'{B}Números digitados: {Ac}{tupla}')
print(f'{M}-' * 40)
while True:
    if cont >= 2:
        print(f'{M}-' * 40)
    cont += 1
    print(f'{B}Opções:\n[ 1 ]Quantas vezes apareceu um determinado número\n[ 2 ]Em que posição foi digitado algum'
          ' determinado número\n[ 3 ]Quais foram os números pares\n[ 4 ]Sair do programa')
    e = int(input(f'{Am}Escolha: '))
    if e == 1:
        x = int(input('Qual número deseja saber? '))
        print(f'{B}O número{Ac} {x} {B}apareceu{Ac} {tupla.count(x)} {B}vezes.')
    elif e == 2:
        x = int(input('Qual número deseja saber? '))
        if x not in tupla:
            print(f'{B}O número{Ac} {x} {B}não foi escrito nenhuma vez.')
        else:
            print(f'{B}A primeiro número{Ac} {x} {B}está na{Ac} {tupla.index(x) + 1}ª {B}posição')
    elif e == 3:
        if n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 1 and n4 % 2 == 1:
            print(f'{B}Não há números pares.')
        else:
            print(f'{B}O(s) número(s) par(es) é(são):{Ac}', end = ' ')
            for c in tupla:
                if c % 2 == 0:
                    print(c, end = ' ')
        print('')
    elif e == 4:
        break
print(f'{M}-' * 40)
print(f'{Verde}Programa finalizado. Tenha um ótimo dia!!!')
