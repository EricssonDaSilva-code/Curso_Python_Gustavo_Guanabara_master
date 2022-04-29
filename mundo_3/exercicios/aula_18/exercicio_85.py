'''
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares
em ordem crescente.
'''
temporario = int
numeros = []
pares = []
impares = []
for c in range(0, 7):
    temporario = int(input('Entre com um número: '))
    if temporario % 2 == 0:
        pares.append(temporario)
        print(pares)
    else:
        impares.append(temporario)
        print(impares)
sorted(pares)
sorted(impares)
print(pares, impares)
numeros.append(pares[:])
numeros.append(impares[:])
print(numeros)
pares.clear()
impares.clear()
print(f'Pares {sorted(numeros[0])}\nimpares {sorted(numeros[1])}')
