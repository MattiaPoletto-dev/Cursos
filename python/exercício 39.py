'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
     - se ele ainda vai se alistar ao serviço militar
     - se é a hora de se alistar
     - se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

# Minha resolução
from datetime import date
ano = int(input('\033[93mEm qual ano você nasceu? '))

idade = date.today().year - ano
tempo = 18 - idade

if idade < 18 and idade > 0:
    if idade == 17:
        print(f'\033[97mNascido em \033[96m{ano}\033[97m com \033[96m{idade} anos de idade\033[97m.\nAinda falta \033[92m1 ano\033[97m para seu alistamento!')
    else:
        print(f'\033[97mNascido em \033[96m{ano}\033[97m com \033[97m{idade} anos de idade\033[97m.\nAinda faltam \033[92m{tempo} anos \033[97mpara seu alistamento!')
elif idade == 18:
    print(f'\033[97mEstá na hora de você se alistar!')
elif idade < 1:
    print('\033[91mIdade inválida. \033[97mTente novamente.')
else:
    conv = tempo * (-1)

    if conv == 1:
        print(f'\033[97mNascido em \033[96m{ano} \033[97mcom \033[96m{idade} de idade\033[97m.\nJá se passou \033[91m1 ano\033[97m o seu alistamento!')
    elif conv > 1:
        print(f'\033[97mNascido em \033[96m{ano} \033[97mcom \033[96m{idade} anos de idade\033[97m.\nJá se passaram \033[91m{conv} anos \033[97mo seu alistamento!')
