'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

tupla = ('arroz', 30, 'feijão', 10, 'carne', 58, 'leite', 5,
         'refrigerante', 8)
print('=' * 30)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<30}{tupla[c+1]}')
