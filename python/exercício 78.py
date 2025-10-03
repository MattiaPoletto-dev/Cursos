'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''

#Resolução do vídeo
lista1 = []
mai = men = 0
for c in range(0, 5):
    lista1.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men =lista1[c]
    else:
        if lista1[c] > mai:
            mai = lista1[c]
        elif lista1[c] < men:
            men = lista1[c]

print('-=-' * 30)
print(f'Você digitou os valores {lista1}')
print(f'O maior valor digitado foi {mai} nas posições ', end = '')
for i, v in enumerate(lista1):
    if v == mai:
        print(f'{i}...', end = '')
print(f'\nO menor valor digitado foi {men} nas posições ', end  = '')
for i, v in enumerate(lista1):
    if v == men:
        print(f'{i}...', end = '')
