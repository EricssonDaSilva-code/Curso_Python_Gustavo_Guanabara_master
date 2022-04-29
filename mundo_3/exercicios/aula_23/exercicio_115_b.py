import lib
from time import sleep

from mundo_3_ericsson.exercicios.aula_23.lib.arquivo import arquivoExiste
from mundo_3_ericsson.exercicios.aula_23.lib.interface import cabeçalho, menu
from mundo_3_ericsson.exercicios.aula_23.lib.arquivo import *

#programa principal
arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
