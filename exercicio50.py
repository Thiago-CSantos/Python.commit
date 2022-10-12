contador=0



for c in range(0,6):
    num=int(input("Digite um numero: "))

    if(num %2 == 0):
        contador=num+contador


print(contador)