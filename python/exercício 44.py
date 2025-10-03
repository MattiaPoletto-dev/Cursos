'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço mensal e
condições de pagamento:
     - à vista (dinheiro / cheque): 10% de desconto
     - à vista no cartão: 5% de desconto
     - em até 2x no cartão: preço normal
     - 3x ou mais no cartão: 20% de juros.'''

# Minha resolução
produto = float(input('\033[96mPreço do produto: R$'))
print('\033[97mFormas de pagamento:\n[ 1 ] Dinheiro (desconto de 10%)\n[ 2 ] Cheque (desconto de 10%)\n[ 3 ] Cartão')
opção = int(input('\033[96mEscolha: '))
if opção == 1 or opção == 2:
    conv1 = produto * 0.9
    print(f'\033[97mO produto de \033[92mR${produto:.2f} \033[97mrecebe 10% de desconto, passando a custar \033[92mR${conv1:.2f}\033[97m.')
elif opção == 3:
    print('\033[97mOpções:\n[ 1 ] À vista (desconto de 5%)\n[ 2 ] À prazo (2x: preço normal; acima de 2x: juros de 20%)')
    opção2 = int(input('\033[96mPagará à vista ou à prazo? '))
    if opção2 == 1:
        conv2 = produto * 0.95
        print(f'\033[97mO produto de \033[92mR${produto:.2f} \033[97mrecebe 5% de desconto, passando a custar \033[92m{conv2:.2f}\033[97m.')
    elif opção2 == 2:
        opção3 = int(input('\033[96mEm quantas vezes deseja dividir (máx 12x)? '))
        if opção3 == 2:
            x = produto / opção3
            print(f'\033[97mO produto permanece com o preço normal de \033[92mR${produto:.2f}\n\033[97mCusto de cada parcela: \033[92mR${x:.2f}')
        elif opção3 >= 3 and opção3 <= 12:
            juros = produto * 1.2
            y = juros / opção3
            print(f'\033[97mO produto de \033[92mR${produto:.2f} \033[97mrecebe um juros de 20%, passando a custar \033[92mR${juros:.2f}\n\033[97mCusto de cada parcela: \033[92mR${y:.2f}\033[97m.')
        else:
            print('\033[91mOpção inválida! \033[97mTente novamente')
    else:
        print('\033[91mOpção inválida! \033[97mTente novamente')
else:
    print('\033[91mOpção inválida! \033[97mTente novamente')
