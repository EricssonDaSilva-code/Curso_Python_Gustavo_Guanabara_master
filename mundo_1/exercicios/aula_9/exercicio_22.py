# Crie um programa que leia o nome completo de uma pessoa:
nome = input('Digite um nome: ')

# O nome com todas as letras maiúsculas
print('Maiúsculas: ', nome.upper())

# O nome com todas minúsculas
print('Minúsculas: ', nome.lower())

# Quantas letras ao todo (sem considerar espaços)
print('Contagem: ', len(nome))

# Quantas letras tem o primeiro nome:
dividido = nome.split()
print('Letras do Primeiro nome: ', len(dividido[0]))
