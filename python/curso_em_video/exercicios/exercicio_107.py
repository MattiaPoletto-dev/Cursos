'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e meta-
de(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

#Minha resolução
from ex107_a_ex112 import moeda

valor = float(input('Digite o preço: R$'))

print(f'O dobro de {valor:.2f} é {moeda.dobro(valor):.2f}')
print(f'A metade de {valor:.2f} é {moeda.metade(valor):.2f}')
aumentar = float(input(f'Em quantos % deseja aumentar o valor {valor:.2f}? '))
print(f'Aumentando em {aumentar}%, temos o valor {moeda.aumento(valor, aumentar):.2f}')
diminuir = float(input(f'Em quantos % deseja diminuir o valor {valor:.2f}?'))
print(f'Diminuindo em {diminuir}%, temos o valor {moeda.diminuir(valor, diminuir):.2f}')
