'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
     - O primeiro valor é maior
     - O segundo valor é maior
     - Não existe valor maior, os dois são iguais.'''

# Minha Resolução
'''n1 = int(input('\033[93mDigite um primeiro número: '))
n2 = int(input('Digite um segundo número: '))
if n1 > n2:
    print(f'\033[97mO número \033[96m{n1} \033[97mé maior que o \033[96m{n2}\033[97m!')
elif n1 == n2:
    print('\033[97mNão há número maior, os dois números são iguais!')
else:
    print(f'\033[97mO número \033[96m{n2} \033[97mé maior que \033[96m{n1}\033[97m!')'''

# Resolução do caba
n1 = int(input('\033[93mPrimeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('\033[97mO PRIMEIRO valor é \033[96mmaior')
elif n1 == n2:
    print('\033[97mOs dois valores são \033[96mIGUAIS')
else:
    print('\033[97mO SEGUNDO valor é \033[96mmaior')
