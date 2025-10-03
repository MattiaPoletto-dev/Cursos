'''Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na
tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

#Minha resolução
from ex107_a_ex112 import moeda4

p = float(input('Digite o preço: R$'))
aumento = float(input('Quanto foi o aumento (em %)? '))
reducao = float(input('Quanto reduziu (em %)? '))
moeda4.resumo(p,aumento,reducao)
