'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''

cont = ''
num = int
list = []
list_imp = []
list_par = []
while True:
    num = int(input('Digite um número: '))
    list.append(num)
    if num % 2 == 0:
        list_par.append(num)
    else:
        list_imp.append(num)
    cont = str(input('Continuar? [S/N]')).strip().upper()
    if 'N' in cont[0]:
        break
print(f'Os números na ordem digitada {list}')
print(f'Os números na ordem crescente {sorted(list)}')
print(f'Pares {list_par}')
print(f'Ímpares {list_imp}')
