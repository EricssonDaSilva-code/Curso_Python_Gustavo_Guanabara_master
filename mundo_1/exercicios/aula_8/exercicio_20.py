# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = ["ricardo", "algusto", "joel", "lucas", "Maria", "Joaquina", "Andrieli"]
shuffle(nomes) # não colco a lista dentro de uma variavel
print(nomes)
