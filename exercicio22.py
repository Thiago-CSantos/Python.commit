from dataclasses import replace
from gettext import find
from re import split


nome=input('Digite seu nome: ').strip()

print(nome.upper(), '\n')

print(nome.lower(), '\n')

nome2=len(nome)-nome.count(' ')

print('A quantidade de caracteres é: {}'.format(nome2))

print('{}'.format(nome.find(' ')))
