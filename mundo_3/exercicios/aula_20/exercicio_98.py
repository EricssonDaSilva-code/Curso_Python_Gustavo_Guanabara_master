"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

--> print(f"{valor} ", end="")  # Exemplo de print espaçado
"""
def titulo(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))

def contador(inicio, fim, passo):
    if inicio < fim:
        fim += 1
    elif inicio > fim:
        passo = passo - passo * 2
        fim -= 1
    titulo(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ', flush=True)




#programa principal
titulo(f'\n{contador(0, 10, 1)}\n')
contador(10, 0, 2)
titulo('\nAgora é sua vez de contar')
inicio = int(input('inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
