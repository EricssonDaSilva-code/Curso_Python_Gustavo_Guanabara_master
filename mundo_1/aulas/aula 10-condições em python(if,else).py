#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus
# programas em Python.

#Condições são caminhos que podemos seguir ou como colocar um programa simples dentro de um programa

"""tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo.')
else:
    print('Carro velho. ')
print('FIM.')
"""

#condição simplificada

"""tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
print('FIM.')
"""

#Pratica:

"""nome = str(input('Qual é o seu nome? ')).strip().title().split()[0]
if nome == 'Ericsson':
    print('Que nome lindo você tem!'.)
else:
print('Seu nome é tão normal.')
print('Bom dia {}'.format(nome))
"""

"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Parabéns!'.upper())
else:
    print('Estude mais!'.upper())
"""