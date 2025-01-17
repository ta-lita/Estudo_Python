numero = eval(input("Digite um número para calcular seu fatorial: "))
fatorial = numero
while numero >= 2:
    fatorial = fatorial * (numero - 1) #
    numero -= 1 
print(fatorial)


