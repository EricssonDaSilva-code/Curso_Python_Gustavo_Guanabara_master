'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''

from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9 and idade >=4:
    print('Sua idade {} anos '.format(idade))
    print('Sua categoria é a mirim')
elif idade >= 10 and idade <= 14:
    print('Sua idade {} anos '.format(idade))
    print('Sua categoria é a infantil. ')
elif idade >= 15 and idade <= 19:
    print('Sua idade {} anos '.format(idade))
    print('Sua categoria é a júnior. ')
elif idade == 20:
    print('Sua idade {} anos. '.format(idade))
    print('Sua categoria é a sênior. ')
elif idade >= 21 and idade <= 90:
    print('Sua idade {} anos. '.format(idade))
    print('Sua categoria é a master. ')
else:
    print('Sua idade {} anos. '.format(idade))
    print('Você não tem idade para concorrer. ')
print('FIM.')
