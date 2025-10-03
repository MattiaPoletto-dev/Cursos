'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.'''

#Minha resolução
lista = list()

while True:
    v = int(input('Digite um número: '))
    if v in lista:
        print('Não é possível adicionar valores duplicados!')
    else:
        lista.append(v)
        print('Valor adicionado com sucesso!!!')
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in 'sn' and o != '' and o != 'sn':
            break
    if o == 'n':
        break
    print(f'Lista até o momento: {lista}')
lista.sort()
print(f'Voce digitou os números: {lista}')
