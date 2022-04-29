# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

n1 = float(input('Digite a temepratura que deseja converter para fahrenheit: '))
con = (n1 * 9/5) + 32
print('{:.1f}C° equivale à {:.1f}F° '.format(n1, con))
