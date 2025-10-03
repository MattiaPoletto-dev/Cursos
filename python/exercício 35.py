'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
um triângulo.'''

'''med1 = float(input('Primeiro segmento: '))
med2 = float(input('Segundo segmento: '))
med3 = float(input('Terceiro segmento: '))
s1 = med1 + med2
s2 = med1 + med3
s3 = med2 + med3
if med3 >= s1 or med2 >= s2 or med1 >= s3:
    print(f'O triângulo com {med1}, {med2} e {med3} NÃO é formado :(')
else:
    print(f'O triângulo com {med1}, {med2} e {med3} é formado :)')'''


print('\033[97m-=' * 20)
print('\033[95mAnalisador de Triângulos')
print('\033[97m-=' * 20)
med1 = float(input('\033[93mPrimeiro segmento: '))
med2 = float(input('Segundo segmento: '))
med3 = float(input('Terceiro segmento: '))
s1 = med1 + med2
s2 = med1 + med3
s3 = med2 + med3
if med3 >= s1 or med2 >= s2 or med1 >= s3:
    print(f'\033[97mOs segmentos acima \033[91mNÃO PODEM FORMAR triângulo!')
else:
    print(f'\033[97mOs segmentos acima \033[92mPODEM FORMAR triângulo!')
