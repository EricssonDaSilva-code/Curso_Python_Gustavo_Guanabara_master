'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

first_term = int(input('Digit o primeiro termo: '))
ratio = int(input('Digite a razão: '))
count = 0
while count <10:
    print(first_term, end=' ')
    first_term = first_term + ratio
    count += 1
