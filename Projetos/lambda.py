#Calculadora básica com lambda
calculo = input("Digite '+' para soma, '-' para subtração, '*' para multiplicação e '/' para divisão: ")
continuar = "sim"

while continuar == "sim":
    numero1 = eval(input("Digite o primeiro número: "))
    numero2 = eval(input("Digite o segundo número: "))

    if calculo == "+":
        soma = lambda a,b:a+b
        print(soma(numero1,numero2))

    elif calculo == "-":
        subtracao = lambda a,b:a-b
        print(subtracao(numero1,numero2))  

    elif calculo == "*":
        multiplicacao = lambda a,b:a*b
        print(multiplicacao(numero1,numero2))

    elif calculo == "-":
        divisao = lambda a,b:a/b
        print(divisao(numero1,numero2))
    
    continuar = input("Se deseja fazer outra conta digite 'sim': ")  
print("Cálculos finalizados, obrigada!")

