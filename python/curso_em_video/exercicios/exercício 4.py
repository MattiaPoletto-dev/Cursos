'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
as informaçoes possíveis sobre ele.'''

n = input('\033[97mDigite algo: ')
print('\033[97mO tipo primitivo desse valor é: \033[92m', type(n))
a1 = bool(n.isspace())
a2 = bool(n.isnumeric())
a3 = bool(n.isalpha())
a4 = bool(n.isalnum())
a5 = bool(n.isupper())
a6 = bool(n.islower())
a7 = bool(n.istitle())

if a1 == True:
    print('\033[96mSó tem espaços?\033[92m', n.isspace())
else:
    print('\033[96mSó tem espaços?\033[91m', n.isspace())
if a2 == True:
    print('\033[96mÉ um número?\033[92m', n.isnumeric())
else:
    print('\033[96mÉ um número?\033[91m', n.isnumeric())
if a3 == True:
    print('\033[96mÉ alfabético?\033[92m', n.isalpha())
else:
    print('\033[96mÉ alfabético?\033[91m', n.isalpha())
if a4 == True:
    print('\033[96mÉ alfanumérico\033[92m?', n.isalnum())
else:
    print('\033[96mÉ alfanumérico\033[91m?', n.isalnum())
if a5 == True:
    print('\033[96mEstá em maiúsculas?\033[92m', n.isupper())
else:
    print('\033[96mEstá em maiúsculas?\033[91m', n.isupper())
if a6 == True:
    print('\033[96mEstá em minúsculas?\033[92m', n.islower())
else:
    print('\033[96mEstá em minúsculas?\033[91m', n.islower())
if a7 == True:
    print('\033[96mEstá capitalizada?\033[92m', n.istitle())
else:
    print('\033[96mEstá capitalizada?\033[91m', n.istitle())
