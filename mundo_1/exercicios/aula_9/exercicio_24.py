# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

cidade1 = input('Digite o nome de uma cidade: ')
cidade = cidade1.title().strip



if 'Santo' in cidade:
    print('A cidade {} contem santo no nome.'.format(cidade))
else:
    print('A cidade {} não contem Santo no nome. '.format(cidade))
