'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''

"""

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
"""

a = int(input('Valor do primeiro lado: '))
b = int(input('Valor do segundo lado: '))
c = int(input('Valor do terceiro lado: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Os lados podem formar um triângulo. ')
    if a == b and a == c and c == b:
        print('Os lados formam um triangulo equilatero. ')
    elif a != b and a != c and c != b:
        print('Os lado formam um triangulo escaleno. ')
    else:
        print('Os lados formam um triangulo isósceles')
else:
    print('Os lados não podem formar um triângulo. ')
print('FIM')