"""
 Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
 Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
 Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
"""
#função == rotina
"""
Usamos até agora funções que já vem com o python, exemplo:
print(), input(), len(), float()
Podemos criar funções como acima, adequadas as nossas nescessidades, exemplos:
mostraLinha() que faz: 
----------------------------------------------------------------------------------------------------

<<<< Para fazer uma função: .>>>>>>

def mostraLinha():
    print('-' * 30)

 Entre o def e o programa principal, precisa por duas linhas em branco
 
 Podemos trabalhar também com parametros, exemplo:
 
 def mensagem(msg):
    print('_' * 30)
    print(msg)
    print('_' * 30)
    
mesagem('SISTEMA DE ALUNOS')

"""

#exemplos


#Queremos somar dois números, então substituimos este exrtenso código por uma funçao:
"""
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
"""
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)



#programa principal
soma(4, 5)     # Os números dentro do parenteses são os paramnêtros
soma(8, 9)      # Se não declarar nada ele segue a função lá de cima.
soma(a=9, b=1) # Podemos deixar explicito qual a ordem dos números
soma(b=4, a=5)     # Podendo até mesmo estar de forma diferente das definidas lá em cima


#Empacotar parametros
"""
 Se quisermos fazer um contador:
 
 contador(5, 7, 3, 1, 4)
 contador(8, 4, 7)
 
 Na maioria das linguagens ele não permitem você colocar mais de um paramêtro por função, o python permite.
 Chamamos isso de empacotamento, exemplo:
 
 def contador(*núm):           O * serve para dizer que colocaremos x números, não sabemos quanto colocaremos, 
                               se ele passar um ou mil paramentros ele vai pegar tudo isso e colocar dentro de núm    

"""

def contador(*núm):
    for valor in núm:        # podemos colocar o que quisermos dentro do def, neste exemplo ele esta exibindo os números
        print(valor, end=' ') #dentro de uma tupla, vamos ver com listas


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(f'\n{valores}')



