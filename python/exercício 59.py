'''Crie um programa que leia dois valores e mostre em menu na tela:
     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] saber qual é o maior
     [ 4 ] trocar os números
     [ 5 ] sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
print('\033[96mDigite números inteiros')
n1 = int(input('\033[97mPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 2.5
while opc != 5:
    print('\033[96m-=-\033[97m' * 14)
    print('O que deseja fazer:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Descobrir qual é o maior'
          '\n[ 4 ] Trocar os números\n[ 5 ] Sair do programa')
    opc = int(input('\033[93mEscolha: \033[97m'))
    if opc == 1:
        print(f'Soma: \033[96m{n1} + {n2} = {n1 + n2}')
        sleep(2)
    elif opc == 2:
        print(f'Multiplicação: \033[96m{n1} x {n2} = {n1 * n2}')
        sleep(2)
    elif opc == 3:
        if n1 > n2:
            print(f'O primeiro número é maior: \033[96m{n1} > {n2}')
            sleep(2)
        elif n1 == n2:
            print(f'Os dois números são iguais: \033[96m{n1} = {n2}')
            sleep(2)
        elif n1 < n2:
            print(f'O segundo número é maior: \033[96m{n1} < {n2}')
            sleep(2)
    elif opc == 4:
        print('Por quais números deseja substituir seus primeiros números?')
        n1 = int(input('\033[93mPrimeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print(f'\033[93mOs novos números agora são: \033[96m{n1} \033[97me \033[96m{n2}\n\033[97mO que deseja fazer com eles?')
    elif opc > 5 or opc < 1:
        print('\033[91mOpção inválida! Tente novamente.')
        sleep(2)
print('\033[97mFinalizando...')
sleep(2)
print('\033[92mFim do programa! Volte sempre!')
