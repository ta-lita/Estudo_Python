import pandas as pd
import os

base_dados = {
    "id_pedido": ["001", "002", "003", "004", "005", "006", "007", "008"],
    "vendedor": ["Ana", "Ana", "Bruno", "Bruno", "Carlos", "Carlos", None, "Ana"],
    "regiao": ["Sul", "Sul", "Sudeste", "Sudeste", "Sul", "Sul", "Sudeste", "Sul"],
    "valor_venda": ["1000", "1500", "2000", None, "1800", "900", "1200", "1300"],
    "desconto": [100, 0, 150, 200, None, 50, 0, 130],
    "status": ["Concluido", "Concluido", "Concluido", "Cancelado", "Concluido", "Concluido", "Concluido", "Concluido"],
    "mes": ["Jan", "Fev", "Jan", "Fev", "Jan", "Fev", "Fev", "Mar"]
}

df_bruto = pd.DataFrame(base_dados)
df = pd.DataFrame(base_dados)

# ----- Exploração dos dados -----
print("\nDados brutos (5 linhas)\n")
print(df.head())

print("\nInformações sobre dados\n")
print(df.info())

print("\nEstatística descritiva\n")
print(df.describe())

# Filtro Apenas concluídos

filtro_status = df["status"] == "Concluido"

df = df[filtro_status]
print("\nAplicação filtro concluído\n")
print(df)

# Tratamento tipos de coluna

df["id_pedido"] = pd.to_numeric(df["id_pedido"], errors="coerce")
df["valor_venda"] = pd.to_numeric(df["valor_venda"], errors="coerce")
df["desconto"] = pd.to_numeric(df["desconto"], errors="coerce")

print("\n Tipos corrigidos\n")
print(df.info())

# Tratamento dos Nulos
print("\nAnálise nulos\n")
print(df.isna().sum())

df["vendedor"] = df["vendedor"].fillna("Não informado")
df["valor_venda"] = df["valor_venda"].fillna(df["valor_venda"].mean())
df["desconto"] = df["desconto"].fillna(0)

print("\nBase pós tratamento dos nulos\n")
print(df)

# Colunas calculadas

df["valor_liquido"] = df["valor_venda"] - df["desconto"]
df["comissao"] = df["valor_liquido"] * 0.01


def transf_mes_num(mes):
    if mes == "Jan":
        return 1
    elif mes == "Fev":
        return 2
    elif mes == "Mar":
        return 3
    else:
        0


df["mes_num"] = df["mes"].apply(transf_mes_num)

print("\nBase pós colunas calculadas\n")
print(df)

# Criação das tabelas

vendas_tratadas = df.copy()

receita_mensal = vendas_tratadas.groupby(["mes_num", "mes", "regiao"])[
    "valor_venda"].sum().reset_index().sort_values("mes_num")
print("\nReceita Mensal\n")
print(receita_mensal)

ranking_vendedores = vendas_tratadas.groupby("vendedor")["valor_venda"].sum(
).sort_values(ascending=False).reset_index()

ranking_vendedores.index = range(1, len(ranking_vendedores) + 1)
ranking_vendedores.index.name = "ranking"
print("\nRanking vendedores\n")
print(ranking_vendedores)

ticket_medio = vendas_tratadas.groupby(
    "vendedor")["valor_venda"].mean().reset_index()
print("\nTicket Médio\n")
print(ticket_medio)

comissao = vendas_tratadas.groupby(["vendedor"])[
    "comissao"].sum().reset_index()
print("\nComissão\n")
print(comissao)

# Exportação
caminho = os.path.join(os.path.dirname(__file__), "base_tratada.xlsx")

with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
    df_bruto.to_excel(
        writer,
        sheet_name="dados_brutos",
        index=False
    )
    vendas_tratadas.to_excel(
        writer,
        sheet_name="vendas_tratadas",
        index=False
    )
    receita_mensal.to_excel(
        writer,
        sheet_name="receita_mensal",
        index=False
    )
    ranking_vendedores.to_excel(
        writer,
        sheet_name="ranking_vendedores",
        index=True
    )
    ticket_medio.to_excel(
        writer,
        sheet_name="ticket_medio",
        index=False
    )
    comissao.to_excel(
        writer,
        sheet_name="comissao",
        index=False
    )
