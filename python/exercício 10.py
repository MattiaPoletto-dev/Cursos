'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar.
(Obs:US$1.00 = R$3.27)'''

'''d = float(input('Quantos reias você tem na carteira? '))
p = d / 3.27
print(f'Você consegue até {p:.2f} dólares no câmbio.')'''

r = float(input('\033[97mQuanto dinheiro você tem na carteira? \033[92mR$'))
d = r / 5.80
e = r / 6.10
l = r / 7.30
print('\033[91m-' *40)
print('\033[97mNo dia 26/11/2024, seu dinheiro vale:')
print(f'\033[96mDólar(US$)  = {d:.2f} \n\033[93mEuro (€)    = {e:.2f} \n\033[95mLibra (£)   = {l:.2f}')
print('\033[91m-' *40)


'''d = float(input('Quanto dinheiro você tem na carteira? R$'))
p = d / 3.27
print(f'Com R${d:.2f} você pode comprar US${p:.2f}')'''
