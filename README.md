# 🌤️ Observatório Climático Local

Repositório desenvolvido para as Atividades de Estudo (AE1 e AE2) do projeto extensionista, integrando engenharia de dados, consultas analíticas e visualização interativa de métricas meteorológicas.

---

## 🎯 Sobre o Projeto

O **Observatório Climático Local** tem como objetivo coletar, processar, armazenar e disponibilizar dados meteorológicos históricos recentes de uma localidade específica (Juiz de Fora - MG), transformando dados brutos em indicadores úteis (KPIs) para a comunidade e o público-alvo.

---

## 📂 Estrutura do Repositório

- `clima_observatorio.duckdb` - Banco de dados analítico local estruturado em DuckDB.
- `import_openmeteo_requests.py` - Script Python responsável pela coleta dos dados na API Open-Meteo e carga na tabela principal.
- `app.py` - Aplicação interativa desenvolvida em Streamlit para exibição do painel analítico.
- consulta_sql.py - Consulta para exibir a tabela com as informações.
- `README.md` - Documentação oficial do projeto.

---

## 📊 Variáveis Coletadas e Dicionário de Dados

A tabela principal `clima_diario` armazena as seguintes variáveis:

1. **`cidade` (VARCHAR):** Nome da localidade monitorada.
2. **`data` (DATE):** Data de referência do registro diário.
3. **`temperatura_min` (DOUBLE):** Temperatura mínima diária registrada (°C).
4. **`temperatura_max` (DOUBLE):** Temperatura máxima diária registrada (°C).
5. **`precipitacao` (DOUBLE):** Volume de precipitação acumulada no dia (mm).

---

## 🔍 Consultas SQL e Indicadores (KPIs)

O projeto contempla quatro perguntas analíticas principais respondidas por meio de consultas executadas no DuckDB:

- **Temperatura Máxima Mínima:** Calcula a média das temperaturas mínimas do período.
- **Temperatura Mínima:** Calcula a média das temperaturas máximas do período.
- **Precipitação Acumulada Total:** Soma o volume total de chuva registrado nos 30 dias.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o Python instalado junto com as bibliotecas necessárias. No terminal, execute:

```bash
pip install duckdb pandas requests streamlit openmeteo-requests
```
