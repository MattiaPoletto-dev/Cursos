'''Faça um programa que leia uma frase pelo teclado e mostre:
     1) quantas vezes aparece a letra "a"
     2) em que posição ela aparece a primeira vez
     3) e em que posição ela aparece a última vez'''

# não consegui
'''frase = str(input('Digite uma frase: ')).strip().lower()
conv1 = frase.count('a')
conv2 = frase.find('a')
print('A letra "a" aparece', conv1,'vezes')
print(f'A posição, começando do 1, em que a primeira letra "a" aparece é: {conv2 + 1}')'''


frase = str(input(('\033[93mDigite uma frase: '))).strip().lower()
print(f'\033[97mA letra \033[92m"a"\033[97m aparece \033[92m{frase.count('a')} vezes \033[97mna frase.')
print(f'A primeira letra \033[92m"a"\033[97m apareceu \033[92mna posição {frase.find('a') + 1}\033[97m.')
print(f'\033A última letra \033[92m"a"\033[97m apareceu na \033[92mposição {frase.rfind('a') + 1}\033[97m.')
