"""Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
 Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos
  built-in e módulos externos, oferecidos no Pypi."""

#para incluir mais funcionalidades usa-se o comando import + o nome do módulo ou biblioteca
#para incluir importações unicas usar import from + nome do módulo ou biblioteca
#exemplo:
"""math
     ceil == faz arredondamento para cima
     floor == faz arredondamento para baixo
     trunc == truncate, corta da virgula pra frente sem fazer arredondamento
     pow == power == potência
     sqrt == squareroot == raiz quadrada
     factorial == fatora
     import math ou from math import + o nome
     """
"""import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}. '.format(num, raiz))
print('A raiz de {} é igual a {}. '.format(num, math.ceil(raiz)))
"""

"""from math import sqrt, floor             #posso colocar uma virgula e importa outro módulo, exemplo: ,floor

num = int(input('Digite um número: '))
raiz = sqrt(num) #como a importação foi especifica não precisa por math. na frente
print('A raiz de {} é igual a {}. '.format(num, raiz))
#print('A raiz de {} é igual a {}. '.format(num, math.ceil(raiz))) sem importar o módulo não funciona
print('A raiz de {} é igual a {}. '.format(num, floor(raiz)))
"""
#para ver quais bibliotecas posso importar consultar bibliotecas no site python
#exemplos Guanabara:

"""import random
num = random.random() #randomiza um número entre 0 e 1
num1 = random.randint(1, 10) #randomiza os números que você escolheu (de, até)
print(num)
print(num1)
"""

#para importar bibliotecas que não estão no computador, clique na lampada vermelha onde esta sublinhado
#  escolha install package. Exemplo: não consegui importar emoji, da erro depois eu vejo isso

"""import emoji

print(emoji.emojize("Olá Mundo! :sunglasses: ", use_aliases=True))
"""

#para ver o que esta instalado ir em settings



