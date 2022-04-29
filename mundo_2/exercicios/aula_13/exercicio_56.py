''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

average_age = 0
young_women = 0
old_man = ''
age_old_man = 0

for c in range(1, 5):
    name = str(input('Enter your name: '))
    age = int(input('Enter your age: '))
    gender = str(input('Enter your gender: ')).strip().title()
    average_age += age
    if gender == 'Feminino' and age < 20:
        young_women += 1
    elif gender == 'Masculino' and age > age_old_man:
        age_old_man += age
        old_man = name

print(f'A média de idade do grupe é de {average_age / c} anos. ')
print(f'O número de mulheres com menos de vinte anos é {young_women}')
print(f'O nome do homem mais velho é {old_man}')


