a = 1 
b = 1
digito = eval(input("Digite o elemento: "))

if digito == 1 or digito==2:
    print(1)
else:
    for _ in range(2, digito):
        c = a + b
        a = b
        b = c
    print(f"O número de fibonacci na posição {digito} é {c}")
    