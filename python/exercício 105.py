'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
     A)Quantidade de notas
     B)A maior nota
     C)A menor nota
     D)A média da turma
     E)A situação (opcional)
Adicione também as docstrings da função.'''

#Minha resolução
'''def dicionario(plista):
    """
--> Função que recebe uma lista de notas e devolve várias informações sobre ela em um dicionário.
    :param plista: lista de notas recebidas.
    :return: um dicionário com várias informações sobre a situação da turma.
    """
    plista.sort(reverse = True)
    d = dict()
    d['total'] = cont
    d['maior'] = plista[0]
    d['menor'] = plista[len(plista) - 1]
    d['média'] = f'{(s / cont):.2f}'
    if opc == 's':
        if (s / cont) >= 9:
            d['situação'] = 'EXCELENTE'
        elif 7 <= (s / cont) < 9:
            d['situação'] = 'BOA'
        elif 5 <= (s / cont) < 7:
            d['situação'] = 'RAZOÁVEL'
        elif 3 <= (s / cont) < 5:
            d['situação'] = 'RUIM'
        else:
            d['situação'] ='PÉSSIMA'
        return d
    else:
        return d


lista = list()
cont = s = 0
while True:
    cont += 1
    x = float(input(f'{cont}ª nota: '))
    s += x
    lista.append(x)
    while True:
        y = str(input('Teve mais [S/N]? ')).lower().strip()
        if y in ['s','n']:
            break
    if y == 'n':
        break
while True:
    opc = str(input('Deseja que seja mostrado a situação [S/N]? ')).lower().strip()
    if opc in ['s','n']:
        break

print('-=' * 35)
resp = dicionario(lista)
print(resp)
print('-=' * 35)
while True:
    opc2 = str(input('Deseja que seja mostrado a funcionabilidade'
                     ' da função dicionário utilizada [S/N]? ')).lower().strip()
    if opc2 in ['s','n']:
        break
if opc2 == 's':
    help(dicionario)
print('-=' * 35)
print('Programa finalizado com sucesso. Volte sempre!!!')'''

#Resolução do vídeo
def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informções sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5,2.5,1.5, sit=True)
print(resp)
help(notas)
