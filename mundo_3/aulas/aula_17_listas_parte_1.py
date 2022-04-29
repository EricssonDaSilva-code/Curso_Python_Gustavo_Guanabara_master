"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.
"""
#listas [] == podem ser modificadas, isto é, podem sofrer alterações enquanto o programa roda.
"""
lanche = ['hambuerguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picole'
lanche.append('biscoito')
lanche.insert(0, 'cachorro quente')

para isso usa-se o método .append('biscoito'), adicionando o elemento no final por padrão.

para adicionar em qualquer outro local da usa-se o método .insert(0, 'cachorro quente'),
 onde zero é a posição em que queremos colocar

Para apagar pode-se usar um comando, que não é um método, del lanche[3]
O método lanche.pop(3) == normalmente ele é usado para excluir o ultimo elemento mas pode-se passar como PARAMENTRO
 o elemento, no caso do exemplo, elemento 3
 
Método .remove('pizza') == nesse aqui não se apaga pelo valor, mas sim pelo indice

if 'pizza' in lache:
    lanche.remove('pizza')

valores = list(range(4, 11))
    ficando valores 4, 5, 6, 7, 8, 9, 10
                    0  1  2  3  4  5  6
                    
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()             == organiza eles em ordem crescente
valores.sort(reverse=True) == organiza eles pelo inverso
"""

#num = (2, 5, 9, 1)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.remove(2)   # ele varre a lista e apaga o primeiro elemento 2 que encontra
print(num)
print(f'Essa lista tem {len(num)} elementos.')

#duas formas de criar uma lista == valores = [], assim e assim valores = list(): assim como tuplas
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end=' ')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a
b = a[:]                 #aqui ele cria uma cópia, b recebe todos os elementos de a e não a
#b[2] = 8                #aqui ele modifica o elemento 2 nas duas listas,criando uma ligação, para poder copiar uma lista
print(f'lista {a}')
print(f'lista {b}')
