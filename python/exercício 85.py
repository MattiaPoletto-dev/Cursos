'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''


#Minha resoluçãp
lista = [[],[]]
print('Digite 7 números inteiros')
for c in range(1,8):
    n = int(input(f'Digite o {c}° número:'))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print('-=-' * 20)
print(f'Lista dos números pares: {lista[0]}')
print(f'Lista dos números ímpares: {lista[1]}')
