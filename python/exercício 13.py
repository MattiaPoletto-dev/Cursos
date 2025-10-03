'''Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.'''

'''s = float(input('Salário do funcionário: R$'))
p = float(input('Qual o aumento do salário(em %): '))
aum = s * (1 + (p * 0.01))
luc = (s * (1 + (p * 0.01))) - s
print(f'Salário do funcionário com {p}% de aumento: R${aum:.2f}')
print(f'O aumento foi de R${luc:.2f}')'''


s = float(input('\033[97mQual é o salário do funcionário? R$'))
aum = s * 1.15
print(f'Um funcionário que ganhava \033[96mR${s:.2f}\033[97m, com \033[93m15%\033[97m de aumento,'
      f' passa a receber \033[92mR${aum:.2f}\033[97m.')
