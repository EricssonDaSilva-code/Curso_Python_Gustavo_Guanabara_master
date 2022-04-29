"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randint

def maior(*num):
    print(max(num))




maior(100, 11, 3, 5, 9, 45, 78)

