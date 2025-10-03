'''Escreva um programa que pergunta o salário de um funcionário e calcule o valor de seu aumento. Para salários
superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

'''sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250.00:
    aum1 = sal * 1.1
    lucro1 = sal * 0.1
    print(f'O salário do funcionário foi de R${sal:.2f} para R${aum1:.2f}\nHouve um aumento de R${lucro1:.2f}')
else:
    aum2 = sal * 1.15
    lucro2 = sal * 0.15
    print(f'O salário do funcionário foi de R${sal:.2f} para R${aum2:.2f}\nHouve um aumento de R${lucro2:.2f}')'''


sal = float(input('\033[93mQual é o salário do funcionário: \033[92mR$'))
if sal > 1250.00:
    aum1 = sal * 1.1
    print(f'\033[97mQuem ganhava \033[92mR${sal:.2f}\033[97m passa a ganhar \033[92mR${aum1:.2f}\033[97m agora.')
else:
    aum2 = sal * 1.15
    print(f'\033[97mQuem ganhava \033[92mR${sal:.2f}\033[97m passa a ganhar \033[92mR${aum2:.2f}\033[97m agora.')
