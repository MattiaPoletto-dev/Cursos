'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''

#Minha resolução
def area(l,c):
    print(f'A área de um terreno {l} x {c} é {l * c:.2f} m²')
def traco():
    print('-' * 30)

while True:
    traco()
    print(f'{' Calule a área do terreno ':=^30}')
    traco()
    l = float(input('LARGURA (m): '),)
    c = float(input('COMPRIMENTO (m): '))
    area(l,c)
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
    if o == 'n':
        break
traco()
print('Volte sempre!!!')
