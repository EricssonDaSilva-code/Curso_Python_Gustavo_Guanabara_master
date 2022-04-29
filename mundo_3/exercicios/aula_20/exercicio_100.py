"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
def sorteia(a, b):
    for c in range(0, 5):
        r = randint(a, b)
        numeros.append(r)
def soma_par():
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s += c
    print(s)



numeros = []

sorteia(0, 10)
print(numeros)
soma_par()