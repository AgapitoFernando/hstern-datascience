# Dia 1 — Introdução ao Pandas

**Dataset:** Joalheria fictícia (criado manualmente)
**Notebook:** `notebooks/dia1_pandas.ipynb`

---

## Conceitos

**Pandas** é uma biblioteca Python para manipulação de dados tabulares — funciona como um Excel dentro do Python, porém automatizável. O nome vem de *Panel Data*, termo da econometria.

**Jupyter Notebook** é um documento interativo que mistura código, resultados e texto (markdown) em blocos chamados células. Formato padrão em Data Science.

### Estruturas principais do Pandas

| Estrutura | O que é |
|-----------|---------|
| `Series` | Uma única coluna de dados com índice |
| `DataFrame` | Tabela completa com linhas e colunas, composta por Series |

---

## Comandos aprendidos

```python
import pandas as pd

# Criar DataFrame
df = pd.DataFrame({"produto": [...], "preco": [...]})

# Explorar
df.shape        # dimensões: (linhas, colunas)
df.info()       # tipos de dados, valores nulos, memória
df.describe()   # estatísticas: média, desvio padrão, min, max, quartis

# Selecionar
df["preco"]                            # uma coluna
df[df["metal"] == "Ouro 18k"]         # filtro por condição
df[df["preco"] == df["preco"].max()]  # linha com valor máximo

# Agrupar
df.groupby("metal")["preco"].mean()   # média de preço por metal

# Nova coluna calculada
df["valor_total"] = df["preco"] * df["estoque"]
```

```python
import matplotlib.pyplot as plt

# Gráfico de barras
df.plot(kind="bar", x="produto", y="valor_total", title="Valor em Estoque")
plt.tight_layout()
plt.show()
```

---

## Insights gerados

- Preço médio do Ouro 18k (R$ 1.045) é quase 3× maior que o da Prata (R$ 385)
- O Colar de Prata, apesar do preço menor, tem o 2º maior valor em estoque por ter 12 unidades — insight que só aparece cruzando `preco × estoque`
