nome=str(input('Qual o seu nome? ')).upper().strip()

nome1=nome.split()

print("Seu primeiro nome é: {}".format(nome1[0]))

print("Seu ultimo nome é: {}".format(nome1[len(nome1)-1]))