'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''

expre = str(input('Digite um expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append(expre)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está certa.')
else:
    print('Sua expressão está errada. ')
