'''Faça um minissistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.'''

#MInha resolução
from time import sleep

def texto(txt,cor):
    print(f'{cor}-' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('-' * (len(txt) + 4))


while True:
    texto('SISTEMA DE AJUDA PyHELP','\033[1:97:42m')
    x = str(input('\033[0:97mSobre qual função deseja saber? ')).lower().strip()
    if x == 'fim':
        break
    texto(f'Acessando o manual do comando "{x}"','\033[1:97:44m')
    sleep(2)
    print('\033[0:97:47m', end = '')
    help(x)

print('\033[1:97:44m  Finalizando...')
sleep(1.5)
texto('Até logo!','\033[0:97:41m')
