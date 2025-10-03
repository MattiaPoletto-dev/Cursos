'''Crie um programa que tenha uma tupla com várias palavras (não usar acento). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.'''

B = '\033[97m'
Ac = '\033[96m'
Am = '\033[93m'

tupla = ('Brasil','Itália','Noruega','Paquistão','China','japão','México','Venezuela')

for c in range(0,len(tupla)):
    print(f'\n{B}A palavra {Ac}{tupla[c]} {B}possui as vogais: ',end = '')
    for x in range(0, len(tupla[c])):
        if tupla[c][x] in 'aeiouáéíóúâêîôûAEIOUÁÉÍÓÚÂÊÎÔÛãõÃÕ':
            print(f'{Am}',tupla[c][x], end = ' ')
