# Dia 5 — Classificação e Avaliação

**Dataset:** Diamantes limpo (`diamonds_clean.csv`)
**Notebook:** `notebooks/dia05_classificacao.ipynb`

---

## Conceitos

**Classificação** é prever uma categoria — diferente de regressão que prevê um número. O modelo aprende a separar os dados em classes a partir das features.

### Regressão vs Classificação

| | Regressão | Classificação |
|--|-----------|---------------|
| Target | Número contínuo | Categoria |
| Exemplo | Prever o preço | Prever o corte |
| Métrica principal | MAE, R² | Acurácia, F1-score |

---

## Random Forest

Conjunto de **árvores de decisão** treinadas com subconjuntos aleatórios dos dados. Cada árvore aprende padrões diferentes — a previsão final é a votação da maioria.

Como um painel de ourives experientes avaliando a qualidade do corte — cada um com sua perspectiva, a decisão final é o consenso.

```python
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(
    n_estimators=100,  # 100 árvores de decisão
    random_state=42,
    n_jobs=-1          # usa todos os núcleos do processador
)

modelo.fit(X_train, y_train)
```

---

## Métricas de Classificação

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Acurácia — percentual geral de acertos
acc = accuracy_score(y_test, y_pred)

# Relatório completo por categoria
print(classification_report(y_test, y_pred))

# Matriz de confusão — onde o modelo acerta e onde erra
cm = confusion_matrix(y_test, y_pred, labels=modelo.classes_)
```

| Métrica | O que mede |
|---------|------------|
| **Acurácia** | % de acertos no total |
| **Precision** | Dos que previu como X, quantos eram X de verdade |
| **Recall** | Dos que eram X, quantos o modelo acertou |
| **F1-score** | Média harmônica entre precision e recall |

---

## Features mais importantes

```python
# Quais características mais influenciam a previsão
importancias = pd.Series(
    modelo.feature_importances_,
    index=X.columns
).sort_values(ascending=False)
```

---

## Resultados

| Métrica | Valor |
|---------|-------|
| Acurácia | ~77% |
| Melhor categoria | Ideal — 87% F1-score |
| Pior categoria | Very Good — 56% F1-score |

### Features mais importantes
| Feature | Importância | Significado |
|---------|-------------|-------------|
| `table` | ~26% | Largura da mesa |
| `depth` | ~21% | Profundidade |
| `x`, `y`, `z` | ~30% | Dimensões físicas |

---

## Insight principal

O corte é determinado por **proporções físicas** (`table`, `depth`, `x/y/z`) — não por cor ou clareza. Exatamente o que um ourives experiente sabe: a qualidade do corte está na geometria da pedra, não nas suas características gemológicas.

Isso é **domain knowledge validado por dados** — um diferencial real numa entrevista. 💎

---

## Previsão com probabilidades

O Random Forest permite ver a probabilidade de cada categoria:

```python
corte_previsto = modelo.predict(diamante)[0]
probabilidades = modelo.predict_proba(diamante)[0]

for cat, prob in zip(modelo.classes_, probabilidades):
    print(f"{cat}: {prob*100:.1f}%")
```
