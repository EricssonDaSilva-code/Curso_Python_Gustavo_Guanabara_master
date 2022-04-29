''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date
contMaior = 0
contMenor = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    if date.today().year - nasc < 18:
        contMenor += 1
    elif date.today().year - nasc >= 18:
        contMaior += 1
print('O número de menores de idade é {} pessoas e o de maiores é {} pessoas'.format(contMenor, contMaior))

