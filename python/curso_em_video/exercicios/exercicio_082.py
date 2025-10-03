'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados. Ao final, mostre o conteúdo das três listas
geradas.'''

#Minha resolução
lista = list()
lista_par = list()
lista_impar = list()

while True:
    n = int(input('Digite um número para sua lista: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    if n % 2 == 1:
        lista_impar.append(n)
    while True:
        p = str(input('Quer continuar [S/N]? ')).lower().strip()
        if p in ['s','n']:
            break
    if p == 'n':
        break
    print('-' * 40)

copia_lista = lista.copy()
copia_lista_par = lista_par.copy()
copia_lista_impar = lista_impar.copy()

while True:
    print('-' * 40)
    print('Qual lista deseja ver?\n[ 1 ]Lista padrão\n[ 2 ]Lista dos números pares'
          '\n[ 3 ]Lista dos números ímpares\n[ 4 ]Fechar programa')
    e = int(input('Escolha: '))
    print('-' * 40)
    if e == 1:
        print('[ 1 ]Na ordem de digitação dos números\n[ 2 ]Ordem crescente'
              '\n[ 3 ]Ordem decrescente')
        x = int(input('Escolha: '))
        if x == 1:
            print(f'Sua lista é:\n {lista}')
        elif x == 2:
            copia_lista.sort()
            print(f'Sua lista na ordem crescente é:\n {copia_lista}')
        elif x == 3:
            copia_lista.sort(reverse = True)
            print(f'Sua lista na ordem decrescente é:\n {copia_lista}')
        else:
            print('Opção inválida!')
    elif e == 2:
        print('[ 1 ]Na ordem de digitação dos números\n[ 2 ]Ordem crescente\n[ 3 ]Ordem decrescente')
        y = int(input('Escolha: '))
        if y == 1:
            print(f'Sua lista dos números pares é:\n {lista_par}')
        elif y == 2:
            copia_lista_par.sort()
            print(f'Sua lista dos números pares em ordem crescente é:\n {copia_lista_par}')
        elif y == 3:
            copia_lista_par.sort(reverse = True)
            print(f'Sua lista dos números pares em ordem decrescente é:\n {copia_lista_par}')
        else:
            print('Opção inválida!')
    elif e == 3:
        print('[ 1 ]Na ordem de digitação dos números\n[ 2 ]Ordem crescente\n[ 3 ]Ordem decrescente')
        z = int(input('Escolha: '))
        if z == 1:
            print(f'Sua lista dos números ímpares é:\n {lista_impar}')
        elif z == 2:
            copia_lista_impar.sort()
            print(f'Sua lista dos números ímpares em ordem crescente é:\n {copia_lista_impar}')
        elif z == 3:
            copia_lista_impar.sort(reverse = True)
            print(f'Sua lista dos números ímpares em ordem decrescente é:\n {copia_lista_impar}')
        else:
            print('Opção inválida!')

    elif e == 4:
        break
    else:
        print('Opção inválida!')

print('programa finalizado com sucesso!!!')
