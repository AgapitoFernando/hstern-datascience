# Dia 6 — Dashboard com Streamlit

**Dataset:** Diamantes limpo (`diamonds_clean.csv`)
**App:** `app/dashboard.py`

---

## Conceitos

**Streamlit** transforma um script Python em uma aplicação web interativa, sem precisar saber HTML, CSS ou JavaScript. Ideal para prototipar dashboards de dados rapidamente.

Diferente de notebooks, Streamlit roda como um **script `.py` normal** que é reexecutado do início a cada interação do usuário (mudar um filtro, mover um slider).

---

## Estrutura básica

```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Título", page_icon="💎", layout="wide")
st.title("Título do Dashboard")

@st.cache_data
def carregar_dados():
    return pd.read_csv('../data/diamonds_clean.csv')

df = carregar_dados()
st.dataframe(df.head())
```

```bash
streamlit run app/dashboard.py
```

---

## Componentes usados

| Componente | Função |
|------------|--------|
| `st.set_page_config()` | Configura título, ícone e layout da página |
| `st.title()` / `st.markdown()` | Texto e títulos |
| `@st.cache_data` | Evita recarregar dados a cada interação |
| `st.sidebar` | Barra lateral para filtros |
| `st.multiselect()` | Seleção múltipla (ex: filtro de corte) |
| `st.slider()` | Seletor de faixa de valores (ex: faixa de preço) |
| `st.metric()` | Card com métrica em destaque |
| `st.columns()` | Divide a tela em colunas lado a lado |
| `st.pyplot()` | Exibe gráficos do matplotlib/seaborn |
| `st.dataframe()` | Exibe tabelas interativas |

---

## Filtros interativos

```python
st.sidebar.header("🔍 Filtros")

cortes_selecionados = st.sidebar.multiselect(
    "Corte", options=df['cut'].unique(), default=df['cut'].unique()
)

preco_min, preco_max = st.sidebar.slider(
    "Faixa de preço (USD)",
    min_value=int(df['price'].min()),
    max_value=int(df['price'].max()),
    value=(int(df['price'].min()), int(df['price'].max()))
)

df_filtrado = df[
    (df['cut'].isin(cortes_selecionados)) &
    (df['price'] >= preco_min) & (df['price'] <= preco_max)
]
```

---

## Métricas e gráficos lado a lado

```python
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", f"{len(df_filtrado):,}")
col2.metric("Preço médio", f"$ {df_filtrado['price'].mean():,.0f}")

col_esq, col_dir = st.columns(2)
with col_esq:
    fig, ax = plt.subplots()
    sns.histplot(df_filtrado['price'], bins=40, ax=ax)
    st.pyplot(fig)
```

---

## Erro do dia

```python
df.groupby('cut', observed=true)   # ❌ NameError
df.groupby('cut', observed=True)   # ✅ Python é case-sensitive — booleanos são maiúsculos
```

---

## Hot reload

O Streamlit recarrega automaticamente ao salvar o arquivo — não precisa parar e rodar `streamlit run` de novo. Basta salvar no editor e voltar ao navegador (ou apertar `R`).

---

## Resultado

Dashboard funcional com:
- Tabela de dados filtrável
- Filtros por corte (multiselect) e faixa de preço (slider)
- 4 métricas em destaque (cards)
- Histograma de distribuição de preços
- Gráfico de preço médio por corte

Primeira aplicação web em Python — sem front-end tradicional, 100% Python. 💎
