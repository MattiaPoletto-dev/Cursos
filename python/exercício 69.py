'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
     A)Quantas pessoas tem mais de 18 anos
     B)Quantos homens foram cadastrados
     C)Quantas mulheres tem menos de 20 anos.'''

cont1 = cont2 = cont3 = 0
while True:
    print('\033[96m-' * 39)
    print('|         \033[97mCadastre uma pessoa         \033[96m|')
    print('-' * 39)
    idade = int(input('\033[97mIdade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    while sexo not in 'mf' or sexo == '':
        sexo = str(input('\033[93mSexo [M/F]: ')).strip().lower()[0]
    if idade > 18:
        cont1 += 1
    if sexo == 'm':
        cont2 += 1
    if idade < 20 and sexo == 'f':
        cont3 += 1
    o = str(input('\033[97mDeseja continuar [S/N]? ')).strip().lower()[0]
    while o not in 'sn' or o == '':
        o = str(input('\033[93mDeseja continuar [S/N]? ')).strip().lower()[0]
    if o == 'n':
        break
print('\033[96m-' * 39)
print(f'\033[97mSegundo os dados cadastrados, tem-se:\nPessoas com mais de 18 anos  : \033[96m{cont1}\n'
      f'\033[97mHomens cadastrados           : \033[96m{cont2}\n\033[97mMulheres com menos de 20 anos: \033[96m{cont3}')
