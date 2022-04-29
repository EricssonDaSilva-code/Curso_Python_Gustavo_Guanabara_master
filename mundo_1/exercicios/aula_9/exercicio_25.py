# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome1 = input('Digite um nome: ')
nome = nome1.title().strip()

print('Seu nome tem Silva? {} '.format('Silva' in nome))

"""if 'Silva' in nome:
    print('O nome {} contém Silva no nome. '.format(nome))
else:
    print('O nome {} não contém Silva no nome. '.format(nome))
"""
