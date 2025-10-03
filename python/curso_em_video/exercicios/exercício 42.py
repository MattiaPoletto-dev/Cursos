'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
     - Equilátero: todos os lados iguais
     - Isósceles: dois lados iguais
     - Escaleno: todos os lados diferentes.
Obs: ex035 --> Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo.'''

# Minha resolução
l1 = float(input('\033[93mPrimeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print('\033[91mImpossível formar um triângulo com esses lados!')
else:
    if l1 != l2 != l3 !=l1: # Cai na bait!
        print('\033[97mFormará um triângulo e ele será \033[96mESCALENO\033[97m!')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('\033[97mFormará um triângulo e ele será \033[96mISÓSCELES\033[97m!')
    elif l1 == l2 == l3:
        print('\033[97mFormará um triângulo e ele será \033[96mEQUILÁTERO\033[97m!')
