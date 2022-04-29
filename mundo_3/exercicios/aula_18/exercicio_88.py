'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.

O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint
palpite = []
jogos = []
num = int(input('Quantos jogos deseja gerar?\n'))
while len(jogos) != num:
    for c in range(1, 7):
        gerador = randint(1, 60)
        if gerador not in palpite:
            palpite.append(gerador)
            if len(palpite) == 6:
                break
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
for c, v in enumerate(jogos):
    print(f'jogo {c} {v}')
