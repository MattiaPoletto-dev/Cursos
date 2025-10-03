'''Crie um programa que leia o nome completo de uma pessoa e mostre:
    1) o nome com todas as letras maiúsculas;
    2) o nome com todas as letras minúsculas;
    3) quantas letras tem ao todu (sem considerar espaços);
    4) quantas letras tem o primeiro nome.'''

'''nomeescrito = str(input('Digite seu nome completo: '))
nome = nomeescrito.strip()
nomeconv1 = nome.split(nome)
espaço = nome.count(' ')
dividido = nome.split()[0]
print('Seu nome com todas as letras maiúsculas:',nome.upper())
print('Seu nome com todas as letras minúsculas:',nome.lower())
print('Seu nome completo tem:',len(nome) - espaço,'letras')
print('Seu primeiro nome tem:',len(dividido),'letras')'''


nomeescrito = str(input('\033[93mDigite sem nome completo: '))
nome = nomeescrito.strip()
conv1 = nome.upper()
conv2 = nome.lower()
conv3 = len(nome) - nome.count(' ')
conv4 = nome.split()[0].capitalize()
conv5 = len(conv4) - conv4.count(' ')
print('\033[97mAnalisando seu nome...')
print(f'Seu nome em \033[4:97mmaiúsculas\033[0:97m é \033[92m{conv1}\033[97m')
print(f'Seu nome em \033[4:97mminúsculas\033[0:92m é \033[92m{conv2}\033[97m')
print(f'Seu nome tem ao todo \033[92m{conv3} letras\033[97m')
print(f'Seu \033[4:97mprimeiro nome\033[0:97m é \033[92m{conv4}\033[97m e ele tem \033[92m{conv5} letras\033[97m.')
