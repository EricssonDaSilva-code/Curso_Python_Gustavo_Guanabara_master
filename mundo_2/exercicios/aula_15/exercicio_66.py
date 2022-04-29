''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''
s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        r = str(input('Quer parar? [S/N]')).strip().upper()
        if r == 'S':
            s -= 999
            cont -= 1
            break
        else:
            s += n
            cont += 1
    s += n
    cont += 1
print(f'Foram digitados {cont} numeros. ')
print(f'A soma entre eles é {s}')
