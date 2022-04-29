''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
'''

import random

n = 0
n_e = 6
while n_e != n:
    n = random.randint(0, 5)
    n_e = int(input('Digite um número entre 0 e 5: '))
    if n_e < 0 or n_e > 5:
        print('Número invalido')
    elif n_e == n:
        print('O número sorteado foi {}. Parabéns você acetou!'.format(n))
    else:
        print('O número sorteado foi {}. Que pena você errou!'.format(n))
print('FIM')
