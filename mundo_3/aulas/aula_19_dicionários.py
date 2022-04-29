"""
 Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
 Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma
estrutura, acessíveis por chaves literais.
"""

"""
Dicionários são variaveis compostas que podem ter indices litearais,personalizar os itens,
ao inves de apenas números. Para tal usamos chaves.{}
dados = dict{}
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome']     ===  Pedro
print(dados['idade'])   ===  25
"""

 #Para adicionar elemenetos, no caso genêro, .append() não funciona basta usar este comando:
#     dados['sexo'='M']

 #Para apagar:
#     deldados['idade']

"""
Vamos criar um dicionario para guardar nomes de filme exemplo:
filme={'titulo':'Star Wars',               
       'ano':1977,                          
       'diretor':'George Lucas'
        }

O dicionario filmes possui 3 elementos, o python chama esses elementos de keys

A qualquer momento podemos acessar: itens, chaves e valores, vamos ver a diferença:

print(filme.values())   === 'Star Wars' 1977 'George Lucas'
print(filme.keys())     ===    titulo    ano    diretor
print(filme.items())    ===  Pega tudo que esta em cima:

Podemos velues, keys e item com for:

for k, v in filme.items():
    print(f'O {{k} é {v}')
igual a ===:
O titulo é Star Wars
O ano é 1977
O diretor é George Lucas

"""

"""
 Podemos aninhar listas, dicionarios e tuplas:
 
locadora = list()
locadora.append(filmes)

locadora:
'Star Wars' 1977 'George Lucas'  'Avengers' 2012 'joss Whedon' 'Matrix' 1999 'wachowski'    
   titulo    ano    diretor        titulo    ano    diretor     titulo   ano   diretor
             0                               1                           2

print(locadora[0]['ano'])    === 1977
print(locadora[2]['titulo']) === Matrix

"""
#Pratica
"""
pessoas = {'nome': 'Gustavo', 'genêro': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['genêro'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')  #como foi declarado com aspas '' simples temos que usar ""
#del pessoas['sexo']
pessoas['nome'] = 'leandro'
pessoas['peso'] = 95.5
for k in pessoas.values():  #trocar o keys por items() e values() para exemplificar
    print(k)                #não se usa enumerate
"""
brasil = []
estado1 = {'uf': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado2 = {'uf': 'Santa Catarina', 'Sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['Sigla'])
print(brasil[0]['uf'])

#o seguinte código não funcioa
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado[:])                            Não se pode fazer cópias de dicionarios com [:]
print(brasil)                                           para isso usase o métod .copy()
"""
#aqui funciona

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())                           # Não se pode fazer cópias de dicionarios com [:]
for e in brasil:                                           #para isso usase o métod .copy()
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
"""
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
"""