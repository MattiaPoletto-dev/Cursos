'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

#Minha resolução
B,Am,M,Ac,Verm,Verd = '\033[97m','\033[93m','\033[95m','\033[96m','\033[91m','\033[92m'
from random import randint
from time import sleep
ltemp = list()
lorig = list()

print(f'{M}-=-' * 20)
print(f'|                  {B}Jogos da MEGA SENA                      {M}|')
print('-=-' * 20)

n = int(input(f'{B}Quantos jogos você quer que sejam gerados? '))
for c in range(0,n):
    while len(ltemp) < 6:
        x = randint(1,60)
        if x not in ltemp:
            ltemp.append(x)
    ltemp.sort()
    lorig.append(ltemp[:])
    ltemp.clear()

print(f'{B}-=-=-=-=-=  SORTEANDO {Ac}{n} {B}JOGOS =-=-=-=-=-')
sleep(1.5)
for i,v in enumerate(lorig):
    print(f'{B}Jogo {i + 1}: {v}')
    sleep(1)
print(f'{B}-=-=-=-=-=-=  {Verd}< BOA SORTE! >  {B}=-=-=-=-=-=-')
