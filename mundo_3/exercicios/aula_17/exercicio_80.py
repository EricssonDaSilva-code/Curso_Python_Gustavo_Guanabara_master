'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''

list = []
num = int
for c in range(0, 5):
    num = int(input('Digite um número.'))
    if len(list) == 0:
        list.append(list)
    else:
        if num > max(list):
            list.append(num)
        elif num < min(list):
            list[0].append(num)
print(list)

# Versão do Gustavo Guanabara:

lista = []
for i in range(0, 5):
    n = int(input("Digite um número: \n"))
    if i  == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
