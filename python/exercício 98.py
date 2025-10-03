'''Faça um programa ue tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
e realize as contagens. Sue programa tem que realizar três contagens através da função criada:
     A)de 1 até 10, de 1 em 1
     B)de 10 até 0, de 2 em 2
     C)Uma contagem personalizada.'''

#Minha resolução
from time import sleep

def contador(inicio,fim,passo):
    print('-=' * 20)
    if passo > 0:
        if inicio < fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(0.5)
            for c in range(inicio,fim + 1,passo):
                print(c,end = ' ')
                sleep(0.25)
            print('FIM!')
        elif inicio > fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(0.5)
            for d in range(inicio, fim - 1, passo * (-1)):
                print(d, end = ' ')
                sleep(0.25)
            print('FIM!')
        else:
            print(inicio, end = ' ')
            print('FIM!')
    elif passo < 0:
        passo = passo * (-1)
        if inicio < fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(0.5)
            for c in range(inicio,fim + 1,passo):
                print(c,end = ' ')
                sleep(0.25)
            print('FIM!')
        elif inicio > fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            sleep(0.5)
            for d in range(inicio, fim - 1, passo * (-1)):
                print(d, end = ' ')
                sleep(0.25)
            print('FIM!')
        else:
            print(inicio, end = ' ')
            print('FIM!')
    else:
        print('Com o passo igual a 0, ele não sairá do lugar :)')

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
while True:
    contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
    while True:
        o = str(input('Quer continuar[S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
    print('-=' * 20)
    if o == 'n':
        break
print('Volte sempre!!!')
