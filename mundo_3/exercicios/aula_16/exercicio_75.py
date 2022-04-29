'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'O número nove apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número três apareceu pela primeira vez na posição {num.index(3)}')
for item in num:
    if item % 2 == 0:
        print(f'Os números pares são {item}', end=',')

