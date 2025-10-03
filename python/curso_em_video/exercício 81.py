'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
     A)Quantos números foram digitados
     B)A lista de valores, ordenada de forma decrescente
     C)Se o valor 5 foi digitado e está ou não na lista.'''

#Minha resolução
B = '\033[97m'
Verm = '\033[91m'
Verd = '\033[92m'
Ac = '\033[96m'
Ae = '\033[94m'
Am = '\033[93m'
M = '\033[95m'

print(f'{M}-=-' * 23)
print(f'|                         {B}Escreva sua lista                         {M}|')
print(f'-=-' * 23)

lista = list()
cont = 0
while True:
    n = int(input(f'{B}Digite um número: '))
    lista.append(n)
    print(f'Lista atualizada: {Ac}{lista}{B}')
    cont += 1
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
    if o == 'n':
        break
print(f'Sua lista ficou sendo {Ac}{lista}{B}, o que deseja dela?')
copia_lista1 = lista.copy()
while True:
    print('[ 1 ]Quantos números foram digitados\n[ 2 ]Lista ordenada de forma crescente'
          '\n[ 3 ]Lista ordenada de forma decrescente\n[ 4 ]Colocar a lista na ordem padrão'
          '\n[ 5 ]Se algum valor está na lista\n[ 6 ]Sair do programa')
    x = int(input(f'{Am}Escolha: {B}'))
    print('-' * 60)
    if x == 1:
        if cont == 1:
            print(f'{B}Sua lista tem apenas {Ac}1 {B}número')
        else:
            print(f'{B}Sua lista tem exatamente{Ac} {cont} {B}números')
    elif x == 2:
        copia_lista1.sort()
        print(f'{B}Sua lista na ordem crescende é:\n{Ac} {copia_lista1}{B}')
    elif x == 3:
        copia_lista1.sort(reverse = True)
        print(f'{B}Sua lista na ordem decrescente é:\n {Ac}{copia_lista1}{B}')
    elif x == 4:
        print(f'{B}Sua lista na ordem padrão é:\n {Ac}{lista}{B}')
    elif x == 5:
        v = int(input(f'{B}Qual valor deseja saber? '))
        if v in lista:
            print(f'{B}O valor {v} {Verd}está {B}na lista!')
        else:
            print(f'{B}O valor{Ac} {v} {Verm}não está {B}na lista.')
    elif x == 6:
        break
    else:
        print(f'{Verm}Este comando é inválido! {B}Tente novamente.')
    print('-' * 60)
print(f'{Verd}O programa foi finalizado com sucesso. Até a próxima!!!')
