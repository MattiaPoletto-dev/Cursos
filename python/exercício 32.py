'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

'''ano = int(input('Digite o ano que você quer analisar: '))
conv1 = ano % 4
if conv1 == 0:
    print(f'O ano {ano} é um ano bissexto :)')
else:
    print(f'O ano {ano} não é um ano bissexto :(')'''


from datetime import date
ano = int(input('\033[97mQue ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano1 = date.today().year
    conv1 = bool(ano % 100 == 0)
    if conv1 == True:
        conv2 = bool(ano1 % 400 == 0 and ano1 % 4 ==0)
        if conv2 == True:
            print(f'O ano {ano1} é \033[92mBISSEXTO')
        else:
            print(f'O ano {ano1} \033[91mNÃO é BISSEXTO')
    else:
        conv3 = bool(ano1 % 4 == 0)
        if conv3 == True:
            print(f'O ano {ano1} é \033[92mBISSEXTO')
        else:
            print(f'O ano {ano1} \033[91mNÃO é BISSEXTO')
else:
    conv1 = bool(ano % 100 == 0)
    if conv1 == True:
        conv2 = bool(ano % 400 == 0 and ano % 4 ==0)
        if conv2 == True:
            print(f'O ano {ano} é \033[92mBISSEXTO')
        else:
            print(f'O ano {ano} \033[91mNÃO é BISSEXTO')
    else:
        conv3 = bool(ano % 4 == 0)
        if conv3 == True:
            print(f'O ano {ano} é \033[92mBISSEXTO')
        else:
            print(f'O ano {ano} \033[91mNÃO é BISSEXTO')
