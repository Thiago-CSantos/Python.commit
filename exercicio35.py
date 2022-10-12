reta1=float(input('Digite o comprimento de uma reta: '))
reta2=float(input('Digite o comprimento de uma reta: '))
reta3=float(input('Digite o comprimento de uma reta: '))

if(reta1+reta2<reta3) or (reta2+reta3<reta1) or (reta1+reta3<reta2):
    print('Não é um triangulo: ')

else:
    print('È um triangulo')