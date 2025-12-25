import pandas as pd
from thefuzz import fuzz, process

# 1. Carregar os dados que geramos anteriormente
df_oficial = pd.read_csv('data/base_oficial.csv')
df_entrada = pd.read_csv('data/base_entrada.csv')

# 2. Criar uma lista para facilitar a busca do TheFuzz
lista_referencia = df_oficial['nome_oficial'].tolist()

def realizar_matching(linha, escolhas, threshold=85):
    # O process.extractOne busca a melhor combinação na lista de referência
    # Ele retorna uma tupla: (Nome Encontrado, Score)
    resultado = process.extractOne(linha, escolhas, scorer=fuzz.partial_ratio)
    
    nome_encontrado, score = resultado
    
    # Lógica de decisão
    if score >= threshold:
        status = "Validado Automaticamente"
    elif score >= 60:
        status = "Revisão Necessária"
    else:
        status = "Não Encontrado"
        
    return pd.Series([nome_encontrado, score, status])

# 3. Aplicar a lógica na base de entrada
print("Iniciando o processamento de limpeza de dados...")

df_entrada[['sugestao_oficial', 'confianca_score', 'status_validacao']] = df_entrada['nome_digitado'].apply(
    lambda x: realizar_matching(x, lista_referencia)
)

# 4. Exibir o resultado final organizado
df_final = df_entrada.sort_values(by='confianca_score', ascending=False)
print("\n--- RESULTADO DO PIPELINE DE DATA QUALITY ---")
print(df_final)

# 5. Exportar para mostrar ao gestor
df_final.to_csv('data/relatorio_limpeza.csv', index=False)

import matplotlib.pyplot as plt

# Criar um gráfico simples de barras
df_final['status_validacao'].value_counts().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Saúde da Base de Dados - Validação Fuzzy')
plt.xlabel('Status')
plt.ylabel('Quantidade de Registros')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('status_limpeza.png') # Salva a imagem para o seu README do Git
plt.show()