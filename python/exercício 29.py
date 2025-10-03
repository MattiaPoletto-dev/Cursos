'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite'''

'''v = float(input('Velocidade do carro(em km/h): '))
if v <= 80:
    print('Você está no limite de velocidade!')
else:
    multa = (v - 80)
    conv1 = multa * 7
    print(f'Você foi multado! Foi a {v}km/h numa pista de 80km/h\nTotal a pagar: R${conv1}')'''


v = float(input('Qual é a velocidade atual do carro: '))
conv1 = (v - 80) * 7

if v > 80:
    print(f'\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h\nVocê deverá pagar uma multa de \033[93mR${conv1:.2f}')

print('\033[32mTenha um bom dia! Dirija com segurança!')
