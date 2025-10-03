'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No
final, mostre em um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.'''

#Minha resolução top top
B,Am,M,Ac,Verm,Verd = '\033[97m','\033[93m','\033[95m','\033[96m','\033[91m','\033[92m'

print(f'{M}-' * 50)
print(f'|               {B}Criação de boletim               {M}|')
print('-' * 50)

lista1 = list()
lista2 = list()
print(f'{Verm}Observação: certifique-se de escrever os nomes corretamente.')
while True:
    n = str(input(f'{B}Nome:')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista1.append([n, n1, n2])
    lista2.append([n,(n1 + n2) / 2])
    while True:
        o = str(input('Quer continuar[S/N]: ')).lower().strip()
        if o in ['s','n']:
            break
    if o == 'n':
        break
    print(f'{M}-' * 40)
print(f'{Ac}-' * 81)
print(f'|                      {B}Nome do Aluno                      {Ac}|        {B}Média        {Ac}|')
print('-' * 81)
for i,v in enumerate(lista2):
    if lista2[i][1] < 6:
        print(f'{Ac}| {B}{v[0]:.<56}{Ac}-{Verm}{v[1]: ^21}{Ac}|')
    else:
        print(f'{Ac}| {B}{v[0]:.<56}{Ac}-{Verd}{v[1]: ^21}{Ac}|')
print('-' * 81)

while True:
    while True:
        x = str(input(f'{B}Deseja ver a nota de algum aluno separadamente [S/N]? ')).lower().strip()
        if x in ['s', 'n']:
            break
    if x == 'n':
        break
    y = str(input(f'{B}De qual aluno deseja ver? ')).title()
    for c in range(0,len(lista1)):
        if y == lista1[c][0]:
            print(f'As notas de {Ac}{lista1[c][0]} {B}foram: {Ac}{lista1[c][1]} {B}e {Ac}{lista1[c][2]}')
    print(f'{M}-' * 60)

print(f'{M}-' * 60)
print(f'{Verd}Programa finalizado com sucesso!!!')
