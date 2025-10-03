'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será
guardado em um ducionário, incluindo o total de gols feitos durante o campeonato.'''

#Minha resolução
dic = dict()
lista = list()
dic['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
s = 0
for c in range(1, partidas + 1):
    x = int(input(f'Quantos gols na {c}ª partida? '))
    s += x
    lista.append(x)
dic['gols'], dic['total'] = lista.copy(), s
print('-=' * 40)
print(dic)
print('-=' * 40)
for i,v in dic.items():
    print(f'O campo {i} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {dic["nome"]} jogou {partidas} partidas.')
for c in range(1, partidas + 1):
    if dic['gols'][c - 1] == 1:
        print(f'   Na {c}ª partida, fez {dic["gols"][c - 1]} gol')
    else:
        print(f'   Na {c}ª partida, fez {dic["gols"][c - 1]} gols')
if s == 0:
    print('Não marcou gol nenhum')
elif s == 1:
    print('Marcou apenas 1 gol')
else:
    print(f'Foi um total de {s} gols')
