'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de
acordo com a tabela abaixo:
     - abaixo de 18,5: ABAIXO DO PESO
     - entre 18.5 e 25: PESO IDEAL
     - entre 25 e 30: SOBREPESO
     - entre 30 e 40: OBESIDADE
     - acima de 40: OBESIDADE MÓRBIDA.'''

altura = float(input('\033[93mQual é sua altura (em metros)? '))
peso = float(input('Qual é o seu peso (em kg)? '))

imc =  peso / (altura ** 2)

if 0 < imc < 18.5:
    if imc < 14:
        print(f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[91mABAIXO DO PESO')
    else:
        print(
            f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[93mABAIXO DO PESO')

elif 18.5 <= imc < 25:
    print(f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[92mPESO IDEAL')
elif 25 <= imc < 30:
    print(f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[93mSOBREPESO')
elif 30 <= imc < 40:
    print(f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[31mOBESIDADE')
elif imc >= 40:
    print(f'\033[97mTendo \033[96m{altura}m \033[97mde altura e \033[96m{peso}kg\n\033[97mIMC = \033[96m{imc:.1f}\n\033[97mClassificação: \033[91mOBESIDADE MÓRBIDA')
else:
    print(f'\033[91mErro. \033[97mTente novamente.')
