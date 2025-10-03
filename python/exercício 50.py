'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''

#Resolução da questão
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f'Você informou {contador} números pares e a soma foi {soma}')
