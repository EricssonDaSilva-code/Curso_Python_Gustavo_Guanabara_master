"""
 Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
 Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\n\033[31mERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[031mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
