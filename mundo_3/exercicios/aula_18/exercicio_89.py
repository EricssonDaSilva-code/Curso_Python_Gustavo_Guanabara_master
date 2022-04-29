"""
Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta.

No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente

"""
#não consegui fazer por enquanto
"""
nomNot = []
alun = []
nota = 0
media = 0
while True:
    nomNot.append(str(input('Nome: ')).strip().title())
    for c in range(1, 3):
        nota = (int(input(f'Nota {c}\n===>')))
        media += nota
        nomNot.append(nota)
    nomNot.append(media / 2)
    alun.append(nomNot[:])
    nomNot.clear()
    media = 0
    cont = str(input('Continuar? [S/N]')).strip().upper()
    if 'N' in cont[0]:
        break
for c, v in enumerate(alun):
    print(f'{c} {v}')

por_alu = str(input('Deseja acessar a mpta de quais alunos?\n'
                    'A-todos: '
                    'B-selecionar por aluno: ')).strip().upper()
if 'A' in por_alu[0]:
    for c, v in enumerate(alun):
        print(f'O aluno {v[0][c]} teve as seguintes notas {v[1]}, {v[2]} e média de {v[3]}')

"""
#solução do Guanabara
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No."}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('_' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')




