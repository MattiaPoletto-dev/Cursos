'''Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
     A)Quantas pessoas foram cadastradas
     B)Uma listagem com as pessoas mais pesadas
     C)Uma listagem com pessoas mais leves.'''

#Minha resulução
lista = list()
lista2 = list()
cont = nmai = nmen = pmai = pmen = 0

while True:
    print('-' * 10,'Cadastrar pessoa','-' * 10)
    n = str(input('Nome: ')).title()
    p = float(input('Peso: '))
    lista2.append(n)
    lista2.append(p)
    lista.append(lista2[:])
    lista2.clear()
    if cont == 0:
        nmai = nmen = n
        pmai = pmen = p
    else:
        if p > pmai:
            nmai = n
            pmai = p
        elif p < pmen:
            nmen = n
            pmen = p
    cont += 1
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
    if o == 'n':
        print('-' * 60)
        break

lista_maior = list()
lista_menor = list()

for i in range(0,len(lista)):
    if lista[i][1] == pmai:
        lista_maior.append(lista[i][0])
    if lista[i][1] == pmen:
        lista_menor.append(lista[i][0])
print(f'Sua lista cadastrada é: {lista}')
print('-' * 60)
print(f'N° de pessoas cadastradas: {cont}\nA(s) pessoa(s) mais pesada(s) pesam {pmai:.1f}kg e são: {lista_maior}'
      f'\nA(s) pessoa(s) mais leve(s) pesam {pmen:.1f}kg e são: {lista_menor}')
