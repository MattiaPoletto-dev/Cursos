'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

#Minha resolução que nem o chat gpt entendeu
'''l = list()
for c in range(0,5):
    l.append(int(input('Digite um número para a lista: ')))
for d in range(0,5):
    for x in range(0,4):
        if l[x] > l[x + 1]:
            l.insert(x + 2,l[x])
            l.remove(l[x])
print(f'Os valores digitados, em ordem, foram {l}')'''

#Solução do vídeo
lista = list()

for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Primeiro número adicionado com sucesso!!')
    elif n > lista[-1]:
        lista.append(n)
        print('Número adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
