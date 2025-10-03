'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''

'''nome = str(input('Digite seu nome completo: ')).strip().upper()
conv = nome.split()
print('SILVA' in conv)'''


nome = str(input('\033[96mQual é seu nome completo? ')).strip().upper()
conv = nome.split()
n = 'SILVA' in conv
if n == True:
    print('\033[97mSeu nome tem Silva?\033[92m', 'SILVA' in conv)
else:
    print('\033[97mSeu nome tem Silva?\033[91m', 'SILVA' in conv)
