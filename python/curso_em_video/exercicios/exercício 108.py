'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valo-
res como um valor monetário formatado.'''

#Resolução do vídeo
from ex107_a_ex112 import moeda2

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}')
print(f'Aumentando 10%, temos {moeda2.moeda(moeda2.aumentar(p, 10))}')
