'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''

#Minha resolução
d = dict()
l = list()
lmai = list()
while True:
    s = 0
    d['nome'] = str(input('Nome do jogador: ')).strip()
    npartidas = int(input(f'Quantas partidas {d["nome"]} jogou? '))
    for c in range(1,npartidas + 1):
        x = int(input(f'Quantos gols na {c}ª partida? '))
        s += x
        l.append(x)
    d['gols'] = l[:]
    d['soma de gols'] = s
    lmai.append(d.copy())
    l.clear()
    d.clear()
    while True:
        o = str(input('Quer continuar [S/N]? ')).lower().strip()
        if o in ['s','n']:
            break
        print('ERRO! Digite S ou N')
    if o == 'n':
        break
print(lmai)
print('-=' * 60)
print('               Nome                            Gols                Total   ')
print('-' * 76)
for i,v in enumerate(lmai):
        print(f'{i + 1}. {v["nome"]: <31}{str(v["gols"]): <30}{v["soma de gols"]: ^11}')
print('-' * 76)

while True:
    esc = int(input('Digite o número de qual jogador você quer ver os dados [0 para parar]: '))
    if esc == 0:
        break
    elif 0 < esc <= len(lmai):
        print(f' -- Levantamento do jogador(a) {lmai[esc - 1]["nome"]} --')
        for c in range(0, len(lmai[esc - 1]["gols"])):
            print(f'   No jogo {c + 1} fez {lmai[esc - 1]["gols"][c]}.')
    else:
        print(f'ERRO! Não existe jogador com o código {esc}')
    print('-' * 76)
print('-' * 76)
print('Programa finalizado com sucesso. Volte sempre!!!')
