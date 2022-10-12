from traceback import print_tb
from unittest import result


n1=int(input('Digite um numero: '))

result = n1 % 2 

if result == 0:
    print('PAR')

else:
    print('IMPAR')