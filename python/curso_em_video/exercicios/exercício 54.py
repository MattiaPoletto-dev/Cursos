'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores'''

#Minha resoluçãp
from datetime import date
tot1 = 0
tot2 = 0
for c in range(1, 8):
    ano = int(input(f'\033[93mAno de nascimento da {c}ª pessoa: '))
    idade = date.today().year - ano
    if idade >= 18:
        tot1 += 1
    else:
        tot2 += 1
print(f'\033[96m{tot1} \033[97mpessoas maiores de idade \n\033[96m{tot2} \033[97mpessoas menores de idade')
