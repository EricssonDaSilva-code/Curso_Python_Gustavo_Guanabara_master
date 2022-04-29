"""
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores
 em uma mesma estrutura, acessíveis por chaves individuais.
"""
#variavel simples
"""
lanche = hambrguer
lanche = suco    esse substitui o hamburguer e pôe suco
"""
#tuplas
"""
lanche = hamburguer, suco, pizza, pudim
indice ==     0        1     2      3
assim como manipular uma string
print(lanche[2]) mostra a pizza
print(lanche[0:2]) mostra do hamburguer até a pizza, assim como no fatiamento o python exclui o ultimo número.
print(lanche[1:])  mostra do suco até o fim
print(lanche[-1]) mostra o pudim que é o ultimo, lendo de traz para frente.
len(lanche)   vai dizer quantos elementos tem em lanche.
for c in lanche:  não existe a variavel c, então o python cria um bloco e armazena um item    
    print(c)      como é repetição, ele mostra todos de um em um.            
"""
# AS TUPLAS SÃO IMUTÁVEIS: LEMBRE-SE DISSO
"""
Se quisermos substituir qualquer intem da tupla, não tem como alterar dentro do programa
como fizemos com as outras variaveis.
n = int
n = str
"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[:2])
print(sorted(lanche)) #sorted organiza o a tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(f'Comi pra caramba!')
for cont in range(0, len(lanche)):
    print(lanche)  # assim ele mostra as posições de cada lanche
    print(f'eu vou comer {lanche[cont]} na posição {cont}') #assim ele mostra lanche na posição cont
for pos, comida in enumerate(lanche):    #enumerate da tanto o dado comida e a posição pos, primeiro item no for
    print(f'Eu vou comer {comida} na posição {pos}') #posição e depois o item da posição

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(4)) #propriedade index do objeto tupla, mostra em qual posição esta o item

pessoa  = ('gustavo', 39, 'm', 99.88) #pode-se por varios tipos de dados na tupla, str e int.
del(pessoa)  #tuplas são imitaveis mas pode-se apagar da memoria, mas não pode deletar um item apenas toda a tupla
print(pessoa)

