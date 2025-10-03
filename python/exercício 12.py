'''Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.'''

'''p = float(input('Qual é o preço do produto? R$'))
r = float(input('Qual é o desconto do produto(em %)? '))
des = p * ((100 - r) * 0.01)
print(f'O produto que custava R${p:.2f}, na promoção com desconto de {r}% vai custar R${des:.2f}.')'''


p = float(input('\033[97mQual é o preço do produto? R$'))
des = p * 0.95
print(f'O produto que custava \033[96mR${p:.2f}\033[97m,'
      f' na promoção com desconto de \033[93m5%\033[97m vai custar \033[92mR${des:.2f}\033[97m.')
