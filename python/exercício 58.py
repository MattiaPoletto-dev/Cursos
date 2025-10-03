'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários oara vencer.'''

'''from random import randint
print('\033[95m-=-' * 20)
print('|                \033[97mAcerte que número escolhi                 \033[95m|')
print('-=-' * 20)

num = randint(1,10)
tent1 = int(input('\033[97mEscolha um número (de 1 a 10): '))
if tent1 == num:
    print('\033[92mParabéns, você acertou na 1ª tentativa!!!')
else:
    tot2 = 1
    n = -1
    while n != num:
        n = int(input('\033[97mTente novamente: '))
        tot2 += 1
    if tot2 < 4:
        print(f'\033[92mVocê acertou na {tot2}ª tentativa!!!')
    elif tot2 > 3 and tot2 < 8:
        print(f'\033[93mVocê acertou na {tot2}ª tentativa!!')
    elif tot2 < 11 and tot2 > 7:
        print(f'\033[91mVocê acertou na {tot2}ª tentativa!')'''

from random import randint
print('\033[97mSou seu computador...\nAcabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar qual foi?')
numero = randint(1,9)
palp1 = int(input('\033[96mQual é seu palpite? '))
tot1 = 1
while palp1 != numero:
    tot1 += 1
    if palp1 > numero:
        palp1 = int(input('\033[96mMenos\033[97m... Tente mais uma vez. '))
    else:
        palp1 = int(input('\033[96mMais\033[97m... Tente mais uma vez. '))
if tot1 == 1:
    print('\033[92mParabénss!! Você acertou de primeira.')
elif 1 < tot1 < 6:
    print(f'\033[97mParabéns! Você acertou na {tot1}ª tentativa')
elif 5 < tot1 < 9:
    print(f'\033[93mVocê acertou na {tot1}ª tentativa.')
elif tot1 == 9:
    print(f'\033[91mVocê acertou na 10ª tentativa.')
