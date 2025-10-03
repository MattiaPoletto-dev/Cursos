'''Escreva um programa que converta uma temperatura digitada em °C e converta para °F.'''

'''c = float(input('Temperatura em Celcius: '))
conv1 = 1.8 * c + 32
conv2 = c + 273
print(f'Temperatura em Fahrenheit: {conv1}')
print(f'Temperatura em Kelvin    : {conv2}')'''


c = float(input('\033[97mInforme a temperatura em °C: '))
conv = 1.8 * c + 32
print(f'A temperatura de \033[92m{c}°C\033[97m corresponde a \033[94m{conv}°F\033[97m!')
