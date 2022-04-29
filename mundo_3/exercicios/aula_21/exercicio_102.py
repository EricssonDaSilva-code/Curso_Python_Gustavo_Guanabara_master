"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num, show = False):
    """
    -> mostra o fatorial de um número
    :param num: numero a ser fatorado
    :param show: mostra a conta, opcional
    :return: retorna o resultado da fatorção
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


print(fatorial(5, show=True))
