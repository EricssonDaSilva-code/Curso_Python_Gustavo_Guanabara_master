"""
 Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos
a favor das nossas estratégias de código.
 É muito importante saber usar o break no Python, já que em alguns casos
precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

"""
# Quando colocar um True no while ele não para até darmos um comando break
"""
while True:
    if terreno
        passo
    elif buraco:
        pula
    elif moeda:
        pega
    elif trofeu:
        pula
        break
pega
"""
#não deu certo com a string
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == '':
        break
    s += n
print(s)
