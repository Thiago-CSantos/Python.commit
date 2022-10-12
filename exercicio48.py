from unittest import result


contador=0
result=0

for c in range(1, 501, 2):
    
    if(c %3 == 0):
        contador = contador + c
        result= contador


print(result, end=' ')
