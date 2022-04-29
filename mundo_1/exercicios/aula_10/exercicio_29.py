"""
''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.

"""

v = int(input('Digite a velocidade do carro: '))
mu = (v - 80)*7
if v > 80:
    print('Você estava a {}Km/h, sua multa é de R${:.2f} reais. '.format(v, mu))
else:
    print('Você esta a {}Km/h. '.format(v))
print('FIM')
