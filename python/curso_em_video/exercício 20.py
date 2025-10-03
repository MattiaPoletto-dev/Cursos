'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um
programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

'''from random import shuffle
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
opcoes = [n1, n2, n3, n4]
shuffle(opcoes)
print(f'A ordem dos que apresentarão o trabalho é {opcoes}')'''


from random import shuffle
n1 = str(input('\033[93mPrimeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
opcoes = [n1, n2, n3, n4]
shuffle(opcoes)
print(f'\033[97mA ordem de apresentação será: \n\033[92m{opcoes}')
