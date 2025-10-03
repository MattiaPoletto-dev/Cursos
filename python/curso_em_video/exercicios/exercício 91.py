'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

#Minha resolução
'''from random import randint
from time import sleep

print('\nNeste jogo, cada jogador deverá lançar o dado, um de cada vez, e caso o dado lançado seja igual a um número já lançado\n'
      'o jogador deverá lançar novamente. Vence quem lançar o maior valor!\n')
int1 = str(input('(press enter for start)'))

lista = list()
lista2 = list()
dic = dict()
cont = 0
while True:
    x = randint(1,6)
    if x not in lista:
        lista.append(x)
        cont += 1
        print(f'Jogador{cont} tirou {lista[cont - 1]} no dado')
        sleep(1)
    if len(lista) == 4:
        break
lista2 = lista[:]
lista2.sort(reverse = True)
print('-=-' * 20)
print('  == RANKINGO DOS JOGADORES ==')
sleep(1.5)
for c in range(0,4):
    for v in range(0,4):
        if lista[v] == lista2[c]:
            print(f'    {c + 1}° lugar: jogador{v + 1} com {lista2[c]}')'''

#Resolução do vídeo
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
ranking = list()

print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('=-=' * 20,'\n== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'  {i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
