'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
um laço for.'''

#Resolução da questão
print(('-=-' * 11 +'-='))
print('|             tabuada             |')
print(('-=-' * 11 + '-='))
a = int(input('Digite um número: '))
for c in range(0, 11):
    if c < 10:
        print(f'{a} x {c}  =', a * c)
    else:
        print(f'{a} x {c} =', a * c)
