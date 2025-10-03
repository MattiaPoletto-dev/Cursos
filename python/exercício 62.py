'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.'''

print('\033[93m-=-' * 20)
print('|                      \033[97mTermos da PA                        \033[93m|')
print('-=-' * 20)

a1 = int(input('\033[97mPrimeiro termo: '))
r = int(input('Razão: '))
t = 0
while t < 10:
    t += 1
    if t == 1:
        print(f'\033[97mOs 10 primeiros termos são:\nPA(\033[96m{a1}', end = ', ')
    elif t > 1:
        a1 += r
        print(a1, end = ', 'if t < 10 else '\033[97m)')
n = 1
s = 0
while n != 0:
    n = int(input('\n\033[93mQuantos números a mais deseja adicionar? \033[96m'))
    s += n
    if n > 0:
        print('...', end = '')
        for x in range(1, n + 1):
            print(a1 + x * r, end = ' ,'if x != n else '\033[97m)')
        a1 += r * n
print(f'\033[97mA PA Obtida tem \033[96m{s + 10} \033[97mtermos')