''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

of_age = men = women = 0

while True:
    name = str(input('Nome: ')).strip().title()
    gender = str(input('Gênero [M/F]: ')).strip().title()
    age = int(input('Idade: '))
    continues = str(input('Deseja continuar? [S/N]\n ')).strip().upper()
    continues2 = continues[0]
    if 'N' in continues2:
        break
    elif age > 18:
        of_age += 1
    elif gender[0] == 'M':
        men += 1
    elif gender[0] == 'F' and age < 20:
        women += 1
print(f'O número de pessoas maiores de 18 anos é de {of_age} pessoa(s). ')
print(f'O número de homens na lista é de {men} homens. ')
print(f'O número de mulheres com menos de 20 anos de idade é de {women} mulhere(s). ')
