# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção inteira.
from math import trunc

nr = float(input('Digite um número real: '))
r = trunc(nr)
print('A parte inteira de {} é {}. '.format(nr, r))

