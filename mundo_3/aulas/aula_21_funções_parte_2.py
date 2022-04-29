"""
 Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções,
argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
"""

#topicos :
#==> interactive help
#==> docstrings
#==>Argumentos opcionais
#==>Escopo de variáveis
#==>Retorno de resultados


# 1° tópico: #==> interactive help ==> help()
"""
 A ajuda interatica (interactive help), é uma função do python para poder-mos ver como funciona cada função, ou
o que desejar-mos usar no python:
 Para usa-lo basta abrir o python console e digitar help(), usando quit se sai do help().
 Outra maneira é dentro do aquivo colocar exemplo: help(input()), vai retornar o que é e o que faz a função input.
 Outra maneira seria imprimir o doc do comando==> print(input.__doc__)
 
"""

# 2° Tópico ==> docstrings:
"""
 Uma docstring é basicamente uma string de documentação, um manual dos comandos e funções.
 Nós também temos que fazer nossas próprias docstring, sobre as funções, códigos que criamos, para criarmos docstrings
basta colocarmos 3 aspas duplas depois do nome da função, exemplo:
 



def contador(i, f, p):
"""
"""
    -> Aqui no meio, tudo o que for escrito vira docstring
    -> fa uma contagem de i até f, usando p de passo.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada por Gustavo Guanabar do canal CursoemVídep
    """
"""
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(2, 10, 2)
"""

# 3° Tópico ==> Argumentos opcionais ==
"""
def somar(a, b, c)
    s = a + b + c
    print(f'A soma de vale{s}')
    
    
    
somar(3, 2, 5)
somar(8, 4) se deixarmos os paramentros não definidos lá em cima na definição da função, é obrigatório o preenchimento
            de todos os campos, no caso o somar(8, 4), neste exemplo não funciona pois esta faltando indicar qual o c.
            Agora se definirmos desse jeito:
            
def somar(a = 0, b = 0, c = 0)  Aqui definimos as funções, então pode-se até mesmo chamar a função somar() sozinha que 
    s = a + b + c              que ela vai retornar alguma coisa, no caso ali é 0 
    print(f'A soma de vale{s}')  
"""
# 4° Tópico ==> Escopo de variáveis

"""
 Básicamente na programação, escopo é um local onde uma variavel vai existir e onde uma variável não vai mais existir
 Existem dois tipos de variáveis, as globais e as locais.
globais funcionam em todo o programa, enquanto que as locais vão funcionar só em determinadas partes
que definirmos, como em uma def, exemplo

def teste():
    x = 0     variavel local x
    print(f'Na função teste, n vale {n'})
    print(f'Na função teste, x vale {x}') 


programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa pricipal, x vale {x})  O x não esta definido no programa pricipal, então esse print()
                                           retorna com um erro. 


 No python uma mesma variavel pode existir com dois valores diferentes, desde que sejam dois tipos de variaveis 
ou seja, uma global e uma local, exemplo

def teste(b): 
    global a   ==> com esse comando definimos que A sera global, no caso o a lá de baixa que passa a veler 8
    a = 8     se não exsitisse esse A declarado aqui dentro, ele pegaria o valor global, mas como foi definida
    b += 4   ele usa a local, mas o b continar pegando o valor da variavel global, 5 += 4     
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
    
    
a = 5 
teste(a)
print(f'A fora vale {a}')
"""

# 5° ==> Tópico Retorno de resultados: Retornando Valores
"""
 def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')
    
    
somar(3, 2, 5)

 Se quisermos retornar, as somas valem 3, 2 e 5 não podemos usar a função somar() como está descrita ali em cima
para tal usamos o return

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s
    
    
resp = somar(3, 2, 5) podemos jogar o resultado que é s dentro de uma variavel, que é resp ou
print(somar(3, 2, 5)) colocarmos direto dentro de um print, como fazermos com as outras variaveis

 Assim podemos ter vaias variaveis usando a mesmo função com resultador diferentes:
 
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')

"""

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

#Ao invés de números podemos retornar verdadeiro ou falso:

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


