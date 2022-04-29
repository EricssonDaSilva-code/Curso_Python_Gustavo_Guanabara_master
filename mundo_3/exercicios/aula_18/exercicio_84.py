'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

'''

pessoas = []
dados = []
pessoas_pe = []
pessoas_le = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])

    if dados[1] >= 75:
        pessoas_pe.append(dados[:])
        dados.clear()
    elif dados[1] < 75:
        pessoas_le.append(dados[:])
        dados.clear()
    next = str(input('Continuar? [S/N]')).strip().upper()
    if 'N' in next[0]:
        break
print(f'{len(pessoas)} pessoas cadastradas. ')
print(f'pessoas pesadas\n{pessoas_pe}')
print(f'Pessoas leves\n{pessoas_le}')
