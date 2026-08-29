# Consolidando Pandas para Análise de Dados

O objetivo do projeto é consolidar os conhecimentos em python, especificamente com a biblioteca pandas, após o mini curso [PANDAS NO PYTHON DO ZERO | Guia Completo de DataFrames e Análise de Dados](https://www.youtube.com/watch?v=sRE0UQuXF88&t=35s) do canal Engenharia de Dados | Data Engineer Help

## Estudo de caso

_Foi criado uma base de dados simples e didática com algumas vendas._

Sua função é tratar essa base para ser usada posteriormente em analises mais profundas pela equipe de BI que precisa das seguintes planilhas em excel:

- Vendas tratadas
- Receita mensal por região
- Ranking vendedores
- Ticket médio
- Comissao

## Regras de negócio

1. Apenas vendas concluídas
2. Comissão = 1% por venda concluída
3. Ticket médio por vendedor

**Tratamento de nulos**

1. valor_venda = média
2. desconto = 0
3. vendedor = "Não informado"

## Etapas

1. Análise exploratória
2. Aplicação de filtro concluídos
3. Tratamento tipo de coluna
4. Tratamento nulos
5. Tratamento meses
6. Colunas calculadas
7. Criação das tabelas
8. Exportação excel

_Data de criação: 29/08/2026_
