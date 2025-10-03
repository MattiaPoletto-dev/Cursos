'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).'''

cont = s = 0
while True:
    n = int(input('\033[93mDigite um número inteiro [para parar digite 999]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'\033[97mEntre os números digitados, tem-se:\nNúmeros digitados: '
      f'\033[96m{cont}\n\033[97mSoma entre eles: \033[96m{s}')
