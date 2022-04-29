"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""
from datetime import date
def voto(birthday):
    """
    Calcula a idade e diz se pode ou não votar
    :param birthday: ano de nascimento
    :return: sem retorno
    """
    current_year = date.today().year
    age = current_year - birthday
    if age < 18:
        print(f'Com {age} anos, o voto é NEGADO')
    elif age >= 18:
        print(f'Com {age} anos, o Voto é OBRIGATÓRIO')
    elif age >= 65:
        print(f'Com {age} anos o voto é OPCIONAL')



voto(2010)
