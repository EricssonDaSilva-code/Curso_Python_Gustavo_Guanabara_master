'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

num = []

for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
num = sorted(num)
print(num)
print(f'O maior número é o {max(num)} na posição {num.index(max(num))}')
print(f'O menor número é o {min(num)} na posição {num.index(min(num))}')
