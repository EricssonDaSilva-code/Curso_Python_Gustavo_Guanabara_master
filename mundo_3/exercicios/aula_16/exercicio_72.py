'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito',
       'dezenove', 'vinte')
l_num = int(input('Digite um número entre 0 e 20 para te-lo em extenso: '))
print(num[l_num])
