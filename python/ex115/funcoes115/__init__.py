from time import sleep
B,Verd,Verm,Az,Am = '\033[97m','\033[92m','\033[91m','\033[94m','\033[93m'


def cabecalho(msg):
    print(f'{B}-' * 50)
    print(f'{msg: ^50}') #tembém funciona msg.center(50)
    print('-' * 50)


def menu():
    cabecalho('MENU PRINCIPAL')
    print(f'{Am}1 - {Az}Ver pessoas cadastradas\n{Am}2 - {Az}Cadastrar nova Pessoa\n{Am}3 - {Az}Sair do Sistema')
    print(f'{B}-' * 50)
    while True:
        try:
            x = int(input(f'{Verd}Sua opção: '))
        except ValueError:
            print(f'{Verm}ERRO! Por favor, digite um número inteiro válido')
        except KeyboardInterrupt:
            print()
            print(f'{B}-' * 50)
            print(f'{B}Finalizando...')
            sleep(2.5)
            print(f'{Verd}Até a próxima')
            exit()
        else:
            if x < 1 or x > 3:
                print(f'{Verm}ERRO! Digite uma opção válida!')
            else:
                sleep(1)
                return x

def opcao(x):
    cabecalho(x)
