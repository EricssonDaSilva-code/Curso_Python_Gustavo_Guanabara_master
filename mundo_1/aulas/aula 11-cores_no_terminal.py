"""
Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para
configurar cores para os seus programas em Python.
 Veja como utilizar o código \033[m com todas as suas principais possibilidades.
"""

#ANSI - escape sequence
"""
Código ANSI começa sempre com \e um código, (\) signifa em muitas linguagens escape.
Código ANSI para as cores é (\)e um número, o que melhor se adequa em python é 033, 
\033[  m(vamos preencher o espaço entre o conchete e o (m) com um códgio), esse código pode ser nenhum
código, 1, 2 ou 3 códigos.
"""
#style = comportamento, estilo da fonte => normal, negrito, italico(0, 1, 4, 7)
"""
0 => \033[0:0:0m
1 => BOLD
4 => underline
7 => Negative
"""
#text = óbvio => cor do texto (de 30 até 37)
#back = background ou seja cor de fundo (de 40 a 47)

nome = 'Ericsson'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;30m'}

print('{}Olá Mundo! \n'.format(cores['azul']))
print('muito prazer em te conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('\033[31;1;42mOlá Mundo!\033[m')

a = 'curso de python no cursoemvideo'
print(a[:5])
s = 'prova de python'
print(len(s))



