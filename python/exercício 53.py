'''Crie um programa que leia uma frase qualquer e diga se ele é um palíndromo, desconsiderando os espaços.'''

#Resolução do vídeo
'''print('\033[93m-_' * 20)
print('¡\033[97m        Detector de palíndromos       \033[93m!')
print('-_' * 20)

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')'''

#Segunda resolução
frase = str(input('Digite uma frase: ')).strip().lower()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
