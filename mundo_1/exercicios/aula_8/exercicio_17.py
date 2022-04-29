# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

n1 = int(input('Digite o valor do cateto oposto: '))
n2 = int(input('Digite o valor do cateto adjacente: '))
h = hypot(n1, n2)
print('A hipotenusa é {:.2f}.'.format(h))



