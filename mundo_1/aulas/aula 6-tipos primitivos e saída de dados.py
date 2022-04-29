"""Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool()
e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python."""
#Na aula anterior foi mostrado um desafio, fazer a soma entre dois números.
"""n1 = input('digite um número:')
   n2 = input('digite mais um número:')
   s = n1 + n2
   print('A soma vale',s)
Solução proposta por Guanabara
o Problema é que o código não funcionou, pois os números foram concatenados (concatenar é juntar uma string na outra), 
por que os números foram considerados
strings, adicionando a nomeclatura do tipo primitivo antes, no caso acima adicionando int antes do input, exemplo:
n1 = int(input('digite um número'))
fazendo isso ele ira entender que é um número inteiro ao invés de um texto."""
#São 4 os tipos primitivos:

# int == inteiro exmplo: 7, -4, 0, 9865
# float == numeros reais exemplo: 4.5, 0.076, -15.223, 7.0
# bool == booleanos exemplo: True and False, sempre com começo maiusculo
# str == string = texto

#usando o comando (.format)
"""print('A soma vale {}',.formar(s))"""

#exemplos Guanabara:
"""n1 = int(input('Digite um valor: '))
   n2 = int(input('digite um valor: '))
   s = n1 + n2
   print('A soma entre {} e {} vale {}'.format(n1, n2, s))
   
   n = float(input('Digite um valor: '))
   print(n)
   prynt(type(n))
   print(n.isnumeric())""" #comando(variavel.is), interessante para avalicação booleana, True or False, bom de usar com
                           # if, else, elif