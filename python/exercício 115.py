'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

from ex115.funcoes115 import menu
from ex115.arquivo import * #Tudo

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    p = menu()
    if p == 1:
        lerArquivo(arq)
    elif p == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    else:
        break

cabecalho('Saindo do sistema... Até logo!')
