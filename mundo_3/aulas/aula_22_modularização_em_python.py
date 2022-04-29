"""
 Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos.
 Vamos aprender também como agrupar vários módulos em um pacote,
ampliando ainda mais a modularização em grandes projetos em Python.
"""

#Módulos e pacotes
"""
 O ato de construir módulos, surgiu no início da década de 60 com os sistemas ficando cada vez maiores.
 Foco principsl é dividir um programa grande em varias partes menores e aumentar a legibilidade com isso
facilitando a a manutenção do sistema.
 Para usar os módulos se usa o mesmo comando que usamos até o momento para importar bibliotecas, 
 import + o que se quer
"""
from uteis import numeros


num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')

"""
 Vantagens de se fazer a modularização:
 Organização
 Facilita a manutenção
 Ocultação de código detalhadio
 reutilização em outros projetos
"""
#pacotes: quando os módulos não sõa o suficiente para mantes a organização
"""
 É uma pasta que contem módulos, importa-se da mesma maneira
 como criar:
 basta criar uma pasta package.py com o nome que ser quer e assim separar por tipos de utilização, tratamento ou 
o que lhe convir.
"""