"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""

from datetime import date
worker = {}
while True:
    worker['nome'] = str(input('Nome: ')).strip().title()
    worker['nascimento'] = int(input('Ano de nascimento: '))
    worker['ctps'] = int(input('Número da carteira de trabalho: '))
    worker['idade'] = date.today().year - worker['nascimento']
    ctps = str(worker['ctps'])
    if len(ctps) != 8:
        while len(ctps) != 8:
            print('Digite um número válido: ')
            worker['ctps'] = int(input('Número da carteira de trabalho: '))
            ctps = str(worker['ctps'])
    elif worker['ctps'] != 0:
        worker['ano de contratação'] = int(input('Ano de contratação: '))
        worker['salario'] = float(input('Sálario: '))
        worker['ano de aposentadoria'] = worker['ano de contratação'] + 35
        worker['idade de aposentadoria'] = worker['ano de aposentadoria'] - worker['nascimento']
    break
print('-=' * 30)
for k, v in worker.items():
    print(f'  - {k}                     {v:.>10}')

