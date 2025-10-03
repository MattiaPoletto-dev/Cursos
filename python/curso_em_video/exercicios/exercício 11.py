'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
 tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².'''

'''l = float(input('Largura da parede (em metros): '))
a = float(input('Altura da parede (em metros): '))
ar = l * a
qt = ar / 2
print('-' * 50)
print(f'Tendo uma parede de {l:.3f}m de largura e {a:.3f}m de altura, tem-se:')
print(f'Área da parede                     : {ar:.3f}m² \nQuantidade necessária para pintá-la: {qt:.3f}L')
print('-' * 50)'''


l = float(input('\033[93mLargura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
qt = ar / 2
print(f'\033[97mSua parede tem a dimensão de {l}x{a} e sua área é de \033[92m{ar:}m²\033[97m.')
print(f'Para pintar essa parede, você precisará de \033[96m{qt}L\033[97m de tinta.')