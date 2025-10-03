'''Faça um programa qque leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

'''n = int(input('Digite um número inteiro: '))
print(f'Seu sucessor é {n+1}')
print(f'Seu antecessor é {n-1}')'''


'''n = int(input('igite um número inteiro: '))
print('Seu sucessor é',n+1)
print('Seu antecessor é',n-1)'''


n = int(input('\033[97mDigite um número: '))
print(f'Analisando o valor \033[4:96m{n}\033[0:97m, seu sucessor é \033[92m{n+1} \033[97m'
      f'e seu antecessor é \033[91m{n-1}\033[97m.')
