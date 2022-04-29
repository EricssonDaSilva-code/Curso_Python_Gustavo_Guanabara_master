''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

n1 = int
n2 = int
menu = int
result = int
while menu != 5:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    menu = int(input('Escolha uma opção:\n1-somar\n2-multiplicar\n3-maior\n4-novos números\n5-sair\n==>'))
    if menu > 5 or menu < 0:
        print('Escolha uma opção válida!')
    elif menu == 1:
        result = n1 + n2
        print(f'O resulto da soma entre {n1} e {n2} é igual a {result}')
    elif menu == 2:
        result = n1 * n2
        print(f'O resultado da multiplicação de {n1} por {n2} é igual a {result}')
    elif menu == 3:
        if n1 > n2:
            result = n1
        else:
            result = n2
        print(f'O maior número é {result}')
    elif menu == 4:
        n1 = int
        n2 = int
print('Fim do programa')
