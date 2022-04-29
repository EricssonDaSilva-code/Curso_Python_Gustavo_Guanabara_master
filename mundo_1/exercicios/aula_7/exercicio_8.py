# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

v = float(input('Escreva um valor para converter: '))
c = v * 100
mm = v * 1000
print('O valor de {} metros equivale à {} cm'.format(v, c))
print('O valor de {} metros equivale à {} mm '.format(v, mm))
