'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.
   Ex: escreva("Olá, Mundo!")
    --> ~~~~~~~~~~~~~~~
          Olá, Mundo!
        ~~~~~~~~~~~~~~~'''

#Minha resolução (mosquei um pouco)
'''def linha():
    print(f'{caract[0]}' * (len(texto) + 6))

def escreva(texto):
    linha()
    print(f'{texto: ^{len(texto) + 6}}')
    linha()


texto = str(input('Escreva uma frase: ')).strip()
caract = str(input('Qual caractere deseja utilizar? ')).strip()
escreva(texto)'''

#Resolução do vídeo
def escreva(msg):
    tam = len(msg) + 6
    print('~' * tam)
    print(f'   {msg}')
    print('~' * tam)
    
escreva('Oi')
escreva('Curso de Python no YouTube')
escreva('CeV')
