'''Dentro do pacote utilidadesCeV que foi criado no desafio 111, temos um módulo chamado dado. Crie uma fun-
ção chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.'''

#Resolução do vídeo
from ex107_a_ex112.ex111.utilidadesCeV import moeda5,dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda5.resumo(p, 35,22)
