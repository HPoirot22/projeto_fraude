# projeto_fraude

Projeto para detecção de fraude em transações financeiras. O repositório contém código, documentação e um exemplo de dado em `data/sample.csv`, mas **os datasets completos não estão versionados** por serem muito grandes para o GitHub.

## Estrutura do repositório

```text
projeto_fraude/
├── .gitignore
├── LICENSE
├── README.md
├── data/
│   ├── raw/                # Dados brutos locais (não estão no repositório)
│   ├── processed/          # Dados processados locais (não estão no repositório)
│   └── sample.csv          # Exemplo pequeno disponível no repositório
├── src/                   # Código do projeto
└── .venv/                 # Ambiente virtual local (ignorado pelo Git)
```

## Dados

Os arquivos completos de dados `data/raw/fraudTrain.csv` e `data/processed/dados_fraude_sparkov.csv` não são incluídos no repositório porque excedem o limite de tamanho do GitHub. Use o arquivo `data/sample.csv` como exemplo do formato de dados.

Coloque seus dados locais na pasta:
- `data/raw/` para o dataset bruto
- `data/processed/` para o dataset já tratado

## Instruções de uso

1. Crie um ambiente virtual:

```bash
python -m venv .venv
```

2. Ative o ambiente:

```bash
source .venv/Scripts/activate
```

3. Instale dependências (caso haja `requirements.txt`):

```bash
pip install -r requirements.txt
```

4. Execute seus scripts ou pipeline localmente.

## Observações

- O repositório não contém os dados grandes por limitação do GitHub.
- `data/sample.csv` deve permanecer no repositório para servir de exemplo de formato.
- A pasta `data/` está ignorada no Git, exceto pelo arquivo `data/sample.csv`.
