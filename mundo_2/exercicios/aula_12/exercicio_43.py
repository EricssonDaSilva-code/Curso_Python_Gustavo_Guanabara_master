'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
from math import ceil
peso = float(input('Digite seu peso: '))
alt = float(input('Dgite sua altura: '))
imc = peso / alt ** 2
if imc >= 18.5 and imc <= 25:
    print('Seu IMC é {}, peso ideal: '.format(imc.__ceil__()))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {}: sobrepeso. '.format(imc.__ceil__()))
elif imc > 30 <=40:
    print('Seu IMC é {}: obesidade. '.format(imc.__ceil__()))
elif imc > 40:
    print('Seu IMC é {}: obesidade mórbida. '.format(imc.__ceil__()))
elif imc < 18.5:
    print('Seu IMC é {}: abaixo do peso. '.format(imc.__ceil__()))
print('FIM.')
