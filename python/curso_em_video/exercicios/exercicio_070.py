'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:
     A)Qual é o total gasto na compra
     B)Quantos produtos custam mais de R$1000
     C)Qual é o nome do produto mais barato.'''

s = cont1 = cont2 = 0
print('\033[95m-=-' * 23)
print('|                          \033[97mLojas Tabaratin                          \033[95m|')
print('-=-' * 23)
while True:
    cont1 += 1
    if cont1 == 1:
        print('\033[97m-' * 30)
        nome = str(input('\033[97mNome do produto: '))
        preco = float(input('Preço: R$'))
        baratopreco = preco
        nomebarato = nome
    else:
        print('\033[97m-' * 30)
        nome = str(input('\033[97mNome do produto: '))
        preco = float(input('Preço: R$'))
        if preco < baratopreco:
            baratopreco = preco
            nomebarato = nome
    s += preco
    if preco > 1000:
        cont2 += 1
    c = str(input('\033[97mQuer continuar [S/N]? ')).strip().lower()[0]
    while c not in 'sn':
        c = str(input('\033[93mQuer continuar [S/N]? ')).strip().lower()[0]
    if c in 'n':
        break
print('\033[95m-' * 25,' \033[97mFIM DO PROGRAMA ', '\033[95m-' * 25)
print(f'\033[97mSegundo os {cont1} produtos registrados, tem-se:\nTotal gasto                        : \033[96mR${s:.2f}\n'
      f'\033[97mProdutos que custam mais de R$1000 : \033[96m{cont2}'
      f'\n\033[97mNome do produto mais barato        : \033[96m{nomebarato}\033[97m,\033[96m R${baratopreco}')
