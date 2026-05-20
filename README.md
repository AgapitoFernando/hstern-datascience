# HStern Data Science & Gen AI — Plano de Estudos

Repositório de estudos criado como preparação para o estágio em Ciência de Dados e IA Generativa no Núcleo de IA da HStern Joalheiros.

**Autor:** Fernando Agapito da Veiga
**Curso:** Ciência da Computação — Faculdade Descomplica (3º período)
**Formação anterior:** Design de Joias — UVA (2012)
**Experiência:** Ourives autônomo desde 2004

---

## Estrutura do repositório

```
hstern-datascience/
  semana1/
    dia1_pandas.ipynb
  semana2/
  README.md
  .gitignore
```

---

# Diário de estudos

## Dia 1 — Introdução ao Pandas

### Conceitos aprendidos

#### O que é o Pandas
Biblioteca Python para manipulação e análise de dados tabulares. Funciona como um Excel dentro do Python, porém automatizável e muito mais poderoso. O nome vem de **Pan**el **Da**ta, termo da econometria.

#### Estruturas principais
- **Series** — uma única coluna de dados com índice
- **DataFrame** — tabela completa com linhas e colunas, composta por Series

#### O que é um Jupyter Notebook
Documento interativo que mistura código, resultados e texto explicativo em blocos chamados células. Formato padrão em Data Science — permite explorar dados de forma incremental, executando um bloco por vez e vendo o resultado imediatamente.

---

### Ambiente de desenvolvimento

#### Ferramentas utilizadas
- **macOS** com terminal **zsh**
- **Python 3** (no Mac, o comando é `python3`)
- **VS Code** com extensões: Python, Pylance, Python Debugger, Python Environments, Jupyter
- **pip** — gerenciador de pacotes do Python (dentro do venv, funciona sem o `3`)

#### Bibliotecas instaladas
| Biblioteca | Para que serve |
|---|---|
| `pandas` | Manipulação de dados tabulares |
| `matplotlib` | Gráficos e visualizações |
| `seaborn` | Gráficos estatísticos mais elaborados |
| `plotly` | Gráficos interativos |
| `scikit-learn` | Machine Learning |
| `streamlit` | Criação de apps web com Python |
| `jupyter` | Notebooks interativos |

---

### Comandos de terminal

#### Navegação e diretórios
```bash
# Navegar até uma pasta (no Mac, pasta Documentos em português)
cd ~/Documentos/projetos/hstern-datascience

# Criar estrutura de pastas de uma vez só
# -p significa "parents" — cria todas as pastas intermediárias sem erro
mkdir -p ~/Documentos/projetos/hstern-datascience/semana1
```

#### Ambiente virtual
```bash
# Criar o ambiente virtual (isolamento de pacotes por projeto)
python3 -m venv .venv

# Ativar o ambiente virtual (aparece "Py hstern-datascience" no terminal)
source .venv/bin/activate

# Instalar todas as bibliotecas de uma vez
pip install pandas matplotlib seaborn plotly scikit-learn streamlit jupyter

# Atualizar o pip
pip install --upgrade pip
```

> **Por que usar ambiente virtual?** Isola os pacotes de cada projeto, evitando conflitos de versão entre projetos diferentes.

#### Git — controle de versão
```bash
# Inicializar repositório Git na pasta atual
git init

# Renomear branch para "main" (padrão atual do mercado)
git branch -m main

# Ver arquivos rastreados/não rastreados
git status

# Adicionar todos os arquivos para o próximo commit
git add .

# Criar um commit com mensagem descritiva
git commit -m "Dia 1: introducao ao Pandas com dataset de joalheria"

# Verificar configurações globais do Git
git config --global user.name
git config --global user.email

# Conectar repositório local ao GitHub
git remote add origin https://github.com/AgapitoFernando/hstern-datascience.git

# Subir o projeto para o GitHub pela primeira vez
git push -u origin main
```

#### .gitignore
Arquivo que diz ao Git quais arquivos ignorar. Criado com:
```bash
echo ".venv/" > .gitignore    # > cria/substitui o arquivo
echo ".DS_Store" >> .gitignore # >> adiciona linha sem apagar o resto
```

Itens ignorados neste projeto:
- `.venv/` — ambiente virtual (pesado, cada um recria o seu)
- `.DS_Store` — arquivo oculto criado automaticamente pelo macOS

---

### Comandos Pandas aprendidos

#### Criando um DataFrame
```python
import pandas as pd

dados = {
    "produto": ["Anel", "Colar", "Brinco", "Pulseira"],
    "metal": ["Ouro 18k", "Prata", "Ouro 18k", "Prata"],
    "preco": [1200, 450, 890, 320],
    "estoque": [5, 12, 3, 8]
}

df = pd.DataFrame(dados)
```

#### Explorando o DataFrame
```python
df.shape        # Dimensões: (linhas, colunas) → (4, 4)
df.info()       # Raio-x: tipos de dados, valores nulos, memória
df.describe()   # Estatísticas: média, desvio padrão, min, max, quartis
```

#### Selecionando dados
```python
df["preco"]                      # Seleciona uma coluna (retorna Series)
df[df["metal"] == "Ouro 18k"]   # Filtra linhas por condição
df[df["preco"] == df["preco"].max()]  # Linha com o valor máximo
```

#### Análises agrupadas
```python
# Preço médio por tipo de metal
df.groupby("metal")["preco"].mean()
```

#### Criando novas colunas
```python
# Coluna calculada a partir de outras colunas
df["valor_total"] = df["preco"] * df["estoque"]
```

#### Primeiro gráfico
```python
import matplotlib.pyplot as plt

df.plot(
    kind="bar",
    x="produto",
    y="valor_total",
    color=["gold", "silver", "gold", "silver"],
    legend=False,
    title="Valor Total em Estoque por Produto"
)

plt.ylabel("Valor (R$)")
plt.xlabel("")
plt.tight_layout()
plt.show()
```

---

### Insights gerados com os dados

- Preço médio do **Ouro 18k** (R$ 1.045) é quase 3x maior que o da **Prata** (R$ 385)
- O **Anel** é o produto mais caro (R$ 1.200)
- O **Colar de Prata**, apesar do preço menor, tem o 2º maior valor em estoque (R$ 5.400) por ter 12 unidades — insight que só aparece cruzando preço × estoque

---

### Conceitos de terminal

| Conceito | Explicação |
|---|---|
| **Diretório** | Palavra técnica para pasta |
| **Flag** | Opção de um comando, ex: `-p` em `mkdir -p` |
| **`>`** | Cria/substitui um arquivo com o conteúdo |
| **`>>`** | Adiciona uma linha ao final do arquivo |
| **Ambiente virtual** | Pasta isolada com Python e pacotes de um projeto |
| **Commit** | Snapshot do projeto em um momento, com mensagem descritiva |
| **Branch** | Linha do tempo do projeto; `main` é a principal |
| **Push** | Enviar commits locais para o repositório remoto (GitHub) |

---

### Ferramentas e formatos

| Ferramenta/Formato | O que é |
|---|---|
| **Markdown (.md)** | Formato de texto com formatação via símbolos (`#`, `**`, `-`) |
| **Jupyter Notebook (.ipynb)** | Documento interativo com código + resultados + texto |
| **VS Code** | Editor de código leve e extensível, padrão do mercado |
| **GitHub** | Plataforma de hospedagem de repositórios Git — portfólio do dev |
| **.gitignore** | Arquivo que lista o que o Git deve ignorar |

---

*Próximo: Dia 2 — Visualização de dados com matplotlib e seaborn usando dataset real de diamantes* 💎
