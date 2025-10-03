'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.'''

#Minha resolução
p = ''
s = cont = 0
while p != 'n':
    cont += 1
    if cont == 1:
        n = int(input('\033[90mDigite um número inteiro: '))
        p = str(input('Quer continuar [S/N]: ')).strip().lower()
        maior = menor = n
    else:
        n = int(input('Digite um número inteiro: '))
        p = str(input('Quer continuar [S/N]: ')).strip().lower()
        if n >= maior:
            maior = n
        elif n <= menor:
            menor = n
    s += n

print(f'\033[97mEntre os \033[96m{cont}\033[97m números digitados, tem-se:\nMédia: \033[96m{s / cont}'
      f'\n\033[97mMaior: \033[96m{maior}\n\033[97mMenor: \033[96m{menor}')

#Resolução do vídeo
'''resp = 's'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')'''
