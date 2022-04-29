def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(preço)


def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else moeda(res)


def metade(preço=0, format=False):
    res = preço / 2
    return res if format is False else moeda(res)


def resumo(preço=0, taxaa=10, taxar=5):
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analizado:   \t{moeda(preço)}')
    print(f'metadade do preço: \t{metade(preço, True)}')
    print(f'dobro do preço:  \t{dobro(preço, True)}')
    print(f'{taxaa}% de aumento:   \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução:   \t{diminuir(preço, taxar, True)}')
    print('_' * 30)


def moeda(preço=0, moeda='R$', format=False):
    return F'{moeda}{preço:>.2f}'.replace('.', ',')