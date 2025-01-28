"""
1- Capital investido (C)
2- Taxa de juros anual (i)
3- Tempo em meses que o capital vai ficar investido (t)
4- Os juros do rendimento (J), valor final - valor investido
5- Montante final: M = C*(1+i)^t 
"""
import math
import tkinter

help(tkinter)

def composto(capital, juros, tempo):
    return capital*math.pow(1+juros,tempo)

def simples (capital, juros, tempo):
    return capital*juros*tempo

capital = float(input("Qual será o aporte inicial? "))
juros = float(input("Qual será o juros ao ano em porcentagem (%)? "))
tempo = int(input("Qual será o tempo investido em meses? "))

juros = juros/100
tempo = tempo/12

valor_final_composto = composto(capital,juros,tempo)
valor_final_simples = simples(capital, juros, tempo)

print(f"O valor final do rendimento com juros compostos será: R$ {valor_final_composto:.02f}")
print(f"O juros do rendimento com juros compostos será: R$ {(valor_final_composto - capital):.02f}")
print(f"O valor final do rendimento com juros simples será: R$ {(valor_final_simples + capital):.02f}")
print(f"O juros do rendimento com juros simples será: R$ {(valor_final_simples):.02f}")