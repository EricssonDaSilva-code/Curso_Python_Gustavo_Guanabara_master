"""Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência
dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão,
 exponenciação e quociente na linguagem Python."""

#na aula passada:
"""n1 = int(input('Digite um valor: '))
   n2 = int(input('digite um valor: '))
   s = n1 + n2
   print('A soma entre {} e {} vale {}'.format(n1, n2, s))"""

#operadores aritméticos
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // Divisão inteira = ou seja sem fração
# % resto da divisão = ou seja o que sobrou da divisão inteira

#exemplo:
"""n = 23 // 8
n2 = 23 % 8
n3 = 23 / 8
print(n, n2, n3)"""

#Ordem de Procedência
# 1 (), o que estiver dentro do parenteses
# 2 **, exponenciação
# 3 *, /, //, %, depois dos outros dois o que vier nessas ordem
# 4 + e -, por ultimo adição e subtração não nescessariamnete nessa ordem

#exemplo:
"""5 + 3 * 2 == 11
   3 * 5 + 4 ** 2 == 31
   3 * ( 5 + 4 ) ** 2 == 243
   pow(4,3). com essa função ele perde a ordem de precedencia, existem outras funções
   como raiz quadrada também
   
   81**(1/2), ele força a raiz quadrada potencializando por 1/2(meio)
   funciona com raiz cubicas e outras, basta substituir o 2 pelo número desejado
   
   127**(1/3), raiz cubica
   
   'oi' + 'olá == oiolá
   'oi' * 5 == oioioioioi
    da para multiplicar textos
   
    prin('='*20)
    nome = input('Qual é o seu nome? ')
    print('prazer em, te conhecer {}!'.format(nome))
    colocando dentro das chaves {}, dois pontos :, conseguese alterar o texto
    exemplo:"""
    #{:20} ele coloca o texto em 20 caracteres, completando com espaços
    #{:>20} é alinhado a direira com 20 espaços
    #{:<20} é alinhado a esquerda com 20 espaços
    #{:^20} centralizado com 20 espaços
    #{:=^20} centralizado com 20 sinais de iguais, 10 de casa lado

"""n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
print('A divisão é {:.3f}'.format(d)) """
#resultado:
"""A soma é 7, o produto é 12 e a divisão é 1.3333333333333333
   Divisão inteira 1 e potência 64
   Se eu quiser o resultado da divisão só com duas casas == {:.3f} 3 casas decimais flutuantes
   pode-se diminuir as casas para 2 ou 1. 
   
   o resultado do print aparece quebrado no exemplos acima, para juntar todos na mesma linha basta por uma virgula
   depois do () do .format e escrever end=' '  (ou seja e em branco), para quebrar a linha (\n)
   Exemplo:
   
   print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ')
   print('Divisão inteira {} e potência {}'.format(di, e))"""




