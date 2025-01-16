nota1 = eval(input("Digite a nota 1: "))
nota2 = eval(input("Digite a nota 2: "))

media = (nota1+nota2)/2

if media >= 7:
    print("Parabens, você foi aprovado")
elif media >= 5:
    print("Você está em exame.")
else:
    print("Infelizmente você foi reprovado!")