senha_correta = 10
chance = 3 


while chance != 0:
    tentativa = eval(input("Digite a senha:"))
    if tentativa == senha_correta:
        print("Senha correta, cofre liberado!")
        break
    else:
        print(f"Senha incorreta, você ainda tem {chance-1} tentativas.")
    chance -= 1 
if tentativa != senha_correta:
    print("Você não digitou a senha correta, cofre bloqueado")