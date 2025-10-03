'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantas anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele
não pode exceder 30% do salário ou então o empréstimo será negado.'''

# meu programa:
'''valor_da_casa = float(input('\033[93mQual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = float(input('em quantos anos será pago?'))

prestacao_mensal = valor_da_casa / (tempo * 12)

if prestacao_mensal <= salario * 0.3:
    print('\033[92mO empréstimo foi aprovado!')
    print(f'\033[97mA prestação mensal da casa é de \033[96mR${prestacao_mensal:.2f}\033[97m.')
else:
    print('\033[91mO empréstimo foi negado!')'''

# Igual ao dele:
valor_da_casa = float(input('\033[97mValor da casa: \033[92mR$'))
salario = float(input('\033[97mSalário do comprador: \033[92mR$'))
tempo = int(input('\033[97mQuantos anos de financiamento? '))

prestacao_mensal = valor_da_casa / (tempo * 12)

print(f'\033[97mPara pagar uma casa de \033[92mR${valor_da_casa:.2f} \033[97mem \033[96m{tempo} anos'
      f'\033[97m, a prestação será de \033[92mR${prestacao_mensal:.2f}\033[97m.')
if prestacao_mensal <= salario * 0.3:
    print('\033[92mEmpréstimo APROVADO!')
else:
    print('\033[91mEmpréstimo NEGADO!')
