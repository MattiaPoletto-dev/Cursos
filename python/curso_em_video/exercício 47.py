'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50'''

#Resolução da questão
from time import sleep
print('\033[97mLista de números pares de 1 a 50:\033[96m')
for c in range(2, 51, 2):
    print(c, end = ' ')
    sleep(0.3)
print('\n\033[97mEssa é a lista de todos os números pares de 1 a 50!!!')


#Melhoria minha!
'''print(('\033[97m-=-' * 20))
print('\033[97m|                    \033[96mAchador de Números                    \033[97m|')
print(('\033[97m-=-' * 20))

print('De qual número inteiro até qual deseja?')
a = int(input('De (Menor valor): '))
b = int(input('A (Maior valor): '))

x1 = a % 2

print('Quer os números pares ou ímpares?\n[ 1 ]Pares\n[ 2 ]Ímpares ')
c = int(input('Escolha: '))

if  x1 == 0 and c == 1:
    for cont1 in range(a, b + 1, 2):
        print(cont1)
    print(f'Esses são os números pares de {a} a {b}!!')
elif x1 == 1 and c == 1:
    for cont2 in range(a + 1, b + 1, 2):
        print(cont2)
    print(f'Esses são os números pares de {a} a {b}!!')
elif x1 == 0 and c == 2:
    for cont3 in range(a + 1, b + 1, 2):
        print(cont3)
    print(f'Esses são os números ímpares de {a} a {b}!!')
elif x1 == 1 and c == 2:
    for cont4 in range(a, b + 1, 2):
        print(cont4)
    print(f'Esses são os números ímpares de {a} a {b}!!')
else:
    print('Tentativa inválida. Tente novamente!')'''
