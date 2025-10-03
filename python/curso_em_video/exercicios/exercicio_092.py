'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuição).'''

#Minha resolução
'''from datetime import date

d = dict()
l1 = list()
l2 = list()
while True:
    n = str(input('Nome: ')).strip()
    ano = int(input('Ano de nascimento: '))
    ncart = int(input('Carteira de trabalho [se não tiver digite 0]: '))
    idade = date.today().year - ano
    if ncart == 0:
        d['Nome'],d['Idade'],d['CTPS'] = n, idade, ncart
        l1.append(d.copy())
        d.clear()
    elif ncart > 0:
        ano_contrat = int(input('Ano de contratação: '))
        aposentadoria = ano_contrat - ano + 35
        sal = float(input('Salário: R$'))
        d['Nome'], d['Idade'], d['CTPS'], d['Ano de contratação'], d['Salário'],d['Aposentadoria'] =n, idade, ncart, ano_contrat, sal, aposentadoria
        l2.append(d.copy())
        d.clear()
    else:
        print('Número da carteira de trabalho inválido! Tente novamente.')
    while True:
        o = str(input('Deseja continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
    if o == 'n':
        break
    print('-=-' * 30)

print('-=-' * 30)
print('     === LISTA DAS PESSOAS SEM CTPS ===     ')
for c in range(0,len(l1)):
    print(f'{c + 1}. {l1[c]['Nome']}')
print('     === LISTA DAS PESSOAS COM CTPS ===     ')
for x in range(0,len(l2)):
    print(f'{x + 1}. {l2[x]['Nome']}')
print('-=-' * 30)

while True:
    nome = str(input('Digite o nome da pessoas que você quer ver os dados [0 para fechar programa]: '))
    if nome == '0':
        break
    else:
        for i,v in enumerate(l1):
            if v['Nome'] == nome:
                for y,z in v.items():
                    print(f'{y}: {z}')
        for i,v in enumerate(l2):
            if v['Nome'] == nome:
                for y,z in v.items():
                    print(f'{y}: {z}')
print('-=-' * 30)
print('Programa finalizado com sucesso!!!')'''

#Resolução do vídeo
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho [0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) -datetime.now().year
print('-=' * 30)
for k,v in dados.items():
    print(f'  - {k} tem o valor {v}')
