'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
de conversão:
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal.'''

# Minha resolução (não aceita todos os números e não consegui a base 16)
from stringprep import c22_specials
n1 = int(input('Digite um número: '))
print('Para qual base deseja transformar esse número? \n[ 1 ] para base binário \n[ 2 ] para base octal \n[ 3 ] para base hexadecimal')
n2 = int(input('Escolha: '))


'''if n2 == 1:
    a1 = n1 // 2
    a2 = a1 // 2
    a3 = a2 // 2
    a4 = a3 // 2
    a5 = a4 // 2
    a6 = a5 // 2
    a7 = a6 // 2
    a8 = a7 // 2
    a9 = a8 // 2
    a10 = a9 // 2
    a11 = a10 // 2
    a12 = a11 // 2
    a13 = a12 // 2
    a14 = a13 // 2
    a15 = a14 // 2
    a16 = a15 // 2
    a17 = a16 // 2
    a18 = a17 // 2
    a19 = a18 // 2
    a20 = a19 // 2
    a21 = a20 // 2
    a22 = a21 // 2
    a23 = a22 // 2
    a24 = a23 // 2
    a25 = a24 // 2
    a26 = a25 // 2
    a27 = a26 // 2
    a28 = a27 // 2
    a29 = a28 // 2
    a30 = a29 // 2

    A1 = n1 % 2
    A2 = a1 % 2 * 10 ** 1
    A3 = a2 % 2 * 10 ** 2
    A4 = a3 % 2 * 10 ** 3
    A5 = a4 % 2 * 10 ** 4
    A6 = a5 % 2 * 10 ** 5
    A7 = a6 % 2 * 10 ** 6
    A8 = a7 % 2 * 10 ** 7
    A9 = a8 % 2 * 10 ** 8
    A10 = a9 % 2 * 10 ** 9
    A11 = a10 % 2 * 10 ** 10
    A12 = a11 % 2 * 10 ** 11
    A13 = a12 % 2 * 10 ** 12
    A14 = a13 % 2 * 10 ** 13
    A15 = a14 % 2 * 10 ** 14
    A16 = a15 % 2 * 10 ** 15
    A17 = a16 % 2 * 10 ** 16
    A18 = a17 % 2 * 10 ** 17
    A19 = a18 % 2 * 10 ** 18
    A20 = a19 % 2 * 10 ** 19
    A21 = a20 % 2 * 10 ** 20
    A22 = a21 % 2 * 10 ** 21
    A23 = a22 % 2 * 10 ** 22
    A24 = a23 % 2 * 10 ** 23
    A25 = a24 % 2 * 10 ** 24
    A26 = a25 % 2 * 10 ** 25
    A27 = a26 % 2 * 10 ** 26
    A28 = a27 % 2 * 10 ** 27
    A29 = a28 % 2 * 10 ** 28
    A30 = a29 % 2 * 10 ** 29

    at = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15 + A16 + A17 + A18 + A19 + A20 + A21 + A22 + A23 + A24 + A25 + A26 + A27 + A28 + A29 + A30

    print(f'O número {n1}, na base 2, é {at}.')
elif n2 == 2:
    a1 = n1 // 8
    a2 = a1 // 8
    a3 = a2 // 8
    a4 = a3 // 8
    a5 = a4 // 8
    a6 = a5 // 8
    a7 = a6 // 8
    a8 = a7 // 8
    a9 = a8 // 8
    a10 = a9 // 8
    a11 = a10 // 8
    a12 = a11 // 8
    a13 = a12 // 8
    a14 = a13 // 8
    a15 = a14 // 8

    A1 = n1 % 8
    A2 = a1 % 8 * 10 ** 1
    A3 = a2 % 8 * 10 ** 2
    A4 = a3 % 8 * 10 ** 3
    A5 = a4 % 8 * 10 ** 4
    A6 = a5 % 8 * 10 ** 5
    A7 = a6 % 8 * 10 ** 6
    A8 = a7 % 8 * 10 ** 7
    A9 = a8 % 8 * 10 ** 8
    A10 = a9 % 8 * 10 ** 9
    A11 = a10 % 8 * 10 ** 10
    A12 = a11 % 8 * 10 ** 11
    A13 = a12 % 8 * 10 ** 12
    A14 = a13 % 8 * 10 ** 13
    A15 = a14 % 8 * 10 ** 14

    at = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15

    print(f'O número {n1}, na base 8, é {at}.')'''

# Resolução do caba
num = int(input('\033[93mDigite um número inteiro: '))
print('''\033[97mEscolha uma das bases para conversão:
\033[94m[ 1 ]\033[97m converter para BINÁRIO
\033[94m[ 2 ]\033[97m converter para OCTAL
\033[94m[ 3 ]\033[97m converter para HEXADECIMAL''')
opção = int(input('\033[93mSua opção: '))
if opção == 1:
    print(f'\033[97m{num} convertido para BINÁRIO é igual a \033[96m{bin(num)[2:]}')
elif opção == 2:
    print(f'\033[97m{num} convetido para OCTAL é igual a \033[96m{oct(num)[2:]}')
elif opção == 3:
    print(f'\033[97m{num} convertido para HEXADECIMAL é igual a \033[96m{hex(num)[2:]}')
else:
    print('\033[91mOpção inválida, tente novamente.')
