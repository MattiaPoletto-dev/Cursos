'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
     A)Quantas pessoas foram contratadas
     B)A média de idade do grupo
     C)Uma lista com todas as mulheres
     D)Uma lista com todas as pessoas com idade acima da média'''

#Minha resolução
d = dict()
l = list()
l2 = list()
l3 = list()
soma = 0
while True:
    d["nome"] = str(input('Nome: '))
    while True:
        d["sexo"] = str(input('Sexo [M/F]: ')).lower().strip()
        if d['sexo'] in ['m','f']:
            break
        print('ERRO! Responda apenas M ou F')
    d["idade"] = int(input('Idade: '))
    soma += d['idade']
    l.append(d.copy())
    d.clear()
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
        print('ERRO! Responda apenas S ou N')
    if o == 'n':
        break
    print('-' * 50)
print('-=-' * 20)
print(f'Ao total, foram contratadas {len(l)} pessoas')
media = soma / len(l)
print(f'Média de idade: {media:.2f} anos')
for i,v in enumerate(l):
    if l[i]['sexo'] == 'f':
        l2.append(l[i]['nome'])
print(f'Lista das mulheres: {l2}')
for i,v in enumerate(l):
    if l[i]['idade'] > media:
        l3.append(l[i]['nome'])
print(f'Pessoas com idade acima da média: {l3}')

#Resolução do vídeo
'''galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram', end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}', end = '')
print()
print('D) Lista das pessoas que estão em cima da média: ', end = '')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'   {k} = {v};', end = '')
        print()
print('<< ENCERRADO >>')'''
