''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''
n = int(input('Digite um númeor para saber sua tabuada: '))
s = 0
for c in range(1, 11):
    s = c * n
    print('{} X {} = {} '.format(n, c, s))
