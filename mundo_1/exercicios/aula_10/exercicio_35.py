# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

# Inclusive posso dizer qual tipo de triângulo pode ser formado.
# Não deve ser difícil isso em Python.
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
else:
    print('Os lados não podem formar um triângulo. ')
print('FIM')
