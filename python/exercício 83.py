'''Crie um programa onde o usuário digite uma expressão qualquer que use parêntesis. Seu aplicativo deverá
analisar se a expressão passada está com os parêntesis abertos e fechados na ordem correta.'''

#Minha resolução
'''lista = list()
e = str(input('Digite a expressão númerica: ')).lower().strip()
if e.count('(') != e.count(')'):
    print('Sua expressão está errada!')
else:
    for i, v in enumerate(e):
        lista.append(v)
        if lista.count('(') < lista.count(')'):
            print('Sua expressão está errada!')
            break
        if i == len(e) - 1:
            print('Sua expressão está correta!')
            break'''

#Resolução do vídeo
e = str(input('Digite a expressão: '))
pilha = []
for simb in e:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
