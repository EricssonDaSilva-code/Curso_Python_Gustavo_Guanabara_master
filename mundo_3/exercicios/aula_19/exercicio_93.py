"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

player = {}
gols = 0

player['nome'] = str(input('Nome do jogador: ')).strip().upper()
player['n° partidas'] = int(input('Numero de partidas: '))
for c in range(1, player['n° partidas'] + 1):
    player[f'partida {c}'] = int(input(f'Numero de gols na partida {c}: '))
    gols += player[f'partida {c}']
player['gols no campeonato'] = gols
for k, v in player.items():
    print(f'{k}      {v}')

#solução Guanabara:
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'     Quantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O jogador {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')

