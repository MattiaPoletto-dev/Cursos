'''Faça um programa que mostre na tela uma contagem regressiva para o estouro dos fogos de artifício,
indo de 10 a 0, com uma pausa de 1 segundo entre eles.'''

# Minha resolução
from time import sleep
print('\033[96mVai começar a contagem regressiva para os fogos!!!\033[97m')
sleep(2)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('0')
print('\033[96m🎉🎉🎉Booom!! \033[92mPaaaa!! \033[95mPooooww!!🎉🎉🎉')
