import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 5, 7, 1]
x2 = [2, 4, 6, 8, 10]
y2 = [5, 10, 1, 2, 3]

titulo = "Meu primeiro gráfico em python"
eixox = "Eixo x"
eixoy = "Eixo y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#plt.plot(x, y) #Gráfico de linha
#comparação
plt.bar(x1,y1, label = "Grupo 1") #Label define a legenda
plt.bar(x2,y2, label = "Grupo 2")
plt.legend() #Legend chama a lengenda
plt.show()

#TESTES GRÁFICOS
x = [1, 2, 3]
y = [2, 7, 1]
plt.scatter(x, y, label = "Pontos", color ="red")
plt.plot(x, y)
plt.legend()
plt.savefig("figura1.pdf")

#Estudo de caso - População brasileira 1980 a 2016
#DataSus

dados = open("/populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
  if i != 0:
    linha = dados[i].split(";")
    x.append(int(linha[0]))
    y.append(int(linha[1]))

plt.plot(x, y, color ="k", linestyle="--")
plt.bar(x, y, color = "#e4e4e4")
plt.title("Crescimento da população brasileira 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()
