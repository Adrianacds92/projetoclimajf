import duckdb

# 1. Conecta ao banco de dados DuckDB que já está salvo na pasta
conn = duckdb.connect('clima_observatorio.duckdb', read_only=True)

print('EXECUTANDO CONSULTAS SQL NO DUCKDB')

# 2. Escreve a consulta SQL pura (exemplo: selecionar as 5 primeiras linhas)
sql_query = """
    SELECT 
        cidade,
        data,
        temperatura_max,
        temperatura_min,
        precipitacao
    FROM clima_diario
    WHERE precipitacao > 0.0
    ORDER BY data DESC
    LIMIT 5;
"""

# 3. Executa a consulta SQL e converte o resultado para o formato Pandas DataFrame
resultado_df = conn.execute(sql_query).fetchdf()

# 4. Mostra o resultado na tela
print(resultado_df)

# Fecha a conexão com o banco
conn.close()