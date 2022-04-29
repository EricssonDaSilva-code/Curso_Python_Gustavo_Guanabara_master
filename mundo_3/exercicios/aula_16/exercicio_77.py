'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''

tupla = ('palavra', 'tupla', 'tempo', 'chocalho', 'python', 'curso em video', 'futuro',
         'presente', 'reset', 'azura', 'tempo', 'madrugada', 'junior', 'desenvolvedor',
         'developer', 'mobile', 'programador', 'emprego', 'estagio', 'estudos')

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos ', end='')

    for letra in palavra:
            if letra.lower() in 'aeiou':
                print(f'{letra}', end=' ')


