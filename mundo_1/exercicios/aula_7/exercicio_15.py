# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

km = float(input('Quantos Km este carro rodou? '))
days = int(input('Por quantos dias ficou? '))
r = km * 0.15 + days * 60
print('O valor do aluguel ficou em R${} reais. '.format(r))
