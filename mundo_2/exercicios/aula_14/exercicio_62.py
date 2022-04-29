'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

first_term = int
ratio = int
num_term = int
count = 0
while True:
    num_term = int(input('Digite o número de termos: '))
    first_term = int(input('Digite o primeiro termo: '))
    ratio = int(input('Digite a razão dos termos: '))
    while count < num_term:
        print(first_term, end=' ')
        first_term = first_term + ratio
        count += 1
    print()
    count = 0
    user = int(input('Mais termo? Digite 0 para encerra: '))
    if user == 0:
        break


