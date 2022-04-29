"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
import random

n = random.randint(0, 5)
n_e = int(input('Digite um número entre 0 e 5: '))
if n_e < 0 or n_e > 5:
    print('Número invalido')
elif n_e == n:
    print('O número sorteado foi {}. Parabéns você acetou!'.format(n))
else:
    print('O número sorteado foi {}. Que pena você errou!'.format(n))
print('FIM')
