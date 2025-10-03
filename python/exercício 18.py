'''Faça um programa que leia um ângulo qualquer e mostre na tela  valor do seno, cosseno e tangente desse ângulo.'''

'''from math import sin,cos,tan,pi
n = float(input('Digite um ângulo (em graus): '))
conv = n * pi / 180
seno = sin(conv)
cosseno = cos(conv)
tangente = tan(conv)
print(f'O ângulo {n} possui:\nseno     = {seno:.4f}\ncosseno  = {cosseno:.4f}\ntangente = {tangente:.4f}')'''


import math
angulo = float(input('\033[93mDigite o ângulo que você deseja (em graus): '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print(f'\033[97mO ângulo de {angulo}° tem:\n\033[96mseno     = {s:.2f} \ncosseno  = {c:.2f} \ntangente = {t:.2f}')
