# Terminal & Git — Referência Rápida

---

## Terminal (zsh no macOS)

### Navegação

```bash
cd ~/Documentos/projetos/hstern-datascience   # entra na pasta do projeto
ls                                             # lista arquivos e pastas
ls ~/.kaggle/                                  # lista pasta oculta específica
mkdir -p pasta/subpasta                        # cria pastas (e intermediárias se não existirem)
mv origem destino                              # move ou renomeia arquivo
rm -r pasta/                                   # remove pasta e todo seu conteúdo
```

> `-p` em `mkdir` = "parents" — cria todas as pastas do caminho sem erro se já existirem.

### Redirecionamento de texto

```bash
echo ".venv/" > .gitignore     # cria/substitui arquivo com o conteúdo
echo ".DS_Store" >> .gitignore # adiciona linha ao final sem apagar o resto
```

### Permissões

```bash
chmod 600 ~/.kaggle/access_token   # apenas o dono pode ler/escrever — usado em arquivos com chaves privadas
```

### Conceitos úteis

| Conceito | Explicação |
|----------|------------|
| `~` | Atalho para a pasta home do usuário (`/Users/fernandoagapito`) |
| Diretório | Palavra técnica para pasta |
| Flag | Opção de um comando, ex: `-p`, `-r` |
| Silêncio = sucesso | No Unix, ausência de mensagem de erro significa que funcionou |

---

## Ambiente Virtual Python

```bash
python3 -m venv .venv              # cria o ambiente virtual na pasta .venv
source .venv/bin/activate          # ativa o ambiente (aparece "Py" no terminal)
pip install pandas matplotlib ...  # instala pacotes dentro do ambiente ativo
pip install --upgrade pip          # atualiza o pip
```

> **Por que usar?** Isola os pacotes de cada projeto — evita conflitos de versão entre projetos diferentes.

---

## Git — Controle de Versão

### Configuração inicial (feita uma vez)

```bash
git config --global user.name "Fernando Agapito"
git config --global user.email "seu@email.com"
git init                          # inicializa repositório na pasta atual
git branch -m main                # renomeia branch para "main"
git remote add origin https://github.com/AgapitoFernando/hstern-datascience.git
git push -u origin main           # primeiro push — conecta local ao remoto
```

### Uso diário

```bash
git status                        # mostra arquivos modificados/novos
git add .                         # adiciona tudo para o próximo commit
git commit -m "mensagem clara"    # registra snapshot com descrição
git push                          # envia commits para o GitHub
```

### Conceitos

| Conceito | Explicação |
|----------|------------|
| Repositório | Pasta com histórico de versões rastreado pelo Git |
| Commit | Snapshot do projeto em um momento, com mensagem descritiva |
| Branch | Linha do tempo do projeto — `main` é a principal |
| Push | Enviar commits locais para o repositório remoto (GitHub) |
| `.gitignore` | Arquivo que lista o que o Git deve ignorar |

### .gitignore deste projeto

```
.venv/      # ambiente virtual — pesado, cada um recria o seu
.DS_Store   # arquivo oculto criado automaticamente pelo macOS
```

---

## Kaggle API

```bash
# Instalar o cliente
pip install kagglehub

# Configurar token de autenticação (feito uma vez)
mkdir -p ~/.kaggle && echo SEU_TOKEN > ~/.kaggle/access_token && chmod 600 ~/.kaggle/access_token

# Verificar se está configurado
ls ~/.kaggle/
```

```python
# Baixar dataset dentro do notebook
import kagglehub, shutil

path = kagglehub.dataset_download("usuario/nome-do-dataset")
shutil.copy(f"{path}/arquivo.csv", "../data/arquivo.csv")
```
