"""
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma
 estrutura, acessíveis por chaves individuais.
"""

"""
pessoas = list()
pessoas.append(dados[:]) copia a lista dados para dentro da lista pessoas, listas dentro de listas
"""
"""
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])        Pedro
print(pessoas[1][1])        19
print(pessoas[2][0])        João
print(pessoas[1])           ['Maria', 19]
"""
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list() #não esquecer de colocar [:] para copiar a lista e enão conectalas
galera.append(teste[:])  #não esquecer de colocar [:] para copiar a lista e enão conectalas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade. ')


"""
galera = list()
dados = list()
totmenor = totmaior = 0
for c in range(0, 3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(str(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade. ')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        totmenor +=1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade. ')

"""
