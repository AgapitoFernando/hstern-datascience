# Dia 4 — Machine Learning Introdutório

**Dataset:** Diamantes limpo (`diamonds_clean.csv`)
**Notebook:** `notebooks/dia04_machine_learning.ipynb`

---

## Conceitos

**Machine Learning** é ensinar um computador a encontrar padrões nos dados e fazer previsões — sem programar regras manualmente. Em vez de dizer "se o diamante pesa mais de 1 quilate, vale mais de $5.000", o modelo aprende essa relação sozinho a partir dos dados.

### Tipos de problema

| Tipo | O que faz | Exemplo |
|------|-----------|---------|
| Regressão | Prevê um número contínuo | Prever o preço de um diamante |
| Classificação | Prevê uma categoria | Identificar se um diamante é Ideal ou não |

Hoje usamos **Regressão** — o target (`price`) é um número.

---

## Pipeline do dia

```
Dados → Encoding → Split treino/teste → Treinar modelo → Avaliar → Prever
```

---

## Comandos aprendidos

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Encoding — converte categorias em colunas binárias (0 ou 1)
df_modelo = pd.get_dummies(df, columns=['cut', 'color', 'clarity'])

# Separa features (X) e target (y)
X = df_modelo.drop(columns=['price'])
y = df_modelo['price']

# Divide em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Cria e treina o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Faz previsões
y_pred = modelo.predict(X_test)

# Avalia o modelo
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## Conceitos importantes

**Encoding (`pd.get_dummies`)** — ML só trabalha com números. Cada categoria vira uma coluna binária. A coluna `cut` com 5 valores vira 5 colunas: `cut_Fair`, `cut_Good`, `cut_Ideal`, `cut_Premium`, `cut_Very Good`.

**Train/test split** — nunca avaliamos o modelo com os mesmos dados que ele usou para aprender. Seria como dar a prova com o gabarito. O `random_state=42` garante que a divisão seja sempre a mesma — resultados reproduzíveis.

**F-strings** — forma moderna de formatar texto em Python:
```python
print(f"MAE: $ {mae:.2f}")   # :.2f = 2 casas decimais
```

---

## Métricas de avaliação

| Métrica | Fórmula simplificada | Interpretação |
|---------|----------------------|---------------|
| **MAE** | Média dos erros absolutos | Erro médio em dólares — mais intuitivo |
| **R²** | Variação explicada pelo modelo | 0 = nada, 1 = perfeito |

---

## Resultados

| Métrica | Valor |
|---------|-------|
| R² | 0.9246 — explica 92,5% da variação de preço |
| MAE | $ 716,53 — erro médio por diamante |

**Previsão exemplo:** 1 quilate, corte Ideal, cor D, clareza IF → **$ 7.630,70**

---

## Limitações da Regressão Linear

- Pode prever **preços negativos** para diamantes baratos — não tem restrição de valor mínimo
- **Dispersão crescente** em diamantes caros — pedras raras têm precificação mais complexa
- Assume relação linear entre features e preço — nem sempre é verdade

Modelos mais sofisticados (Random Forest, Gradient Boosting) corrigem esses problemas.
