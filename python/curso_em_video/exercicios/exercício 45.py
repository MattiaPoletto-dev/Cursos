'''Crie um programa que faça o computador jogar "Pedra, Papel, Tesoura" com você.'''

#Minha resolução
import random
from time import sleep
print('\033[93m-=-' * 20)
print('                   \033[95mPedra, Papel, Tesoura')
print('\033[93m-=-' * 20)
sleep(1)
print('\033[97mTente me ganhar!!!')
sleep(1)
a = input('(Pressione enter para começar)')
print('3')
sleep(0.5)
print('2')
sleep(0.5)
print('1')
sleep(0.5)
print('padra')
sleep(0.75)
print('papel')
sleep(0.75)
print('e teeesoura...')
sleep(1)
print('Digite:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura')
opcao = int(input('Escolha: '))
palavras = ['pedra', 'papel', 'tesoura']
comp = random.choice(palavras)

if opcao == 1:
    print(f'\033[96mJogador   Computador\n \033[97mpedra  x  {comp}')
    sleep(2)
    if comp == 'pedra':
        print('\033[97mDeu empate, haha!')
    elif comp == 'papel':
        print('\033[91mVocê perdeu!!')
    elif comp == 'tesoura':
        print('\033[92mVocê ganhou. Parabéns!!!')
elif opcao == 2:
    print(f'\033[96mJogador   Computador\n \033[97mpapel  x  {comp}')
    sleep(2)
    if comp == 'pedra':
        print('\033[92mVocê ganhou. Parabéns!!!')
    elif comp == 'papel':
        print('\033[97mDeu empate, haha!')
    elif comp == 'tesoura':
        print('\033[91mVocê perdeu!!')
elif opcao == 3:
    print(f'\033[96mJogador   Computador\n\033[97mtesoura x  {comp}')
    sleep(2)
    if comp == 'pedra':
        print('\033[91mVocê perdeu!!')
    elif comp == 'papel':
        print('\033[92mVocê ganhou. Parabéns!!!')
    elif comp == 'tesoura':
        print('\033[97mDeu empate, haha!')
