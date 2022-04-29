"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""
from operator import itemgetter
from random import randint

jogo = {}
ranking = []
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'O {k} tirou {v}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' ==Ranking dos jogadores== ')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}')



