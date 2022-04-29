'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2) / 2
if me < 5.0:
    print('Sua média é de {:.1f}, reprovado. '.format(me))
elif me >= 7.0:
    print('Sua média é de {:.1f}, aprovado. '.format(me))
else:
    print('Sua média foi de {:.1f}, recuperação. '.format(me))
