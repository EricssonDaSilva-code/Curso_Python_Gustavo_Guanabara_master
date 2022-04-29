"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
"""

s = float(input('Digite o valor do salário: '))

if s <= 1250.00:
    a = s + (s / 10)
    print('O seu novo salário é de R$ {:.2f} reais.'.format(a))
else:
    a = s + ((s / 100)*15)
    print('O seu novo salário é de R$ {:.2f} reais. '.format(a))
