'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''

list = []
next = ''
while True:
    list.append(int(input('Digite um número: ')))
    next = str(input('Continuar? [S/N]')).strip().upper()
    if 'N' in next[0]:
        break

print(f'O total de números digitados é {len(list)}. ')
print(f'A lista de forma decrescente {sorted(list, reverse=True)}')
if 5 in list:
    print(f'O valor 5 foi digitado e esta na lista')
else:
    print('O valor 5 não foi digitado. ')
