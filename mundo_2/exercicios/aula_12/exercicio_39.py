'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''

from datetime import date
nasc = int(input('Digite o ano de seu nascimento: '))
cal = date.today().year
idade = cal - nasc
if idade == 18:
    print('Você tem 18 anos, este é o ano de seu alistamento. ')
elif idade < 18 and idade > 0:
    print('Faltam {} anos para o alistamento, ele ocorrera em {}. '.format(18 - idade, nasc + 18))
elif idade > 18:
    print('Passou o seu tempo de se alistar, isso ocorreu há {} anos. '.format(idade - 18))
elif idade <= 0:
    print('Você ainda esta no saco do teu pai. ')
print('FIM.')


