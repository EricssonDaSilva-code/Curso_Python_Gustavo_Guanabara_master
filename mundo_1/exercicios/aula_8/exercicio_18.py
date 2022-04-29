# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import sin, cos, tan

a = int(input('Digite o angulo para saber o seno, cosseno e tangente: '))
s = sin(a)
c = cos(a)
t = tan(a)
print(' seno {}\n cosseno {} \n tangente {}'.format(s, c, t))
