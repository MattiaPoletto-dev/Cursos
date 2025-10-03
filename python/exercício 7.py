'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média aritmética.'''

'''a = input('Nome do aluno: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
ma = (n1 + n2) / 2
print(f'Aluno: {a} \nNota 1: {n1} \nNota 2: {n2} \nMédia aritmética entre as notas é igual a {ma:.2f}')'''


'''n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
ma = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {ma:.1f}')'''


n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
ma = (n1 + n2) / 2
if ma < 5.5:
    print(f'\033[97mA média entre {n1} e {n2} é igual a \033[91m{ma:.1f}\033[97m. \033[91m\nVocê reprovou\033[97m.')
if ma >= 5.5 and ma < 6:
    print(f'\033[97mA média entre {n1} e {n2} é igual a \033[93m{ma:.1f}\033[97m. \033[93m\nPassou arrastado\033[97m.')
if ma >= 6:
    print(f'\033[97mA média entre {n1} e {n2} é igual a \033[92m{ma:.1f}\033[97m.\033[92m\nVocê passou\033[97m!!!')
