#Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

#Exemplo:
# frase = 'Curso em Vídeo Python'
"""Quando se coloca uma string dentro de uma variavel o python não reconhece a frase
como sendo inteira, o que ele faz é colocar cada caracter em um espaço individual, com um número atribuido
começando em 0 e contando os espaços, sendo assim a variavel acima contem 21 espaços.
"""
#fatiamento:
#print(frase[9])
"""
Se nós colocarmos o comando print(frase[9]), ele vai vai mostrar somente o decimo
caracter, já que a contagem começa em 0, na variavel frase corresponde a letra V
maiscula, já que o python diferencia maiuscula de minuscula, pegar uma letra
é a mais simples forma de fatiamento
"""
#print(frase[9:13])
"""
se colocarmos prin(frase[9:13]) ele vai pegar uma fatia maior, começando em 9 e terminado em 12, 
ele corta um número antes do número final escrito, ficando assim: Víde
"""
#print(frase[9:21:2])
"""
Pega a frase a partir do 9, e vai até o 20 de dois em dois espaços.
"""
#print(frase[:5]), frase[15:], frase[9::3]
"""
Quando não se coloca o inicio ele vai do 0 até o numero anterior,
quando não se coloca o fim ele vai do número marcado até o fim, quando se omite 
qualquer número ele toma como sendo o total 
exemplo: frase [9::3], vai do 9 até o fim pulando de 3 em 3 blocos.
"""
#Analize de string:
#len(frase)
"""
len vem de length, que significa comprimento, quando se coloca o len(frase),
ele analiza o comprimento da string, dando os 21 caracteres
"""
#frase.count('alguma letra')
"""
ele conta quantas vezes aparece determinado caracter em uma frase
frase.count('o') conta quantos (o) minusculos tem em uma frase.
frase.count('o', 0, 13), ele faz a contagem já com fatiamento, começando do 0 até 
o 12. 
"""
#frase.find('deo')
"""
ele indica onde começa um ou mais caracteres, no exexmplo acima a resposta seria
11, se você procurar por uma frase que não existe na string ele retorna o valor 
-1.
"""
#'curso' in frase
"""
Responde com True or False, existe a palavra 'Curso' na variabel frase == True
"""
#Transformação:
#frase.replace('Python', 'Android')
"""
Ele subistitui a palavra python por Android, se a palavra for maior ele ajusta a quantidade de caracteres
mas ele não muda a variavel

frase = 'Curso em Vídeo Python'
frase = frase.replace('Pyton', 'Adroid')
print(frase)

Aqui sim ele faz uma troca, se não fizer isso, quando for procuras ou contar a palavra Android ela 
não estara dentro de frase

"""
#frase.upper(), lower() e outras
"""
Coloca todas as palavras em frase em maiuculas, funciona para minusculas e afins.
Não esquecer os parenteses, upper(), lower() e outros, são métodos, veremos mais adiante a diferença
"""
#frase.captalise()
"""
Joga todas as letras para minusculas e só o primeiro caractere da string vai ficar maiusculo.
Curso em vídeo python.
"""
#frase.title()
"""
Lê palavra por palavra e coloca a primeira letra de cada palavra em maiuscula.
Curso Em Vídeo Python.
"""
#frase.strip()
"""
É comum quando alguém vai se cadastrar em um site deixar espaços em braco
no inicio e no fim de um nome por exemplo, para dar uma limpada nos espaços escedentes
no incio e no final.
"""
#frase.rstrip()
"""
De forma semelhante o rstrip(), r de right == direita, remove os espaços no final a direita, analoga
lstrip() remove os das esquerda.
"""
#Divisão:
#frase.split()
"""
ele faz uma divisão onde tem espaços, separando a frase em blocos menores
exemplo:
Curso em Vídeo Python contem 21 espaços começando do 0 ao 20 
quando se usa split ele fica separa Curso[0, 4], em[0, 1], Vídeo[0, 4], Python[0, 5]
Cada uma dessas palavras são colocadas dentro de listas.
"""
#Junção:
#'-'.join(frase)
"""
De forma analoga ao split(), o join junta as listas em uma só, no caso acima separando elas por '-'
pode ser espaço em branco também ' '.
"""
