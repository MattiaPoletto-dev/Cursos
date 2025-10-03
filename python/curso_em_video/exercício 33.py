'''Faça um peograma que leia três números e mostre qual é o maior e qual é o menor.'''

'''n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'Maior: {n1}\nMenor: {n3}')
        else:
            print(f'Maior: {n1}\nMenor: {n2}')
if n2 > n1:
    if n2 > n3:
        if n1 > n3:
            print(f'Maior: {n2}\nMenor: {n3}')
        else:
            print(f'Maior: {n2}\nMenor: {n1}')
if n3 > n1:
    if n3 > n2:
        if n1 > n2:
            print(f'Maior: {n3}\nMenor: {n2}')
        else:
            print(f'Maior: {n3}\nMenor: {n1}')
if n1 < n2 == n3:
    print(f'Maior: {n2}\nMenor: {n1}')
if n2 < n1 == n3:
    print(f'Maior: {n1}\nMenor: {n2}')
if n3 < n1 == n2:
    print(f'Maior: {n1}\nMenor: {n3}')
if n1 == n2 == n3:
    print(f'Maior: {n1}\nMenor: {n1}')'''


a = int(input('\033[93mPrimeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and  b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'\033[97mO menor valor digitado foi: \033[96m{menor}\n\033[97mO maior valor digitado foi: \033[96m{maior}')
