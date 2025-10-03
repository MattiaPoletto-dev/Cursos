'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa.'''

'''cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
hip = ((cat1 ** 2) + (cat2 ** 2)) ** (1/2)
print(f'Sendo o cateto oposto {cat1} e o cateto adjacente {cat2} \na hipotenusa é igual a {hip:.2f}')'''


'''from math import sqrt, pow
cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
hip = sqrt(pow(cat1,2) + pow(cat2,2))
print(f'Sendo o cateto oposto {cat1} e o cateto adjacente {cat2} \na hipotenusa é igual a {hip:.2f}')'''


from math import sqrt
catop = float(input('\033[93mComprimento do cateto oposto: '))
cataj = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(pow(catop,2) + pow(cataj,2))
print(f'\033[97mA hipotenusa vai medir \033[96m{hip:.2f}')

# Obs: pode-se usar também from math import hypot
# ... hip = hypot(catop,cataj)
