def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).lower().strip().replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[91mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
