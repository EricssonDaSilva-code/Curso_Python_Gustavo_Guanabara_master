"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""
def ficha(name = 'unknow', gols = 0):
    """
    -> Faz uma ficha de um jogador:
    :param name: Recebe o nome do jogador
    :param gols: Recebe o número de gols
    :return: sem retorno
    """
    print(f'O jogador {name} fez {gols} gols no campeonato.')


#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)







