# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

nomes = 'ricardo', 'algusto', 'joel', 'lucas', 'Maria', 'Joaquina', 'Andrieli'
r = choice(nomes)
print('O aluno escolhido foi {}.'.format(r))
