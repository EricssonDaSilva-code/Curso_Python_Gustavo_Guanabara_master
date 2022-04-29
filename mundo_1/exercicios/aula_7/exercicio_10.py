# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

c = float(input('Digite quanto dinheiro você tem na carteira: '))
dol = c / 3.27
print('Com {} reais você pode comprar {} dolares. '.format(c, dol))
