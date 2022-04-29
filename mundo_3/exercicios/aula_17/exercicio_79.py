'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

num = []
con = ''
cont = int
while True:
    cont = (int(input('Digite um número:')))
    if cont in num:
        print('O número já esta na lista. ')
    else:
        num.append(cont)
    con = str(input('Continuar? [S/N]')).strip().upper()
    if con[0] == 'N':
        break
print(f'Os números digitados em ordem foram {sorted(num)}')
