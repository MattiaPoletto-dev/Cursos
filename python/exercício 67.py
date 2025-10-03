'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo.'''

print('\033[93m-=-' * 20)
print('|                         \033[97mTabuada                          \033[93m|')
print('-=-' * 20)
while True:
    n = int(input('\033[97mDigite um número: '))
    print('\033[96m----------------------')
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[97m{n} x {c} = {n * c}')
    print('\033[96m----------------------')
print('\033[97mPrograma finalizado com sucesso!!')
