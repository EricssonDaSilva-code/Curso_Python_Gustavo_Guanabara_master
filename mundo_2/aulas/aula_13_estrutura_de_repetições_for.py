"""
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro
o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)
"""
#Estrutura de controle
#laços, repetições ou iterações
"""
for é um laço de repetição (laço com variavel de controle) que segue a repetição o número de vezes que escremos.

for c in range(1, 10):
    passo
pega

for c in range(1, 3):
    passo
    pula
passo
pega

for c in range(1, 3):
    if moeda
        pega
    passo
    pula
passo
pega
"""
for c in range(0, 10):                      #c é a variavel de controle, ele sempre desconsidera o ultimo número;
    n = int(input('Digite um número: '))    #nesse caso o 0 conta como 1, ele para no 9 e fecha 10 vezes a variavel n
print(n)

#oi 6 vezes
"""
for c in range(1, 6):
    print('oi')
print('FIM')
executado:
oi
oi
oi
oi
oi
FIM
"""
#mostrando sequencia de números de 0 à 5, ele para um digito antes do fim
"""
for c in range(0, 6):
    print(c)
print('FIM')
executado:
0
1
2
3
4
5
FIM
foi de 0 até 5
"""
#sequencia de traz pra frente
"""
for c in range(6, 0, -1):      contando para traz, começando do 6 e retirando um até 1
    print(c)
print('FIM')
executado:
6
5
4
3
2
1
FIM
"""
#trocando o número final por uma entrada dada pelo usuario
"""
n = int(input('Digite um número: '))
for c in range(0, n+1):   escolhendo 6 
    print(c)
print('FIM')
executado:
0
1
2
3
4
5
6
FIM
"""
#inicio, fim e o passo, todos entradas pelo usuario
"""
i = int(input('INICIO : '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
"""
#somando números
"""
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório dos número é igua a {}'.format(s))
print('FIM')
"""