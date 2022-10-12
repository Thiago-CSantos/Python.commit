salario=float(input('Qual o seu salario? '))

if (salario>1250.00):
    aumento=salario*0.10

    salarioA=salario+aumento
    print('Você tera um aumento de R${} no seu salario. \n totalizando R${}'.format(aumento, salarioA))

if(salario<=1250.00):
    aumento=salario*0.15
    
    salarioA=salario+aumento
    print('Você tera um aumento de R${} no seu salario. \n totalizando R${}'.format(aumento, salarioA))
