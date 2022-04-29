# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

# ex.: digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

num = input('Digite um número: ')
print('Unidade: ', num[3])
print('Dezena: ', num[2])
print('Centena', num[1])
print('Milhar: ', num[0])
