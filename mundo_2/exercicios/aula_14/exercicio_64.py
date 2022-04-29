'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

n1 = int
flag = 999
cont = 0
soma = 0
while n1 != flag:
    n1 = int(input('Digite um número: '))
    soma += n1
    cont += 1
    if n1 == flag:
        soma -= flag
        cont -= 1
print(f'A quantidade de número digitados foi de {cont} numero(s). ')
print(f'A soma entre eles é de {soma}. ')
print('FIM')
