"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

"""
"""from calendar import isleap

year = int(input('Digite o ano para saber se é bissesto: '))
year_s = coverted_year = str(year)  #função para converter um inteiro em uma string

if len(year_s) < 4:
    print('Digite um ano válido e tente novamente.')
elif isleap(year):
    print('{} é um ano bissesto. '.format(year))
else:
    print('{} não é um ano bissesto. '.format(year))
print('FIM do programa')
"""
from datetime import date

ano = int(input('Digite o ano para saber se é bissesto, digite 0  para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissesto. '.format(ano))
else:
    print('O ano de {} não é bissesto. '.format(ano))
