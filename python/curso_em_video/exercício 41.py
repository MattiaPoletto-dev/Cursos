'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria de acordo com sua idade:
     - até os 9 anos: MIRIM
     - de 9 aos 14 anos:INFANTIL
     - de 14 aos 19 anos: JUNIOR
     - de 19 aos 25 anos: SÊNIOR
     - acima ou igual dos 25 anos: MASTER.'''

# Minha resolução
from datetime import date
ano = int(input('\033[93mEm que ano o competidor nasceu? '))

idade = date.today().year - ano

if 0 < idade < 9:
    print('\033[97mSua categoria é \033[96mMIRIM\033[97m!')
elif 9 <= idade < 14:
    print('\033[97mSua categoria é \033[96mINFANTIL\033[97m!')
elif 14 <= idade < 19:
    print('\033[97mSua categoria é \033[96mJUNIOR\033[97m!')
elif 19 <= idade < 25:
    print('\033[97mSua categoria é \033[96mSÊNIOR\033[97m!')
elif 25 <= idade:
    print('\033[97mSua categoria é \033[96mMASTER\033[97m!')
else:
    print('\033[91mAno inválido\033[97m. Tente novamente')
