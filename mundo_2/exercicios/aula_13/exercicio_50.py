'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
for c in range(0, 6):
    n = int(input('DIgite um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares é {}'.format(s))
