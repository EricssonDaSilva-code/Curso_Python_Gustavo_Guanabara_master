"""
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
usando os comandos if.. elif.. else em programas Python.
"""

nome = str(input('Qual é o seu nome? ')).strip().title()
if nome == 'Ericsson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == ' Maria' or nome == 'Paulo': # elif só depois de um if, mas pode ter quantos quiser
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jessica Juliana':                  # parece lista
    print('Belo nome feminino')
else:                                        #else é opcional
    print('Seu nome é bem comum. ')
print('Tenha um bom dia, {}'.format(nome))