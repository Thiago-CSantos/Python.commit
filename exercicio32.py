ano=int(input('Digite um ano: '))

anob=ano%4

print(anob)

if anob != 0:
    print('Não é um ano BISSEXTO ')

else:
    print('é um ano BISSEXTO ')