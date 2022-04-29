'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''
sex = ''
gender = str(input('Digite seu gênero com [M/F]: ')).strip().upper()
while gender not in 'MmFf':
    gender = str(input('Só ceitamos [M/F]')).upper().strip()
    if gender == 'F':
        sex = 'Feminino'
    elif gender == 'M':
        sex = 'Masculino'
print(f'Gênero {sex} registrado com sucesso. ')




