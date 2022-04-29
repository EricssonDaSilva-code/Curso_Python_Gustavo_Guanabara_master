# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite o valor do salário: '))
aum = (sal/100) * 15
tot = sal + aum
print('O salario atual R${} mais o aumento de R${:.2f} resulta no total de R${:.2f}'.format(sal, aum, tot))
