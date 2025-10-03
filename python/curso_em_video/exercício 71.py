'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
   OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('\033[95m-=-' * 23)
print('|                   \033[97mCaixa eletrônico do Polettão                    \033[95m|')
print('-=-' * 23)

n = int(input('\033[97mValor a ser sacado (apenas n° inteiros): R$'))
cont1 = cont2 = cont3 = cont4 = 0
x = n
while True:
    if n >= 50:
        n -= 50
        cont1 += 1
    if 50 > n >= 20:
        n -= 20
        cont2 += 1
    if 20 > n >= 10:
        n -= 10
        cont3 += 1
    if 10 > n >= 1:
        n -= 1
        cont4 += 1
    if n == 0:
        break
print('-' * 40)
print(f'Para a quantia de \033[96mR${x}\033[97m, será retirado:\nNotas de 50: \033[96m{cont1}'
      f'\n\033[97mNotas de 20: \033[96m{cont2}\n\033[97mNotas de 10: \033[96m{cont3}'
      f'\n\033[97mNotas de 1 : \033[96m{cont4}')
