"""Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular
 (largura e comprimento) e mostre a área do terreno
"""
def cabeçalho(titulo):
    print('-' * len(titulo))
    print(titulo)
    print('-' * len(titulo))


cabeçalho('Controle de terrenos')


def area(largura, comprimento):
    print(f'A area de um terreno {largura} x {comprimento} é igual a {largura * comprimento} m²')


largura = float(input('Largura em metros : '))
comprimento = float(input('Comprimento metros: '))
area(largura, comprimento)
