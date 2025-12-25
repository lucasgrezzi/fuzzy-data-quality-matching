# 🚀 Corporate Data Linkage & Entity Resolution Pipeline

![Status](https://img.shields.io/badge/status-Sprint_01-success)
![Focus](https://img.shields.io/badge/focus-Data_Quality-orange)
![Tech](https://img.shields.io/badge/tech-Python_|_Pandas_|_TheFuzz-blue)

## 📋 Visão Geral
Este repositório contém o primeiro módulo de uma **cadeia de modelagem de dados** transversal para a empresa. O objetivo é utilizar inteligência computacional para padronizar e validar dados de clientes, eliminando duplicidades e garantindo a integridade da base para modelos de **Atribuição de Vendas** e **Retenção**.

## 🎯 O Problema de Negócio
A fragmentação de dados entre diferentes sistemas (CRM, ERP, Planilhas) gera nomes de clientes inconsistentes. 
- **Exemplo:** "Google", "Gogle Brasil" e "Google Brasil Ltda" são tratados como entidades diferentes.
- **Consequência:** Falha na atribuição de vendas e visão distorcida do comportamento do cliente.

## 🛠️ Solução Técnica: Fuzzy Matching
Implementamos um pipeline que utiliza a **Distância de Levenshtein** (via biblioteca `TheFuzz`) com foco no algoritmo `partial_ratio`.

### Diferenciais do Algoritmo:
- **Resiliência a Erros:** Detecta erros de digitação comuns (ex: "Gogle").
- **Ignora Sufixos:** Consegue identificar que "Apple" e "Apple Inc" são a mesma entidade.
- **Automação Segura:** Define níveis de confiança (Thresholds) para decidir o que é automático e o que requer revisão.

## 📂 Estrutura do Projeto
- `base_oficial.csv`: Fonte da verdade (Master Data).
- `base_entrada.csv`: Dados brutos a serem validados.
- `main.py`: Script principal de processamento.
- `relatorio_limpeza.csv`: Output final com scores de confiança.

## 💻 Como Funciona (Pipeline)

1. **Cálculo de Similaridade:** Compara cada entrada bruta contra a base oficial.
2. **Atribuição de Score:** Gera uma nota de 0 a 100 baseada na semelhança.
3. **Classificação Automática:**
    - **Score > 90:** Validação Automática (Alta Confiança).
    - **Score entre 60 e 90:** Revisão Manual Necessária.
    - **Score < 60:** Registro Não Encontrado.

## 📈 Impacto e ROI
- **Eficiência:** Redução de 80% no tempo de conferência manual de dados.
- **Confiabilidade:** Base 100% saneada para os próximos modelos de Atribuição e LTV.
- **Escalabilidade:** Estrutura pronta para ser integrada em Sprints ágeis de 2 semanas.

---
*Projeto desenvolvido como parte da iniciativa de Data Science para otimização de processos corporativos.*
