# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
s = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s = s + c
        print(c)
print('A somda dos número ímpares muliplos de 3, no intervalo de 1 a 500 é {}'.format(s))

