frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python', 'Adroid')
dividido = frase.split()
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[5:])
print(frase[1:15:2])
print(frase[1::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.strip())

print('mostra as listas novas geradas pelo split:', dividido) #mostra as listas novas geradas pelo split
print('mostra da [2] segunda lista a letra [3] na posição 3:', dividido[2][3]) #mostra da [2] segunda lista a letra [3] na posição 3
print('mostra a lista [0] na posição zero:', dividido[0]) #mostra a lista [0] na posição zero


print("""Para textos longos abre aspas 3 vezes e fecha 3 vezes, assim
pode-se colocar qualquer tamanho de texto que ele pões na tela""")
