'''Crie um programa que tenha a função leiaint(), que vai funcionar da forma semelhante à função input() do
Python, só que fazendo a validação para aceitar apenas um valor númerico.
   Ex: n = leiaint("Digite um número: ").'''

#Minha resolução
B, Verm, Ac = '\033[97m','\033[91m','\033[96m'

def leiaint(x):
    while True:
        y = str(input(x))
        if y.isnumeric():
            y = int(y)
            return y
        else:
            print(f'{Verm}ERRO! Digite um valor inteiro válido.')

     #Programa principal
n = leiaint(f'{B}Digite um número inteiro: ')
print(f'{B}Você acabou de digitar o número {Ac}{n}')
