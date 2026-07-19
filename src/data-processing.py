import os
import sys
import pandas as pd
import numpy as np

def carregar_dados(caminho_arquivo):
    """Carrega o dataset bruto do simulador Sparkov."""
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado em: {caminho_arquivo}.")
    
    print(f"[*] Lendo os dados de: {caminho_arquivo}...")
    # Lendo apenas colunas essenciais para otimizar a memória, se o arquivo for muito grande
    return pd.read_csv(caminho_arquivo)

def pipeline_tratamento(df):
    """Executa a limpeza avançada e engenharia de recursos voltada para negócio."""
    print("[*] Iniciando o pipeline de tratamento de dados de fraude...")
    df_clean = df.copy()
    
    # 1. Tratamento de Datas e Horários (Crucial para análises temporais no BI)
    print("[*] Processando variáveis temporais...")
    df_clean['trans_date_trans_time'] = pd.to_datetime(df_clean['trans_date_trans_time'])
    
    # Extraindo inteligência de tempo
    df_clean['hora_transacao'] = df_clean['trans_date_trans_time'].dt.hour
    df_clean['dia_semana'] = df_clean['trans_date_trans_time'].dt.day_name()
    
    # Criar uma flag se a transação ocorreu de madrugada (horário crítico para fraudes)
    df_clean['is_madrugada'] = np.where((df_clean['hora_transacao'] >= 0) & (df_clean['hora_transacao'] <= 5), 1, 0)
    
    # 2. Cálculo de Idade do Cliente (com base na data de nascimento 'dob')
    print("[*] Calculando perfis demográficos...")
    df_clean['dob'] = pd.to_datetime(df_clean['dob'])
    df_clean['idade_cliente'] = df_clean['trans_date_trans_time'].dt.year - df_clean['dob'].dt.year
    
    # 3. Engenharia de Recursos de Negócio (Categorização)
    # Traduzindo e limpando categorias de gastos para o Power BI
    mapa_categorias = {
        'misc_net': 'Internet/Miscelânea', 'entertainment': 'Entretenimento', 
        'food_dining': 'Alimentação/Restaurantes', 'gas_transport': 'Combustível/Transporte',
        'grocery_net': 'Supermercado online', 'grocery_pos': 'Supermercado físico',
        'health_fitness': 'Saúde/Academia', 'home': 'Casa/Decoração', 
        'kids_pets': 'Crianças/Pets', 'misc_pos': 'Shopping/Variados', 
        'personal_care': 'Cuidados Pessoais', 'shopping_net': 'E-commerce', 
        'shopping_pos': 'Lojas Físicas', 'travel': 'Viagens'
    }
    df_clean['categoria_pt'] = df_clean['category'].map(mapa_categorias).fillna(df_clean['category'])
    
    # Criando faixas de valor consistentes
    condicoes = [
        (df_clean['amt'] <= 20),
        (df_clean['amt'] > 20) & (df_clean['amt'] <= 100),
        (df_clean['amt'] > 100) & (df_clean['amt'] <= 500),
        (df_clean['amt'] > 500)
    ]
    escolhas = ['1. Pequeno (Até 20)', '2. Médio (20-100)', '3. Alto (100-500)', '4. Altíssimo (>500)']
    df_clean['faixa_valor'] = np.select(condicoes, escolhas, default='Não Identificado')
    
    # Status legível para o Dashboard
    df_clean['status_fraude'] = df_clean['is_fraud'].map({0: 'Legítima', 1: 'Fraude'})
    
    # 4. Seleção e Renomeação de Colunas para Produção
    # Descartamos colunas de alta cardinalidade desnecessárias para o dashboard (como nº do cartão, nome completo)
    # para reduzir drasticamente o tamanho do arquivo final.
    colunas_finais = {
        'trans_date_trans_time': 'data_hora',
        'merchant': 'estabelecimento',
        'categoria_pt': 'categoria',
        'amt': 'vlr_transacao',
        'gender': 'genero_cliente',
        'city': 'cidade',
        'state': 'estado',
        'job': 'profissao_cliente',
        'is_fraud': 'is_fraud',
        'status_fraude': 'status_fraude',
        'hora_transacao': 'hora_transacao',
        'dia_semana': 'dia_semana',
        'is_madrugada': 'is_madrugada',
        'idade_cliente': 'idade_cliente',
        'faixa_valor': 'faixa_valor'
    }
    
    df_final = df_clean[list(colunas_finais.keys())].rename(columns=colunas_finais)
    
    print("[+] Pipeline concluído com sucesso!")
    return df_final

def exportar_dados(df, diretorio_saida, nome_arquivo="dados_fraude_sparkov.csv"):
    """Salva os dados limpos e otimizados."""
    os.makedirs(diretorio_saida, exist_ok=True)
    caminho_final = os.path.join(diretorio_saida, nome_arquivo)
    
    print(f"[*] Exportando base tratada para: {caminho_final}...")
    df.to_csv(caminho_final, index=False)
    print(f"[+] Sucesso! {len(df)} linhas processadas prontas para o Power BI.")

if __name__ == "__main__":
    # Ajuste o nome caso seu arquivo tenha outro nome (ex: fraudTrain.csv)
    CAMINHO_BRUTO = "data/raw/fraudTrain.csv" 
    DIRETORIO_PROCESSADO = "data/processed"
    
    try:
        dados_brutos = carregar_dados(CAMINHO_BRUTO)
        dados_tratados = pipeline_tratamento(dados_brutos)
        exportar_dados(dados_tratados, DIRETORIO_PROCESSADO)
        
    except Exception as e:
        print(f"[-] Erro crítico: {e}", file=sys.stderr)