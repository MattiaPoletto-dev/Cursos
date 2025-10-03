'''Crie um script Python que leia dois números e tente mostrar a soma e a diferença entre eles.'''

'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
d = n1 - n2
print('-' * 15)
print(f'Os números {n1} e {n2}:')
print(f'Soma      = {s} \nDiferença = {d}')
print('-' * 15)'''


n1 = int(input('\033[97mDigite um número: '))
n2 = int(input('\033[97mDigite outro número: '))
s = n1 + n2
d = n1 - n2
print(f'\033[97mA soma entre\033[92m {n1} \033[97me \033[91m{n2}\033[97m e \033[96m{s}\033[97m e a diferença'
      f' entre\033[92m {n1}\033[97m e \033[91m{n2} \033[97mé \033[96m{d}\033[97m!.')
