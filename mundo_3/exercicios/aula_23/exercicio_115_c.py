"""
Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
"""

import lib
from time import sleep

from mundo_3_ericsson.exercicios.aula_23.lib.arquivo import arquivoExiste
from mundo_3_ericsson.exercicios.aula_23.lib.interface import *
from mundo_3_ericsson.exercicios.aula_23.lib.arquivo import *
from mundo_3_ericsson.exercicios.aula_23.lib.arquivo import cadastrar

#programa principal
arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
        cadastrar()
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = leiaInt('Idade')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
