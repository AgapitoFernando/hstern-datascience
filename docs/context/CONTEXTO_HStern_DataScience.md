# Contexto — HStern DataScience: Do CSV ao Dashboard
**Projeto:** `hstern-datascience` | **Status:** Sessão 3 — Dia 5 completo  
**Repositório:** `~/Documents/projects/hstern-datascience` (Linux), `~/Documentos/projetos/hstern-datascience` (Mac)  
**GitHub:** https://github.com/AgapitoFernando/hstern-datascience

---

## Visão Geral
Plano de 2 semanas (14 dias) para preparação para estágio em Data Science e Gen AI na HStern Joalheiros. Foco em Python, Pandas, Machine Learning e IA Generativa.

**Objetivo educacional:** Entender conceitos profundamente, não apenas copiar soluções. Progresso didático dia por dia com notebooks e documentação.

---

## Progresso Atual

### ✅ Concluído (Dias 1-5)

**Dia 1 — Introdução ao Pandas**
- Dataset: joalheria (características de joias)
- Operações: carregamento, inspeção, estatísticas básicas
- Output: `.describe()`, `.head()`, distribuições

**Dia 2 — Visualização de Dados**
- Biblioteca: matplotlib + seaborn
- Gráficos: histogramas, scatter plots, correlação
- Dataset: diamonds (53.917 diamantes, 10 features)
- Insight: identificação de padrões visuais

**Dia 3 — Limpeza e Preparação**
- Remoção de outliers (IQR method)
- Tratamento de valores ausentes
- Dataset limpo: `diamonds_clean.csv`
- Feature engineering preparado

**Dia 4 — Regressão Linear**
- Problema: prever preço de diamante a partir de características
- Métricas: R², MSE, RMSE
- Modelo: train/test split, sklearn LinearRegression
- Acurácia: ~95% no teste

**Dia 5 — Classificação (Random Forest)**
- Problema: prever qualidade de corte (cut) — 5 categorias
- Dataset: 53.917 diamantes
- Acurácia: 77,3%
- Features mais importantes:
  - `table` (26%) — largura da mesa
  - `depth` (21%) — profundidade  
  - `x/y/z` (30%) — dimensões físicas
  - `price` (10%)
  - `color`, `clarity` — irrelevantes para prever corte
- Insight: corte é determinado por PROPORÇÕES, não cor ou clareza

---

## Estrutura do Repositório

```
hstern-datascience/
├── README.md
├── data/
│   ├── diamonds.csv          (dataset original)
│   └── diamonds_clean.csv    (após limpeza)
├── docs/
│   ├── aprendizados/         (diários dos dias)
│   │   ├── dia4_machine_learning.md
│   │   └── (mais a vir)
│   └── referencias/          (guias e links)
└── notebooks/
    ├── dia1_pandas.ipynb
    ├── dia2_visualizacao.ipynb
    ├── dia3_limpeza_dados.ipynb
    ├── dia4_machine_learning.ipynb
    └── dia5_classificacao.ipynb
```

---

## Tecnologias & Comandos

### Bibliotecas principais
- **pandas** — manipulação de dados
- **matplotlib/seaborn** — visualização
- **scikit-learn** — machine learning
- **numpy** — operações numéricas

### Ambiente virtual
```bash
# Ativar
source .venv/bin/activate

# Instalar dependências
pip install pandas matplotlib seaborn scikit-learn jupyter

# Rodar notebook
jupyter notebook notebooks/dia5_classificacao.ipynb
```

### Git workflow
```bash
git add notebooks/dia5_classificacao.ipynb
git commit -m "Dia 5: classificação com Random Forest — previsão do corte do diamante"
git push
```

---

## Próximos Passos (Dias 6-14)

| Dia | Tema | O que fazer |
|---|---|---|
| **6** | Dashboard Streamlit | Criar painel interativo com dados de diamantes |
| **7** | Revisão e GitHub | Consolidar aprendizado, organizar repositório |
| **8** | O que é Gen AI | Conceitos, LLMs, prompt engineering |
| **9** | APIs de IA | Usar OpenAI/Claude API em Python |
| **10** | Prompt Engineering | Técnicas avançadas de prompting |
| **11** | Automação com IA | Integração IA em workflows |
| **12** | NLP básico | Processamento de linguagem natural |
| **13** | Projeto integrador | Combinar tudo aprendido |
| **14** | Prep para entrevista | Mock interview + últimos detalhes |

---

## Comandos Aprendidos

### Pandas
```python
import pandas as pd
df = pd.read_csv('file.csv')
df.describe()              # Estatísticas
df.corr()                  # Correlação entre features
df['coluna'].value_counts() # Distribuição
```

### Matplotlib/Seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.hist(df['coluna'])
sns.scatterplot(data=df, x='x', y='y', hue='categoria')
```

### Scikit-learn
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)
acuracia = accuracy_score(y_test, modelo.predict(X_test))
```

---

## Pontos-chave de Aprendizado

1. **Dados sujos → Análise limpa:** A limpeza consome 70% do tempo, mas sem ela os modelos falham
2. **Visualização primeiro:** Gráficos revelam padrões que números escondem
3. **Features engineering:** Corte de diamante é PROPORÇÕES, não cor/clareza
4. **Métricas importam:** Acurácia 77% parece baixa, mas é ótima para classificação de 5 categorias
5. **Matriz de confusão fala:** "Very Good" confundido com "Premium" faz sentido no mundo real

---

## Referências

- **Kaggle dataset:** Diamonds dataset (53.917 linhas, 10 features)
- **Conceitos:** Regressão vs Classificação, Train/Test Split, Random Forest, Métricas
- **Diferencial:** Contexto de joalheria — Fernando já entende que corte é proporcional, não visual

---

## Notas Práticas

- Mac M1: Todos os notebooks rodam nativamente
- Linux Zorin: Repositório sincronizado via Git
- Documentação: Cada dia tem `.md` no `docs/aprendizados/`
- GitHub: Push diário, histórico limpo com conventional commits
