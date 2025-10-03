'''Crie uma tupla preenchida com os 20 primeitos colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
     A)Apenas os 5 primeiros colocados
     B)Os últimos 4 colocados na tabela
     C)Uma lista com os times em ordem alfabética
     D)Em que posição da tabela está o time da Chapecoense*.'''

#Minha resolução
B = '\033[97m'
Verm = '\033[91m'
Verd = '\033[92m'
Ac = '\033[96m'
Ae = '\033[94m'
Am = '\033[93m'
M = '\033[95m'

tupla = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthias','Bahia','Cruzeiro','Vasco','Vitória',
         'Atlético-MG','Flumninense','Grêmio','Juventude','Bragantino','Athlético-PR','Criciúma','Atlético-GO','Cuiabá')

print(f'{B}Tabela do Brasileirão série A                                             | 09/12/2024')
print(f'{B}1.{Ae} {tupla[0]}    {B} 5.{Ae} {tupla[4]}   {B}9.{Verd} {tupla[8]}      {B}13.{Verd} {tupla[12]}   {B}17.{Verm} {tupla[16]}')
print(f'{B}2.{Ae} {tupla[1]}   {B} 6.{Ae} {tupla[5]}      {B}10.{Verd} {tupla[9]}         {B}14.{Verd} {tupla[13]}        {B}18.{Verm} {tupla[17]}')
print(f'{B}3.{Ae} {tupla[2]}    {B} 7.{Ac} {tupla[6]}     {B}11.{Verd} {tupla[10]}       {B}15.{B} {tupla[14]}     {B}19.{Verm} {tupla[18]}')
print(f'{B}4.{Ae} {tupla[3]}    {B}8.{Ac} {tupla[7]}          {B}12.{Verd} {tupla[11]}   {B}16.{B} {tupla[15]}    {B}20.{Verm} {tupla[19]}{B}')


print('Opções:\n[ 1 ]Primeiros colocados\n[ 2 ]Últimos colocados\n'
      '[ 3 ]Lista com os times em ordem alfabética\n[ 4 ]Posição de algum time\n[ 5 ]Fechar programa')
while True:
    print(f'{M}-' * 45)
    o = 0
    while o < 1 or o > 5:
        o = int(input(f'{Am}O que deseja saber: '))
    if o == 1:
        n = 0
        while n < 1 or n > 20:
            n1 = int(input(f'Quantos times deseja ver? {B}'))
            for c in range(0, n1):
                print(c + 1,')',tupla[c], end = '  ' if c < n1 - 1 else '\n')
            n = 2
    elif o == 2:
        u = 0
        while u < 1 or u > 20:
            n2 = int(input(f'Quantos times deseja ver? {B}'))
            for x in range(19,19 - n2,-1):
                print(x + 1,')',tupla[x], end = '  ' if x > 20 - n2 else '\n')
            u = 2
    elif o == 3:
            print(f'{B}',sorted(tupla))
    elif o == 4:
        v = 'aaaa'
        while v not in tupla:
            v = str(input('Digite o nome do time: ')).strip().title()
        print(f'{B}O time {Ac}{v} {B}está na {Ac}{tupla.index(v) + 1} {B}posição')
    elif o == 5:
        break
print(f'{Verd}Programa finalizado com sucesso. Volte sempre!!!')
