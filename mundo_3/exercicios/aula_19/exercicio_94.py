"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

pessoas = []
dados = {}
media = idades = 0
mulheres = []
maiorM = []
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['genero'] = str(input('Genêro: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    cont = str(input('Continuar o cadastro? [S/N] ')).strip().upper()
    if 'N' in cont:
        break

print(f'Total de pessoas cadastradas {len(pessoas)}')

for c in pessoas:
    idades += c['idade']
media = idades / len(pessoas)

print(f'\nA média de idades é de {media:.2f} anos')
print()
print('-='*20)
print(f'Lista com as mulheres:')
print()
for m in pessoas:
    if m['genero'] == 'F':
        mulheres.append(m)
for m in pessoas:
    for k, v in m.items():
        print(f'{k} {v}')
    print()
print('-='*20)
print('Lista com as pessoas com idade supedior a média: ')
for maior in pessoas:
    if maior['idade'] > media:
        maiorM.append(maior)
for c in pessoas:
    for k, v in c.items():
        print(f'{k} {v}')
    print()
#solução Guanabara
"""
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoa['genêro'] = str(input('Genêro: [M/F] ')).strip().upper()[0]
        if pessoa ['genêro'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['genêro'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print('D) lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')
"""