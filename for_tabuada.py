#primeira tentativa

qual_tabuada = eval(input("Digite qual tabuada você deseja saber: ")) 
max_tabuada = eval(input("Digite até qual valor deve ir sua tabuada: ")) 

for tabuada in range(0, max_tabuada): 
    tabuada += 1 
    tabuada *= qual_tabuada
    print(tabuada) 

#tentativa pós ajuda

valor_tabuada = eval(input("Digite qual tabuada você deseja saber: "))
limite_tabuada = eval(input("Digite até qual valor deve ir sua tabuada: "))
for tabuada in range(0, limite_tabuada+1):
    print(f"{valor_tabuada}x{tabuada} = {valor_tabuada*tabuada}")