"""Primeira coisa em python, os dados tem delimitadores especias, por exemplo:
em uma mensagem usa-se aspas simples ('') dentro de parenteses, isso para por um texto
print('mensagem'), resultado da string, mensagem
Já para calculos não se usa as aspas
print(5+7), resultado do cálculo, 12
Ambos são funções de print, mas no caso de cima é apresentado apenas um texto e no de baixo uma ação de soma
print('7'+'4'), nesse caso ele interpreta que os dois são strings e juntam os dois, com resultado sendo 74"""

#no python toda Variavel é um objeto
#Toda variavel pode receber valores, sinal de (=) equivale a recebe, igual em pyhton é (==), dois iguais
nome = 'guanabara'
idade = '25'
peso = '75.8'
print(nome, idade, peso)
#para entradas usar input
name = input('Qual é o seu nome?')
age = input('Qual sua idade?')
weight = input('Qual o seu peso?')
print(name, age, weight)
print('O seu nome é {}, sua idade é {} anos e seu peso é {}KG'.format(name, age, weight))

