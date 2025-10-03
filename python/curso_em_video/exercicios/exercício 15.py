'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
 pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.'''

'''km = float(input('Quantidade de km percorridos pelo carro: '))
dias = int(input('Quantidade de dias em que o carro foi alugado: '))
preço = 60 * dias + 0.15 * km
print(f'O preço a pagar de um carro alugado por {dias} dias e que rodou {km}km é de R${preço:.2f}')'''


dias = int(input('\033[93mQuantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preço = dias * 60 + km * 0.15
print(f'\033[97mO total a pagar é de \033[92mR${preço:.2f}')
