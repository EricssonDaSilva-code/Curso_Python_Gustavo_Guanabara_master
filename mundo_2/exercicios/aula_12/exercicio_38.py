'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro valor é o maior. ')
elif num2 > num1:
    print('O segundo valor é o maior. ')
else:
    print('Não existe valor maior; os dois são iguais. ')
print('FIM.')
