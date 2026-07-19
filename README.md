<img width="1316" height="722" alt="image" src="https://github.com/user-attachments/assets/2379c584-9cec-469d-bb40-2cfd1f67f107" />



# 🛡️ Análise de Risco de Fraude Financeira

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Tratamento_de_Dados-150458.svg)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Engenharia_de_Features-F7931E.svg)](https://scikit-learn.org/)

Este projeto apresenta um pipeline analítico de ponta a ponta focado na identificação e monitoramento de risco de fraude em transações financeiras. A solução engloba o tratamento estatístico e a engenharia de recursos (*Feature Engineering*) utilizando Python, culminando no desenvolvimento de um dashboard estratégico e operacional no Power BI para suporte à tomada de decisão.

---

## 📌 Contexto de Negócio & Desafio

A prevenção e o monitoramento de fraudes são pilares críticos no setor financeiro para mitigar prejuízos operacionais (*chargebacks*) e proteger a experiência do cliente. O principal desafio analítico reside no extremo desbalanceamento dos dados, onde as transações fraudulentas representam uma fração mínima do volume total.

Este projeto foi desenvolvido utilizando dados simulados de transações de cartão de crédito (baseados no dataset público *Fraud Detection* do Kaggle) para responder a dores reais de negócio:
1. **Comportamento Temporal:** Identificar se janelas específicas (como transações na madrugada) possuem maior concentração de risco.
2. **Perfil Demográfico:** Avaliar o impacto da idade e do perfil do cliente no volume de fraudes.
3. **Visão de Lojistas:** Mapear quais estabelecimentos comerciais acumulam a maior representatividade de perda financeira.
4. **Categorias de Risco:** Ranquear os segmentos de consumo com maior índice de vulnerabilidade.

---

## 🛠️ Arquitetura da Solução

O fluxo do projeto foi desenhado seguindo as melhores práticas de desenvolvimento local e organização de projetos de dados:

[Dados Brutos: CSV]
│
▼ (Python / VS Code)
[Pipeline de Limpeza & Feature Engineering]
│
▼ (Dataset Otimizado: CSV Tratado)
[Modelagem de Dados & Medidas DAX] (Power BI)
│
▼
[Dashboard Analítico de Risco] (Apresentação / Decisão)

1. **Pré-processamento (Python):** Executado localmente via VS Code com ambiente virtual isolado. Realiza a limpeza de colunas redundantes, tradução de categorias e escalonamento de variáveis financeiras sensíveis a anomalias (*outliers*) utilizando técnicas como o `RobustScaler`.
2. **Modelagem & BI (Power BI):** Consumo do dataset otimizado em Python, reduzindo drasticamente o uso de memória e processamento no Power BI. As regras de negócio e indicadores de conversão de risco foram calculados de forma performática via DAX.

---

## 🔧 Estrutura do Repositório

```text
fraude-analytics/
├── .venv/                  # Ambiente virtual local (ignorado no git)
├── data/
│   ├── raw/                # Dataset bruto original (fraudTrain.csv)
│   └── processed/          # CSV limpo e otimizado para o Power BI
├── src/
│   ├── __init__.py
│   └── data_processing.py  # Script do pipeline de automação de dados
├── .gitignore              # Proteção para não subir arquivos pesados ou locais
├── requirements.txt        # Dependências do projeto (Pandas, Numpy, Sklearn, etc.)
└── README.md               # Documentação técnica e de negócio
```
📈 Inteligência de Negócio & Fórmulas DAX
Os principais indicadores de risco foram centralizados e calculados utilizando expressões DAX customizadas:

Volumetria de Risco: Cálculo da taxa percentual de fraude ajustada para refletir o desbalanceamento real dos dados.

Perda Financeira: Mensuração do impacto financeiro total acumulado por transações confirmadas como fraude (Chargeback Potencial).

Representatividade do Lojista: Fórmula avançada para identificar a concentração de perdas por estabelecimento comercial sobre o prejuízo global da operação.

💡 Principais Insights Gerados
Padrões Noturnos: Transações de alto valor realizadas em horários críticos (como madrugadas) apresentam uma taxa de risco acentuadamente superior à média diária.

Concentração em E-commerce: Gastos voltados a compras online concentram o maior volume financeiro em risco, sugerindo a necessidade de regras de autenticação mais rígidas para o canal digital.

Assimetria de Estabelecimentos: Uma parcela reduzida de lojistas responde pela maior parte do prejuízo total, sinalizando oportunidades claras para auditorias operacionais.

🚀 Como Executar o Projeto
Instale as dependências listadas no arquivo requirements.txt dentro do seu ambiente virtual.

Coloque a base bruta na pasta data/raw/.

Execute o script src/data_processing.py para gerar a base tratada em data/processed/.

Conecte o Power BI ao arquivo processado para visualizar o dashboard.

