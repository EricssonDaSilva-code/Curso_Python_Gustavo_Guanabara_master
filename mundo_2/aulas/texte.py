"""s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos número é igua a {}'.format(s))
print('FIM')
"""
"""
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
"""
"""
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuras [S/N]?')).upper().strip()
print('FIM')
"""
"""n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    elif n % 2 != 0:
        impar += 1
print(f'Você digitou {impar} número impares e {par} números pares:  ')
"""

ist = ['Ana', 'Alice', 'Abel']
valor = max(ist, key=len)
print(valor)

