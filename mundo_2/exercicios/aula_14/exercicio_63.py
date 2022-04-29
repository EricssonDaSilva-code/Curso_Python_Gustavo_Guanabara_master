'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''

n1 = int(input('Digite um número: '))
ultimo = 0
anterior = 0
s = 0
cont = 0
while cont < n1 - 1:
    if anterior < 1:
        anterior = 1
        ultimo = 1
        print(anterior, end=', ')
    s = ultimo + anterior
    anterior = ultimo
    ultimo = s
    cont += 1
    print(anterior, ', 'if cont < n1 -1 else '', end='')



