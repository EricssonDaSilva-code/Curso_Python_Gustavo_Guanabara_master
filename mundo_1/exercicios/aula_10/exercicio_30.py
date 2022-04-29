"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

n_i = int(input('Digite um número: '))
if n_i % 2 == 0:
    print('{} é PAR'.format(n_i))
else:
    print('{} é ÍMPAR'.format(n_i))
print('FIM')
