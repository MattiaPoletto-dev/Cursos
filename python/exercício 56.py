'''Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
     - a média de idade do grupo
     - qual é o nome do homem mais velho
     - quantas mulheres têm idade menor que 21 anos.'''

soma = 0
maisvelho = 'Não há homens'
idademaisvelho = 0
tot1 = 0
for c in range(1, 5):
    print('-------- DADOS --------')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if sexo in 'Mm':
        if c == 1:
            maisvelho = nome
            idademaisvelho = idade
        elif c > 1:
            if idade > idademaisvelho:
                maisvelho = nome
                idademaisvelho = idade
    if sexo in 'Ff':
        if idade < 21:
            tot1 += 1

print(f'Média das idades: {soma / 4}')
print(f'Nome do homem mais velho: {maisvelho}')
print(f'Total de mulheres com menos de 21 anos: {tot1}')
