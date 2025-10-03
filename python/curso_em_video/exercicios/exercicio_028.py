'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.'''

'''import random
numpes = int(input('Adivinhe o número de 0 a 5 que eu pensei: '))
numcom = random.randint(0, 5)
if numpes == numcom:
    print('Você acertou! Essse foi o número que escolhi!')
else:
    print(f'Você errou, o número que escolhi foi {numcom}, tente novamente!')'''


import random
import time
print('\033[33m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033')
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033')
numpes = int(input('Em que número eu pensei? '))
numcomp = random.randint(0,5)
print('\033[35mPROCESSANDO...')
time.sleep(1.5)
if numpes == numcomp:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {numcomp} e não no {numpes}!')
