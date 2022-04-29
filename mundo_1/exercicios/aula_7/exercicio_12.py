# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

price = float(input('Digite o preço: '))
desc = (price / 100) * 5
result = price - desc
print('Valor integral {:.2f}, valor com desconto {:.2f}, o desconto foi de {} . '.format(price, result, desc))
