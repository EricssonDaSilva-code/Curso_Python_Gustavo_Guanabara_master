'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import choice


print('JO KEN PO')
use = input('Escolha sua opção:\n-PEDRA\n-PAPEL\n-TESOURA\n==>').upper()
list = 'PEDRA', 'PAPEL', 'TESOURA'
com = choice(list)

if com  == 'PAPEL' and use == 'PEDRA':
    print('Você escolheu {} e o computador escolheu {}, você perdeu'.format(use, com))
elif com == 'TESOURA' and use == 'PAPEL':
    print('Você escolheu {} e o computador escolheu {}, você perdeu'.format(use, com))
elif com == 'PEDRA' and use == 'TESOURA':
    print('Você escolheu {} e o computador escolheu {}, você perdeu'.format(use, com))
elif use == 'PAPEL' and com == 'PEDRA':
    print('Você escolheu {} e o computador escolheu {}, você venceu!'.format(use, com))
elif use == 'TESOURA' and com == 'PAPEL':
    print('Você escolheu {} e o computador escolheu {}, você venceu!'.format(use, com))
elif use == 'PEDRA' and com == 'TESOURA':
    print('Você escolheu {} e o computador escolheu {}, você venceu!'.format(use, com))
else:
    print('Você escolheu {} e o computador escolheu {}, deu empate'.format(use, com))
print('FIM')







