# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²

lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
r = (lar * alt) / 2
print('Você tem {:.2f} metros quadrados, precisara de {:.2f} litros de tinta para pinta-la '.format(lar*alt, r))

