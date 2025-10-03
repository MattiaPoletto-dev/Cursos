'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

'''n = float(input('Digite um número real:'))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f'O dobro de {n} é {d}, o triplo é {t} e a raiz quadrada é {rq:.3f}.')'''


'''n = int(input('Digite um número: '))
d = 2 * n
t = 3 * n
rq = n ** (1/2)
print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}.')
print(f'A raiz quadrada de {n} é igual a {rq:.2f}.')'''


n = int(input('\033[97mDigite um número: '))
d = 2 * n
t = 3 * n
rq = n ** (1/2) #pow(n,(1/2))
print(f'O dobro de \033[36m{n}\033[97m vale \033[94m{d}\033[97m.\nO triplo de \033[36m{n}\033[97m vale \033[94m{t}\033[97m.'
      f'\nA raiz quadrada de \033[36m{n}\033[97m é igual a \033[94m{rq:.2f}\033[97m.')
