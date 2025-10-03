'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.'''

print('\033[93m-=-' * 20)
print('|                \033[97m10 primeiros termos da PA                 \033[93m|')
print('-=-' * 20)
a1 = int(input('\033[96mPrimeiro termo da PA: '))
r = int(input('\033[96mRazão: '))
print(f'\033[97mOs 10 primeiro termos da PA são: \n\033[96mPA(\033[92m{a1}, ',end = '')
t = 0
while t < 9:
    t += 1
    a1 += r
    print(a1, end = ', 'if t < 9 else '\033[96m)')
