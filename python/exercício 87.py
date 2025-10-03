'''Aprimore o desafio anterior, mostrando no final:
     A)A soma de todos os valores pares digitados
     B)A soma dos valores da 3ª coluna
     C)O maior valor da 2ª linha.'''

#Minha resoluçãp
'''B,Am,M,Ac,Verm,Verd = '\033[97m','\033[93m','\033[95m','\033[96m','\033[91m','\033[92m'

l1 = [[],[],[]]
l2 = [[],[],[]]
l3 = [[],[],[]]
lista_alternativa = list()
for c in range(1,4):
    for x in range(1,4):
        n = int(input(f'{B}Digite o valor do termo {Ac}a{c}{x}{B}: '))
        lista_alternativa.append(n)
        if c == 1:
            l1[x - 1].append(n)
        elif c == 2:
            l2[x - 1].append(n)
        elif c == 3:
            l3[x - 1].append(n)

lista_alternativa.sort()

print(f'{M}-' * 40)
print(f'{B}O que deseja saber de sua matriz')
print(f'{Ac}[{l1[0][0]: ^5}] [{l1[1][0]: ^5}] [{l1[2][0]: ^5}]')
print(f'[{l2[0][0]: ^5}] [{l2[1][0]: ^5}] [{l2[2][0]: ^5}]')
print(f'[{l3[0][0]: ^5}] [{l3[1][0]: ^5}] [{l3[2][0]: ^5}]')
print(f'{B}[ 1 ]A soma de todos os valores digitados\n[ 2 ]A soma de todos os valores pares digitados'
          f'\n[ 3 ]A soma de todos os valores ímpares digitados'
           f'\n[ 4 ]A soma dos valores de alguma linha ou coluna\n[ 5 ]O maior e o menor valor da matriz'
          f'\n[ 6 ]Determinante da matriz\n[ 7 ]Fechar programa')
while True:
    print(f'{M}-' * 40)
    e = int(input(f'{Am}O que deseja saber de sua matriz? {B}'))
    if e == 1:
        s = l1[0][0] + l1[1][0] + l1[2][0] + l2[0][0] + l2[1][0] + l2[2][0] + l3[0][0] + l3[1][0] + l3[2][0]
        print(f'{B}A soma de todos os termos da matriz é:{Ac} {s}')
    elif e == 2:
        soma_par = 0
        for p1 in range(0,3):
            if l1[p1][0] % 2 == 0:
                soma_par += l1[p1][0]
        for p1 in range(0,3):
            if l2[p1][0] % 2 == 0:
                soma_par += l2[p1][0]
        for p1 in range(0,3):
            if l3[p1][0] % 2 == 0:
                soma_par += l3[p1][0]
        print(f'{B}A soma dos números pares de sua matriz é{Ac} {soma_par}')
    elif e == 3:
        soma_impar = 0
        for p1 in range(0,3):
            if l1[p1][0] % 2 == 1:
                soma_impar += l1[p1][0]
        for p1 in range(0,3):
            if l2[p1][0] % 2 == 1:
                soma_impar += l2[p1][0]
        for p1 in range(0,3):
            if l3[p1][0] % 2 == 1:
                soma_impar += l3[p1][0]
        print(f'{B}A soma dos números ímpares de sua matriz é{Ac} {soma_impar}')
    elif e == 4:
        print(f'{B}[ 1 ]Linha\n[ 2 ]Coluna')
        e1 = int(input(f'{Am}Escolha: '))
        if e1 == 1:
            e2 = int(input('1ª, 2ª ou 3ª linha? '))
            if e2 == 1:
                s = l1[0][0] + l1[1][0] + l1[2][0]
                print(f'{B}A soma da 1ª linha é{Ac} {s}')
            if e2 == 2:
                s = l2[0][0] + l2[1][0] + l2[2][0]
                print(f'{B}A soma da 2ª linha é{Ac} {s}')
            if e2 == 3:
                s = l3[0][0] + l3[1][0] + l3[2][0]
                print(f'{B}A soma da 3ª linha é{Ac} {s}')
        elif e1 == 2:
            e2 = int(input('1ª, 2ª ou 3ª coluna? '))
            if e2 == 1:
                s = l1[0][0] + l2[0][0] + l3[0][0]
                print(f'{B}A soma da 1ª coluna é{Ac} {s}')
            if e2 == 2:
                s = l1[1][0] + l2[1][0] + l3[1][0]
                print(f'{B}A soma da 2ª coluna é{Ac} {s}')
            if e2 == 3:
                s = l1[2][0] + l2[2][0] + l3[2][0]
                print(f'{B}A soma da 3ª coluna é{Ac} {s}')
    elif e == 5:
        print(f'{B}Maior valor da matriz:{Ac} {lista_alternativa[8]}'
              f'\n{B}Menor valor da matriz:{Ac} {lista_alternativa[0]}')
    elif e == 6:
        detp1 = l1[0][0] * l2[1][0] * l3[2][0] + l1[1][0] * l2[2][0] * l3[0][0] + l2[0][0] * l3[1][0] * l1[2][0]
        detp2 = l3[0][0] * l2[1][0] * l1[2][0] + l3[1][0] * l2[2][0] * l1[0][0] + l3[2][0] * l2[0][0] * l1[1][0]
        det = detp1 - detp2
        print(f'{B}O determinante da matriz é{Ac} {det}')
    elif e == 7:
        break
    else:
        print(f'{Verm}Opção inválida! Tente novamente')

print(f'{M}-' * 40)
print(f'{Verd}Programa finalizado com sucesso!!!')'''


#Resolução do vídeo
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a{l}{c}: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da 2ª linha é {mai}.')
