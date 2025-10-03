'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo' '''

#ERRADO (Se colocar Santos, ele diz true também)
'''cidade = str(input('Digite o nome de uma cidade: ')).strip()
conv1 = cidade.split()[0]
conv2 = conv1.upper()
print('é','SANTO' in conv2 , 'que inicia com Santo a frase')'''


nome = str(input('\033[97mDirei se a cidade em que você nasceu começa com Santo, qual cidade você nasceu? \033[96m')).strip()
conv = nome.split()[0].upper()
print(conv == 'SANTO')
