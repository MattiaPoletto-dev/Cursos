'''Crie um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por
km para viagens de até 200km e R$0.45 por km para viagens mais longas.'''

'''dis = float(input('Qual é a distância da sua viagem(em km)? '))
conv1 = dis * 0.5
conv2 = dis * 0.45
if dis < 200:
    print(f'O preço da passagem é de R${conv1:.2f}')
if dis >= 200:
    print(f'O preço da passagem é de R${conv2:.2f}')'''


dis = float(input('\033[93mQual é a distância da sua viagem? '))
conv1 = dis * 0.5
conv2 = dis * 0.45
print(f'\033[97mVocê está prestes a começar uma viagem de \033[96m{dis}Km.')
if dis < 200:
    print(f'\033[97mE o preço da sua passagem será de \033[92mR${conv1:.2f}\033[97m.')
if dis >= 200:
    print(f'\033[97mE o preço da sua passagem será de \033[92mR${conv2:.2f}\033[97m.')
