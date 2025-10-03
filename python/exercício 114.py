'''Crie um código em Python que teste se o site YouTube está acessível pelo computador usado.'''

import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except:
    print('O site YouTube não está acessando no momento.')
else:
    print('Consegui acessar o site YouTube com sucesso!')
    print(site.read()) #Conteúdo do site