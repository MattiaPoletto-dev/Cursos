'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira
todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e maantenha tudo funcionando.'''

from ex107_a_ex112.ex111.utilidadesCeV import moeda5,dado

p = float(input('Digite o preço: R$'))
aumento = float(input('Quanto foi o aumento (em %)? '))
reducao = float(input('Quanto reduziu (em %)? '))
moeda5.resumo(p,aumento,reducao)
