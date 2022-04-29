# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza

nome1 = input('Digite um nome: ')
nome = nome1.strip().title().split()

print('Primeiro nome: {}. '.format(nome[0]))
print('Ultimo nome: {}. '.format(nome[-1]))
