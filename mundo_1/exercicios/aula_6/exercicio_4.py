# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
some = input('Digite algo: \n')
print(type(some))

print('É alfanúmerico? {}'.format(some.isalpha()))
print('É minúsculo? {}'.format(some.islower()))
print('É maiscúlo? {}'.format(some.isupper()))
print('É decimal? {}'.format(some.isdecimal()))
print('É númerico? {}'.format(some.isnumeric()))
print('É alfanúmerico?'.format(some.isalnum()))
