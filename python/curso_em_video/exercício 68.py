'''Faça um prograama que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('\033[91m-=-' * 20)
print('|                       \033[97mPar ou Ímpar                       \033[91m|')
print('-=-' * 20)
cont = 0
while True:
    x = randint(0, 10)
    e = str(input('\033[93mPar ou Ímpar [P/I]: ')).strip().lower()
    if e == '':
        while e == '':
            e = str(input('\033[93mPar ou Ímpar [P/I]: ')).strip().lower()
    if e not in 'pi':
        while e not in 'pi':
            e = str(input('\033[93mPar ou Ímpar [P/I]: ')).strip().lower()
    n = int(input('Digite um número [0 a 10]: '))
    if n < 0 or n > 10:
        while n < 0 or n > 10:
            n = int(input('Digite um número [0 a 10]: '))
    if e == 'p' and (n + x) % 2 == 1 or e == 'i' and (n + x) % 2 == 0:
        break
    cont += 1
    if e == 'p':
        print(f'\033[97mEu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é par, \033[92mVocê ganhou!!'
            f'\n\033[97mVamos denovo')
    else:
        print(
            f'\033[97mEu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é ímpar, \033[92mVocê ganhou!!'
            f'\n\033[97mVamos denovo')
if e == 'p':
    if cont == 0:
        print(f'\033[97mEu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é ímpar\nInfelizmente você não ganhou nenhuma partida!')
    elif cont > 1:
        print(f'\033[97mDesta vez eu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é ímparm, \033[91meu ganhei!'
              f'\n\033[97mVocê conseguiu ganhar \033[96m{cont} \033[97mpartidas consecutivas, parabénss!!!')
    else:
        print(f'\033[97mDesta vez eu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é ímpar, \033[91meu ganhei!'
              f'\n\033[97mVocê conseguiu ganhar \033[96m1 \033[97mpartida, parabénss!!!')
else:
    if cont == 0:
        print(f'\033[97mEu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é par\nInfelizmente você não ganhou nenhuma partida!')
    elif cont > 1:
        print(f'\033[97mDesta vez eu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é par, \033[91meu ganhei!'
              f'\n\033[97mVocê conseguiu ganhar \033[96m{cont} \033[97mpartidas consecutivas, parabénss!!!')
    else:
        print(f'\033[97mDesta vez eu escolhi \033[95m{x} \033[97me \033[96m{x} + {n} = {x + n} \033[97mque é par, \033[91meu ganhei!'
              f'\n\033[97mVocê conseguiu ganhar \033[96m1 \033[97mpartida, parabénss!!!')
