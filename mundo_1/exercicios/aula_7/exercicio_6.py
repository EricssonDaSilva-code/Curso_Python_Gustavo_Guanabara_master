# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

n1 = float(input('Digite um número: '))
duble = n1 + n1
triple = n1 + n1 + n1
square = n1**(1/2)
print('O dobro de {} é {:.2f}'.format(n1, duble))
print('O triplo de {} é {:.2f}'.format(n1, triple))
print('E a raiz quadrada de {} é {}'.format(n1, square))

