''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''

frase = str(input("Palíndromo: \n")).upper()
frase = "".join(frase.split(" "))
print("A palavra {} ao contrário é {} e ".format(frase, frase[::-1]), end="")
if frase == frase[::-1]:
    print("é um palíndromo.".format(frase))
else:
    print("não é um palíndromo.".format(frase))