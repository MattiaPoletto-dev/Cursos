'''Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No
final, mostre o conteúdo da estrutura na tela.'''

#Minha resolução
dic = dict()

n = str(input('Nome: '))
m = float(input('Média: '))

dic['Nome'] = n
dic['Média'] = m
if m >= 7:
    dic['situação'] = 'aprovado'
elif  5 <= m < 7:
    dic['situação'] = 'recuperação'
elif 0 <= m < 5:
    dic['situação'] = 'reprovado'


print('-=-' * 15)
for i,v in dic.items():
    print(f'   - O {i} é igual a {v}')
