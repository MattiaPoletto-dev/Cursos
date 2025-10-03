'''Crie um programa que tenha uma tupla única com nomes e produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

B = '\033[97m'
Ac = '\033[96m'
Verde = '\033[92m'

print(f'{Ac}-=-' * 20)
print(f'|                  {B}Cardápio do Polettão                    {Ac}|')
print(f'-=-' * 20)
tupla = ['Hambúrguer',12.50,'Cachorro quente(M)',8.50,'Cachorro quente(G)',13.00,'Pizza(P)',16.90,
         'Pizza(M)',22.50,'Pizza(G)',29.90,'Pizza(M)',38.10,'Batata frita(M)', 8.50,'Batata frita(G)', 11.00,
         'Batata frita(M)',13.90,'Regrigerante(1L)',7.00,'Refrigerante(1.5L)', 9.50]
print('\n','-' * 61)
for c in range(0,len(tupla)):
    if c % 2 == 0:
        print(f'{B} {tupla[c]:.<52}', end = '')
    else:
        print(f'{Verde}R$ {tupla[c]:>5.2f}')
print(f'{Ac}-' * 61)
