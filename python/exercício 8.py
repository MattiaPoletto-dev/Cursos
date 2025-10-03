'''Escreva um programa que leia um valor em metros e o exiba convetido em km, hm, dam, dm, cm e mm.'''

'''v = float(input('Valor em metros: '))
km = (1/1000) * v
hm = (1/100) * v
dam = (1/10) * v
dm = 10 * v
cm = 100 * v
mm = 1000 * v
print(f'A medida de {v}m equivale a {km}km, {hm}hm, {dam}dam, {dm}dm, {cm}cm, {mm}mm.')'''


v = float(input('\033[96mUma distância em metros: '))
km = (1/1000) * v
hm = (1/100) * v
dam = (1/10) * v
dm = 10 * v
cm = 100 * v
mm = 1000 * v
print(f'\033[97mA medida de \033[96m{v}m \033[97mcorresponde a:\033[92m \n{km} km \n{hm} hm '
      f'\n{dam} dam \n{dm} dm \n{cm} cm \n{mm} mm')
