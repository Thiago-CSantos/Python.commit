import random

numero=random.randint(0,5)


usuario=int(input('escolha o numero entre 0 e 5: '))

if usuario == numero:
    print('voce acertou')
    print('numero do computador: {} \n seu numero: {}'.format(numero, usuario))

else:
    print("voce errou")




