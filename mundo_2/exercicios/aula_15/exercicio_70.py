'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
total = count = lower = count2 = 0
lower_nam = ''
while True:
    na_pro = str(input('Digite o nome do produto: '))
    pri_pro = float(input('Digite o preço do produto: '))
    total += pri_pro
    if pri_pro > 1000:
        count += 1
    elif count2 == 0:
        lower = pri_pro
        lower_nam = na_pro
    elif count2 > 0 and pri_pro < lower:
        lower = pri_pro
        lower_nam = na_pro
    count2 += 1
    print(lower_nam, lower)
    continues = str(input('Deseja continuar? [S/N]')).strip().upper()
    continues2 = continues[0]
    if 'N' in continues2:
        break
print(f'O total gasto nessa compra é de R${total:.2f} reais. ')
print(f'{count} produtos custam mais de R$ 1.000,00 reais. ')
print(f'O nome do produto mais barato é {lower_nam}. ')
