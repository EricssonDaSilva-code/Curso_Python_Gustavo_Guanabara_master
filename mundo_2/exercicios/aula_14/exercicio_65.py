''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

n = int
cont = 0
soma = 0
maior = int
menor = int
contin = ''
while contin != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    contin = str(input('Quer continuar [S/N] ')).strip().upper()
print(f'A média entre os {cont} numeros somados é {soma / cont:.2f}. ')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
print(soma, maior, menor, cont)
