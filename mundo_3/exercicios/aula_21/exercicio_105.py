"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)

Adicione tambeem as docstrings da função
"""
def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita váriaveis)
    :param sit: valor opcional, indicando se deve ou não adicionar situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
        return r


#programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)