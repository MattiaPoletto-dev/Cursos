'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.'''

'''n = float(input('Digite um número real: '))
#print(f'A parte inteira de {n} é {n:.0f}')'''


'''from math import floor
#num = float(input('Digite um número real: '))
#a = floor(num)
#print(f'A parte inteira de {num} é {a}!')'''


from math import floor  #pode ser trunc também
num = float(input('\033[97mDigite um valor: '))
a = floor(num)
print(f'O valor digitado foi \033[92m{num}\033[97m e a sua porção inteira é \033[96m{a}')
