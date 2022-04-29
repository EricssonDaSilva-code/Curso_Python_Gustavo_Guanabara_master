'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''
# meu nome é gambi gambiarra
matrizA = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = int
for i in range(0, 3):    # para cada linha
    for j in range(0, 3):# para cada coluna em cada linha
        matrizA[i][j] = (int(input(f'Digite um número para {i} {j}.\n')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matrizA[i][j]:^5}', end='')
    print()
par = 0
col3 = 0
for i in range(0, 3):
    for j in range(0, 3):
        num = matrizA[i][j]
        if num % 2 == 0:
            par += num
print(f'Soma de todos os pares {par}.')

for i in range(0, 3):
    num2 = matrizA[i][j]
    num2 += num2
print(f'Soma dos números da terceira coluna {num2}')

num3 = 0
for j in range(0, 3):
    if matrizA[i][j] > num3:
        num3 = matrizA[i][j]

print(f'O maior valor da segunda linha {num3}')