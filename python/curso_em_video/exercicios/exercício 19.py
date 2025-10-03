'''O professor uer sortear um dos seus quatro alunos para apagar o quadro. Faça um progresso que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.'''

'''from random import choice
nome1 = str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
nome4 = str(input('Aluno 4: '))
opcoes = (nome1, nome2, nome3, nome4)
sorteado = choice(opcoes)
print(f'Entre os quatro alunos, o sorteado foi: {sorteado}')'''


from random import choice
n1 = str(input('\033[93mPrimeiro aluno: '))
n2 = str(input('Sdgundo aluno: '))
n3 = str(input('Tericeiro aluno: '))
n4 = str(input('Quarto aluno: '))
opcoes = [n1, n2, n3, n4] #lista usa-se colchetes []
sorteado = choice(opcoes)
print(f'\033[97mO aluno escolhido foi \033[92m{sorteado}')
