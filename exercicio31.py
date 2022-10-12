from unittest import result


viagem=float(input('Qual a distância da sua viagem? '))



if viagem >= 200:
    result= viagem*0.45
    print('Você pagara R${}'.format(result))

else:
    result= viagem*0.50

    print('Você pagara na sua viagem R${}'.format(result))