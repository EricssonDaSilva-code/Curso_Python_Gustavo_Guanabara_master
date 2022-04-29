# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase1 = input('Digite uma frase: ')
frase = frase1.lower().strip()
c = frase.count('a')
c1 = frase.find('a')
cf = frase.rfind('a')

print('O numero de letras (a) é de {} unidade(s). '.format(c))
print('Ela aparece a primeira vez na posição {}. '.format(c1))
print('E a última vez que aparece é na posição {}. '.format(cf))

