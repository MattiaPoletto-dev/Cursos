'''Crie uma plataforma que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag(999))'''

#Resolução minha
'''print('\033[96m-' * 60)
print('|                 \033[97mSoma de Números Inteiros                 \033[96m|')
print('-' * 60)

n = 0
s = -999
cont = -1
while n != 999:
    n = int(input('\033[93mDigite números inteiros [999 para parar]:'))
    s += n
    cont += 1
print(f'\033[97m(desconsiderando o 999)\nNúmeros digitados: \033[96m{cont}\n\033[97mSoma dos números: \033[96m{s}')'''

#Resolução do vídeo
n = cont = s = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:
    s += n
    cont += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {s}')
