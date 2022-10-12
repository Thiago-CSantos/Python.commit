velo=int(input('Qual a velocidade que está dirigindo? '))

if velo > 80:
    print('Parabens! voce foi multado \n R$:7,00 por Km acima do limite')
    multa=(velo-80)*7

    print('Valor da multa: R${}'.format(multa))