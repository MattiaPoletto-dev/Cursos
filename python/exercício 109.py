'''Modifique as funções que foram usadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

#Resolução do vídeo
from ex107_a_ex112 import moeda3

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, True)}')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda3.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda3.diminuir(p, 13, True)}')
