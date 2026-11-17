from datetime import datetime, timedelta
import duckdb
import pandas as pd
import requests

# Nome e local do arquivo de banco de dados (salva na pasta atual do projeto)
caminho_banco = 'clima_observatorio.duckdb'
print(f'Salvando o banco de dados localmente: {caminho_banco}')

# 1. Coleta dos dados da API Open-Meteo para Juiz de Fora (30 dias)
url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude': -21.7642,
    'longitude': -43.3504,
    'daily': [
        'temperature_2m_max',
        'temperature_2m_min',
        'precipitation_sum',
    ],
    'past_days': 30,
    'forecast_days': 1,
    'timezone': 'America/Sao_Paulo',
}

response = requests.get(url, params=params)
data = response.json()

# 2. Organiza os dados em um DataFrame do Pandas
daily_data = data['daily']
df = pd.DataFrame({
    'cidade': 'Juiz de Fora',
    'data': pd.to_datetime(daily_data['time']),
    'temperatura_max': daily_data['temperature_2m_max'],
    'temperatura_min': daily_data['temperature_2m_min'],
    'precipitacao': daily_data['precipitation_sum'],
})

# Remove valores nulos caso venham de dias incompletos
df = df.dropna()

# 3. Conecta ao DuckDB (Isso criará o arquivo 'clima_observatorio.duckdb' na pasta do seu projeto)
conn = duckdb.connect(database=caminho_banco)

# Cria a tabela principal estruturada
conn.execute("""
    CREATE TABLE IF NOT EXISTS clima_diario (
        cidade VARCHAR,
        data DATE,
        temperatura_max DOUBLE,
        temperatura_min DOUBLE,
        precipitacao DOUBLE,
        PRIMARY KEY (cidade, data)
    )
""")

# Insere ou atualiza os dados na tabela do DuckDB
conn.execute("""
    INSERT OR REPLACE INTO clima_diario 
    SELECT * FROM df
""")

print('Banco DuckDB criado e salvo com sucesso!')

# 4. Executa uma consulta rápida de teste para verificar os dados salvos
print('\n--- Amostra dos dados salvos no banco ---')
resultado = conn.execute('SELECT * FROM clima_diario LIMIT 5').fetchdf()
print(resultado)

# Fecha a conexão com o banco
conn.close()