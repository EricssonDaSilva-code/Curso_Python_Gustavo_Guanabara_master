''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite o número que deseja coverter: '))
base = int(input('1- para binario\n2- para octal \n3- para hexadecimal\n'))
if base == 1:
    print('O número {} em binário fica {}. '.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} em octal fica {}. '.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} em hexadecimal fica {} . '.format(num, hex(num)[2:]))
else:
    print('Você não digitou uma escolha válida.')
print('FIM.')
