'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o nú-
mero a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.'''

#Minha resolução
'''def fatorial(x,show=False):
    """
--> Calcular o fatorial de um número
    :param x: O número a ser calculado
    :param show: Mostrar o não como foi feita a conta
    :return: O valor do fatoria de um número x
    """
    print('-' * 30)
    fac = 1
    print(f'{x}! = ',end = '')
    if show:
        for c in range(x,0,-1):
            fac *= c
            print(f'{c}', end = ' x ' if c > 1 else ' = ')

    else:
        for c in range(x,0,-1):
            fac *= c
    return fac


print(fatorial(5))
print('-' * 30)
help(fatorial)'''

#Resolução do vídeo
def fatorial(n, show = False):
    '''
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

print(fatorial(5, show = True))
help(fatorial)