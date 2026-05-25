# Dia 2 — Visualização de Dados

**Dataset:** Diamantes — Kaggle (`shivam2503/diamonds`)
**Notebook:** `notebooks/dia02_visualizacao.ipynb`

---

## Conceitos

Visualização transforma números em histórias. Cada tipo de gráfico serve a um propósito diferente:

| Gráfico | Quando usar |
|---------|-------------|
| Barras | Comparar categorias |
| Linhas | Mostrar tendências ao longo do tempo |
| Dispersão (scatter) | Relação entre duas variáveis numéricas |
| Heatmap | Correlações entre múltiplas variáveis |
| Histograma | Distribuição de uma variável numérica |

---

## Bibliotecas

**Matplotlib** — base de todas as visualizações em Python. Controle total, mas mais verboso.

**Seaborn** — construído sobre o matplotlib. Gráficos estatísticos mais elaborados com menos código. Integra nativamente com DataFrames do pandas.

---

## Comandos aprendidos

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de barras — matplotlib
df.plot(kind="bar", x="cut", y="price")
plt.title("Preço médio por corte")
plt.tight_layout()
plt.show()

# Dispersão — relação quilates × preço
plt.scatter(df["carat"], df["price"], alpha=0.3)
plt.xlabel("Quilates")
plt.ylabel("Preço (USD)")

# Heatmap de correlações — seaborn
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

# Histograma de distribuição
sns.histplot(df["price"], bins=50)

# Boxplot — distribuição por categoria
sns.boxplot(x="cut", y="price", data=df)
```

---

## Insights gerados

- Quilates e preço têm correlação forte — quanto maior a pedra, maior o valor
- Cortes `Ideal` e `Premium` dominam o dataset em volume
- A distribuição de preços é assimétrica — maioria das pedras custa menos de $5.000, mas existem outliers acima de $15.000
