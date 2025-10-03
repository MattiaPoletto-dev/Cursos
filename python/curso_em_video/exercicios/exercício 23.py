'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados'''

n = float(input('\033[93mDigite um número de 0 a 9999: '))
a4 = int(n / 1000)
a3 = int(int(n / 100) - (a4 * 10))
a2 = int(int(n / 10) - (a4 * 100 + a3 * 10))
a1 = int(n - (a4 * 1000 + a3 * 100 + a2 * 10))
print(f'\033[97munidade: \033[96m{a1}')
print(f'\033[97mdezena : \033[96m{a2}')
print(f'\033[97mcentena: \033[96m{a3}')
print(f'\033[97mmilhar : \033[96m{a4}')
