'''Crie um programa que tenha uma tupla totalmente preenchida cmo uma contagem por extenso, do zero até
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

#Minha resolução
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('\033[95m-' * 50)
    n = int(input('\033[97mDigite um número de 0 a 20 [999 para parar]: '))
    if 0 <= n <= 20:
        print(f'O número digitado foi: \033[96m{tupla[n]}\033[97m')
    elif n == 999:
        break
    else:
        print('\033[91mValor inválido, tente novamente.')
print('\033[95m-' * 50)
print('\033[92mPrograma finalizado com sucesso!!!')
