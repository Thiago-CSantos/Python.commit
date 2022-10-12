num=int(input('Escolha um número: '))
tabuada=0

for c in range(1, 11):

    tabuada= num * c

    print("{} x {} = {}".format(c, num, tabuada))