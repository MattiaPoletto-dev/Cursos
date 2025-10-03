def aumentar(preco=0.0, taxa=0.0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)

def diminuir(preco=0.0, taxa=0.0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)

def dobro(preco=0.0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0.0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def linha():
    print('-' * 30)

def resumo(p,a,r):
    linha()
    print(f'{'RESUMO DO VALOR': ^30}')
    linha()
    print(f'{'Preço analisado:': <21} {moeda(p)}\n{'Dobro do preço:': <21} {dobro(p,True)}\n{'Metade do preço:': <21} {metade(p,True)}'
          f'\n{a}{'% de aumento:': <14}    {aumentar(p,a,True)}\n{r}{'% de redução:': <14}    {diminuir(p,r,True)}')
    linha()
