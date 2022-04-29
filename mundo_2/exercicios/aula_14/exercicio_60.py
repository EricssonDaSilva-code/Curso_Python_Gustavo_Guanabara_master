''' Faça um programa que leia um número qualquer e mostre
o seu fatorial

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''
from math import factorial
n1 = int
menu = int
result = int
while menu != 2:
    n1 = int(input('Digite um número para fatora-lo: '))
    print(f'{n1}! => ', end=' ')
    for c in range(n1, 0, -1):
        print(c, ' X ' if c > 1 else ' = ', end='')
    print(f' {factorial(n1)}')
    menu = int(input('Continuar?\n1-sim\n2-não\n'))
print('fim')
