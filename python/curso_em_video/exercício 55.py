'''Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

#Resolução do vídeo
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}ª pessoa (em kg): '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg\nO menor peso lido foi de {menor}g')
