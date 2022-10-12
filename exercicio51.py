num = int(input('Primeiro termo: '))
numR = int(input('Razão: '))
decimo = num + (10 - 1)*numR


for i in range(num, decimo + numR, numR):
    print('{}'.format(num+i))