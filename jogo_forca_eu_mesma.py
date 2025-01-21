"""
importar o random
definir as variáveis: palavras, palavra_sorteada, palavra_escondida, letras_adivinhadas, max_tentativas
while true todo momento
printo a palavra escondida
solicito uma letra
verifico se essa letra já foi selecionada antes
adiciono a letra escolhia a lista de letras adivinhadas
verificação se a letra pertence a palavra sorteada
se a letra pertence então deixe ela visível 
se nao reduza uma tentativa 
printa se o jogador ganhou ou não
"""

import random 

palavras = ["computador", "tablet", "telefone", "televisao"]

palavra_sorteada = random.choice(palavras)

palavra_escondida = '-'*len(palavra_sorteada)

letras_adivinhadas = [] 

max_tentativas = 6

while True:
    print(palavra_escondida)
    letra = input("Digite uma única letra: ")
    
    if letra in letras_adivinhadas:
        print("Essa letra já foi escolhida antes, tente um outra letra.")
        continue
    letras_adivinhadas.append(letra)

    if letra in palavra_sorteada:
        lista = [] #Lista para adicionar as letras corretas
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra) # se a letra for igual ao indice da palavra_sorteada então adicone a letra na lista
            else:
                lista.append(palavra_escondida[indice]) #se não, adicione o "escondido" na lista

        palavra_escondida = "".join(lista) #altera o valor da variável para a lista concatenada em strings vazias
    else:
        max_tentativas -= 1
        print(f"Letra errada, você ainda possui {max_tentativas} tentativas")
    if palavra_escondida == palavra_sorteada:
        print("Parabéns, você conseguiu adivinhar a palavra!")
        break
    elif max_tentativas == 0:
        print(f"Infelizmente você não conseguiu, a palavra sorteada era {palavra_sorteada}")
        break