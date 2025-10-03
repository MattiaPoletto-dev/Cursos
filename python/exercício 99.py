'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

#Minha resolução
def maior(x):
    print('-' * 30)
    print('Sua lista ficou: (', end = '')
    x.sort(reverse=True)
    for y,z in enumerate(x):
        print(z, end = ', ' if y < len(x) - 1 else ')\n')
    print(f'O maior valor da lista é: {x[0]}')


     #programa principal
while True:
    lista = list()
    while True:
        lista.append(int(input('Digite um valor inteiro: ')))
        while True:
            o = str(input('Quer continuar [S/N]? ')).lower().strip()
            if o in ['s','n']:
                break
        if o == 'n':
            break
    maior(lista)
    print('-' * 30)
    while True:
        o = str(input('Quer fazer outra lista [S/N]? ')).lower().strip()
        if o in ['s', 'n']:
            break
    if o == 'n':
        break
print('-' * 30)
print('Programa finalizado. Volte sempre!!!')
