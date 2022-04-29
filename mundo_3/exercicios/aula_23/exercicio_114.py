"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com/?ref=logo')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site facebook com sucesso!')
    print(site.read())
"""
site = urllib.request.urlopen('https://www.facebook.com/?ref=logo')
print('Consegui acessar o site Pudim')
"""