import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página — precisa ser o primeiro comando Streamlit
st.set_page_config(
    page_title="Dashboard Diamantes",
    page_icon="💎",
    layout="wide"
)

# Título
st.title("💎 Dashboard de Análise de Diamantes")
st.markdown("Explore o dataset de diamantes de forma interativa")

# Carrega os dados (cache evita recarregar a cada interação)
@st.cache_data
def carregar_dados():
    return pd.read_csv('../data/diamonds_clean.csv')

df = carregar_dados()

st.write(f"Dataset com **{len(df):,}** diamantes")
st.dataframe(df.head())

# Barra lateral com filtros
st.sidebar.header("🔍 Filtros")

# Filtro por corte (multiselect)
cortes_selecionados = st.sidebar.multiselect(
    "Corte",
    options=df['cut'].unique(),
    default=df["cut"].unique()
)

# Filtro por faixa de preço (slider)
preco_min, preco_max = st.sidebar.slider(
    "Faixa de preço (USD)",
    min_value=int(df['price'].min()),
    max_value=int(df['price'].max()),
    value=(int(df["price"].min()), int(df["price"].max()))
)

# Aplica os filtros
df_filtrado = df[
    (df["cut"].isin(cortes_selecionados)) &
    (df["price"] >= preco_min) &
    (df["price"] <= preco_max)
]

st.write(f"**{len(df_filtrado):,}** diamantes após o filtro")
st.dataframe(df_filtrado.head(10))

st.markdown("---")

# Métricas em destaque (cards)
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de diamantes", f"{len(df_filtrado):,}")
col2.metric("Preço médio", f"$ {df_filtrado['price'].mean():,.0f}")
col3.metric("Quilates médio", f"{df_filtrado['carat'].mean():.2f}")
col4.metric("Preço máximo", f"$ {df_filtrado['price'].max():,.0f}")

st.markdown("---")

# Gráficos lado a lado
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("Distribuição de preços")
    fig, ax = plt.subplots()
    sns.histplot(df_filtrado['price'], bins=40, ax=ax, color='steelblue')
    ax.set_xlabel("Preço (USD)")
    st.pyplot(fig)

with col_dir:
    st.subheader("Preço médio por corte")
    fig2, ax2 = plt.subplots()
    df_filtrado.groupby('cut', observed=True)['price'].mean().plot(kind='bar', ax=ax2, color='coral')
    ax2.set_ylabel("Preço médio (USD)")
    ax2.set_xlabel("")
    plt.xticks(rotation=45)
    st.pyplot(fig2)