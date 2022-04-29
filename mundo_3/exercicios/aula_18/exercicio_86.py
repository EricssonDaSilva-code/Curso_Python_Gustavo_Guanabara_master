'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
'''
"""
matriz = []
num = []
for c in range(0, 9):
    num.append(int(input('Entre com o número: ')))
    matriz.insert(c, num[:])
    num.clear()
print(matriz[0], matriz[1], matriz[2])
print(matriz[3], matriz[4], matriz[5])
print(matriz[6], matriz[7], matriz[8])
"""
matrizA = []
matrizB = []

for i in range(0, 3):    # para cada linha
    for j in range(0, 3):# para cada coluna em cada linha
        matrizB.append(int(input(f'Digite um número para {i} {j}.\n')))
    matrizA.append(matrizB[:]) #copia a lista
    matrizB.clear()

for l in matrizA:
    print(l)
