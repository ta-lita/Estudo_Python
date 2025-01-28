import random 

#definição das palavras que serão sorteadas
palavras = ["escola", "estudante", "lapis"] 

#método que escolhe alestoriamente uma item da lista 
palavra_sorteada = random.choice(palavras)

#cria uma string com "-" que representa as letras
palavra_escondida = '_' * len(palavra_sorteada) # "-" vezes a quantiade de letras da palavra 

#cria uma lista vazia para armazenar as letras que já foram tentadas
letras_adivinhadas = []

max_tentativas = 6 #variável com o número de tentativas

#condição que fica sempre acontecendo exceto quanto x acontece
while True:
    #mostra a palavra escondida
    print(palavra_escondida)
    #pedimos para o jogador digitar uma letra
    letra = input("Digite apenas uma letra: ")
    #verificamos se a letra já foi verificada
    if letra in letras_adivinhadas:
        print("Você já digitou essa letra, tente outra por favor.")
        continue #para a execução e volta para o começo do loop, nesse caso o while
    #adiciona a letra a lista de letras digitadas
    letras_adivinhadas.append(letra)
    #verificar se a letra digitada está na palavra sorteada
    if letra in palavra_sorteada:
        lista = [] #cria uma lista vazia
        #range.len substitui o equivalente da largura da palavra por um número 
        #o indice percorre cada um desses números 
        for indice in range(len(palavra_sorteada)):
            #se a letra digitada for igual ao indice da palavra sorteada então adiciona a letra a lista criada
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            #se não, adiciona o índice da palavra escondida na lista
            else:
                lista.append(palavra_escondida[indice])
        #transforma a variavel palavra escondida para uma junção de todos os itens usando uma string, nesse caso uma string vazia.
        palavra_escondida = "".join(lista)
    else: #letra não está na palavra sorteada
        max_tentativas -= 1
        print(f"Letra não encontrada, você tem mais {max_tentativas} tentativas")
    
    #verificamos se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print("Você ganhou, parabéns!")
        break
    elif max_tentativas == 0:
        print(f"Você perdeu, a palavra era {palavra_sorteada}")
        break
