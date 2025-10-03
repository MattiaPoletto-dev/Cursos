'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
se encontram no intervalo de 1 a 500.'''

#Resolução da questão
'''soma = 0
cont = 0
for c in range(3,500, 6):
    soma += c
    cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')'''


#Melhoria minha!
print(('-=-' * 20))
print('|             Números ímpares divisíveis por 3             |')
print(('-=-' * 20))

print('Escolha o intervalo: ')
a = int(input('De (menor): '))
b = int(input('A (maior): '))

soma = 0
contador = 0
if a % 2 == 0:
    for c in range(a + 1, b + 1, 2):
        if c % 3 == 0:
            soma += c
            contador += 1
    print(f'A soma de todos os {contador} valor(es) ímpar(es), múltiplo(s) de 3, entre {a} e {b} é {soma}')
elif a % 2 == 1:
    for c in range (a, b + 1, 2):
        if c % 3 == 0:
            soma += c
            contador += 1
    print(f'A soma de todos os {contador} valor(es) ímpar(es), múltiplo(s) de 3, entre {a} e {b} é {soma}')
