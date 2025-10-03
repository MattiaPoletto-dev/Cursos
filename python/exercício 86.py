'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final
mostre a matriz na tela, com a formatação correta.'''

#Minha resoluçãp
'''l1 = [[],[],[]]
l2 = [[],[],[]]
l3 = [[],[],[]]

for c in range(1,4):
    for x in range(1,4):
        n = int(input(f'Digite o valor do termo a{c}{x}: '))
        if c == 1:
            l1[x - 1].append(n)
        elif c == 2:
            l2[x - 1].append(n)
        elif c == 3:
            l3[x - 1].append(n)
print('-' * 40)
print('Sua matruz 3x3 é:')
print(f'[{l1[0][0]: ^5}] [{l1[1][0]: ^5}] [{l1[2][0]: ^5}]')
print(f'[{l2[0][0]: ^5}] [{l2[1][0]: ^5}] [{l2[2][0]: ^5}]')
print(f'[{l3[0][0]: ^5}] [{l3[1][0]: ^5}] [{l3[2][0]: ^5}]')'''

#Resolução do vídeo
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a{l}{c}: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
