'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.'''

#Resolução da questão
from time import sleep
print('\033[96m_.' * 20)
print('|\033[97m             Termos da PA             \033[96m|')
print('_.' * 20)
sleep(1)
prim_term = float(input('\033[97mPrimeiro termo da PA = '))
razao = float(input('Razão da PA: \033[95m'))
for x in range(0, 9):
    print(prim_term + razao * x, end = ', ')
print(prim_term + razao * 9)
