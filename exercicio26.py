frase=str(input("Escreva uma frase: ")).strip().upper()


print("A letra A aparece: {} vezes".format(frase.count('A')))

print("A letra A aparece 1º vezes na posição: {}".format(frase.find('A')))

print("A letra A aparece a ULTIMA vezes na posição: {}".format(frase.rfind('A')))