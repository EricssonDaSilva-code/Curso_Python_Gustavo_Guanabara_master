"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""

dis = int(input('Digite a distancia: '))
if dis <= 200:
    cal = dis * 0.5
    print('Para a distancia de {}Km, a passagem fica em R${} reais.'.format(dis, cal))
else:
    cal = dis * 0.45
    print('Para a distancia de {}Km, a passagem fica em R${} reais. '.format(dis, cal))
print('FIM')
