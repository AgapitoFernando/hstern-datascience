# Dia 3 — Limpeza e Preparação de Dados

**Dataset:** Diamantes — Kaggle (`shivam2503/diamonds`)
**Notebook:** `notebooks/dia03_limpeza_dados.ipynb`

---

## Conceitos

Na prática, cientistas de dados passam 60–80% do tempo limpando dados — antes de qualquer gráfico ou modelo. Dados sujos geram análises erradas.

**Tipos de problema mais comuns:**
- Valores ausentes (NaN)
- Duplicatas
- Tipos de dados errados
- Outliers e erros de medição
- Texto mal formatado

---

## Comandos aprendidos

```python
import pandas as pd
import numpy as np

# Diagnóstico inicial
df.info()               # tipos de dados e contagem de não-nulos
df.isnull().sum()       # total de valores ausentes por coluna
df.describe()           # estatísticas — revela outliers nos min/max

# Remover coluna desnecessária
df = df.drop(columns=["Unnamed: 0"])

# Detectar erros de medição (zeros impossíveis)
(df["x"] == 0).sum()
df[df["y"] > 20][["carat", "price", "x", "y", "z"]]  # investiga outliers

# Remover linhas problemáticas
df = df[(df["x"] > 0) & (df["y"] > 0) & (df["z"] > 0)]   # zeros
df = df[(df["y"] < 20) & (df["z"] < 20)]                  # outliers improváveis

# Converter para category ordenada
cut_order = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
df["cut"] = pd.Categorical(df["cut"], categories=cut_order, ordered=True)
# (mesma lógica para color e clarity)

# Salvar dataset limpo
df.to_csv("../data/diamonds_clean.csv", index=False)
```

---

## Resultado da limpeza

| Etapa | Registros |
|-------|-----------|
| Original | 53.940 |
| Após remover zeros em x, y, z | 53.920 |
| Após remover outliers em y e z | 53.917 |
| **Final** | **53.917** |

Colunas corrigidas: `cut`, `color` e `clarity` → tipo `category` com ordem lógica definida.

---

## Conceitos importantes

**`pd.Categorical` com `ordered=True`** — ensina o pandas que Ideal > Premium > Very Good > Good > Fair. Isso melhora performance e habilita comparações ordenadas em análises futuras.

**Outlier vs erro** — nem todo valor extremo é erro. O diamante Cullinan tinha 3.106 quilates brutos — tecnicamente um "outlier" que é real. Contexto do domínio importa na decisão de remover ou não.
