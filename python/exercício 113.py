'''Reescreva a função leiaint() que foi feita no desafio 104, incluindo a possibilidade de digitação de um
número de tipo inválido, Aproveite e crie também uma função leiaFloat() com a mesma funcionabilidade.'''

def leiaint(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO! Por favor, digite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[97m\nO usuário não quis digitar o valor.\033[m')
            return 0
        else:
            return x

def leiafloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError, TypeError):
            print('\033[91mERRO! Por favor, digite um número válido.\033[m')
        except KeyboardInterrupt:
            print('\033[97m\nO usuário não quis digitar o valor.\033[m')
            return 0
        else:
            return x


n1 = leiaint('Digite um número Inteiro: ')
n2 = leiafloat('Digite um número Real: ')
print(f'Valor inteiro: {n1}\nValor real: {n2}')
