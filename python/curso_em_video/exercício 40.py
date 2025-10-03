'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de
acordo com a média atingida
     - média abaixo de 5.0: REPROVADO
     - média entre 5.0 <= x < 6.0: RECUPERAÇÃO
     - média acima de 7.0: APROVADO.'''

# Minha resolução
n1 = float(input('\033[93mPrimeira nota: '))
n2 = float(input('Segunda nota: '))

Ma = (n1 + n2) / 2

print(f'\033[97mTendo tirado \033[96m{n1:.2f}\033[97m e \033[96m{n2:.2f}\033[97m, sua média foi de \033[96m{Ma:.2f}\033[97m.')
if Ma < 5.0:
    print('\033[97mVocê foi \033[91mREPROVADO\033[97m!')
elif 5.0 <= Ma < 7.0:
    print('\033[97mVocê ficou de \033[93mRECUPERAÇÃO\033[97m!')
elif Ma >= 7.0:
    print('\033[92mParabéns\033[97m!!! Você foi \033[92mAPROVADO\033[97m!')
