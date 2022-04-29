"""
Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
"""
import lib
from time import sleep
from mundo_3_ericsson.exercicios.aula_23.lib.interface import cabeçalho

#programa principal
while True:
    resposta = menu(['Criar Aquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)



