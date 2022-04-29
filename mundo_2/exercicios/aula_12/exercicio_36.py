'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

valor = int(input('Digite o valor da casa. '))
salario = int(input('Digite qual o seu sálario: '))
tempo = int(input('Em quantos anos vai pagar: '))
prestacao = valor / (tempo*12)

if prestacao > (salario / 100) * 30:
    print(f'A pretação ficou em R${prestacao:.2f} ultrapassou 30% do seu sálario, tente novamente com um tempo maior. ')
elif prestacao <= (salario / 100) * 30:
    print(f'A prestação ficou em R${prestacao:.2f}, compra aprovada, parabéns.')