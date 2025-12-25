import pandas as pd
import random

# 1. Criamos a nossa "Base Oficial" (O que seria o mundo ideal)
base_oficial = [
    'Google Brasil Internet Ltda', 
    'Apple Computer Brasil', 
    'Microsoft Informática', 
    'Amazon Serviços de Varejo', 
    'Netflix Entretenimento',
    'Tesla Brazil',
    'Samsung Eletrônica'
]

# 2. Criamos a "Base Suja" (Simulando erros de digitação, abreviações e falta de dados)
base_suja = [
    'Gogle Brasil',                # Erro de digitação
    'Apple Inc',                   # Sufixo diferente
    'Microsft Informática',        # Letra faltando
    'Amazon Varejo',               # Nome incompleto
    'Netlix',                      # Erro de digitação
    'Tesla Br',                    # Abreviação
    'Samsung',                     # Nome genérico
    'Google Brasil Ltda',          # Variação de sufixo
    'Apple Brasil'                 # Variação regional
]

# Transformando em DataFrames
df_oficial = pd.DataFrame(base_oficial, columns=['nome_oficial'])
df_entrada = pd.DataFrame(base_suja, columns=['nome_digitado'])

# Salvando para você usar no projeto
df_oficial.to_csv('base_oficial.csv', index=False)
df_entrada.to_csv('base_entrada.csv', index=False)

print("Arquivos 'base_oficial.csv' e 'base_entrada.csv' gerados com sucesso!")