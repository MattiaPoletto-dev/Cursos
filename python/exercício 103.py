'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente.'''

#Minha resolução bem da safadinha
'''def ficha(pnome,ngols):
    if pnome == '' and ngols != '':
        if ngols[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
        else:
            print(f'O jogador <desconhecido> fez {ngols} gol(s) no campeonato.')
    elif ngols == '' and pnome != '':
        print(f'O jogador {pnome} fez 0 gols no campeonato')
    elif pnome == '' and ngols == '':
        print(f'O jogador <desconhecido> fez 0 gols no campeonato.')
    else:
        if ngols[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print(f'O jogador {pnome} fez 0 gol(s) no campeonato.')
        else:
            print(f'O jogador {pnome} fez {ngols} gol(s) no campeonato.')

     #Programa principal
print('-' * 30)
ficha(str(input('Nome do jogador: ')).strip(), str(input('Número de gols: ')))'''

#Resolução do vídeo
'''def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


     #programa principal
n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n,g)
'''