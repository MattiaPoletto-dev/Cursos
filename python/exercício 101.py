'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
(idade < 16  --> Negado ;16 <= idade < 18 --> Opcional; 18 <= idade < 65 --> Obrigatório; idade >= 65 --> Opcional)'''

#Minha resolução
'''from datetime import datetime

def voto(x):
    if x < 16:
        v = 'NÃO VOTA'
        return v
    elif 16 <= x < 18 or x > 65:
        v = 'VOTO OPCIONAL'
        return v
    elif 18 <= x <= 65:
        v = 'VOTO OBRIGATÓRIO'
        return v


     #Programa principal
print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
idade = datetime.today().year - ano
p = voto(idade)
print(f'Com {idade} anos de idade: {p}')'''

#Resolução do vídeo
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

     #Programa principal
print('-' * 30)
print(voto(int(input('Em que ano você nasceu? '))))
