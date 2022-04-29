'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10)
         , randint(1, 10), randint(1, 10))
print(f'Valores sorteados {tupla}')
print(f'Os valores em ordem {sorted(tupla)}')
print(f'Maior valor {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
