import duckdb
import pandas as pd
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title='Observatório Climático Local', page_icon='🌤️', layout='wide'
)

st.title('🌤️ Observatório Climático Local')
st.markdown(
    'Painel analítico integrado com DuckDB para monitoramento meteorológico'
    ' dos últimos 30 dias.'
)

# Conecta ao banco DuckDB criado anteriormente (modo leitura)
conn = duckdb.connect('clima_observatorio.duckdb', read_only=True)

# 1. Carrega os dados da tabela principal para um DataFrame
df_clima = conn.execute('SELECT * FROM clima_diario ORDER BY data').fetchdf()

# Fecha a conexão com o banco
conn.close()

# Exibe o nome da cidade em destaque
cidade_nome = (
    df_clima['cidade'].iloc[0] if not df_clima.empty else 'Localidade'
)
st.subheader(f'📍 Localidade Analisada: {cidade_nome}')

# 2. Cálculo dos Indicadores (KPIs)
if not df_clima.empty:
  media_temp_min = df_clima['temperatura_min'].mean()
  media_temp_max = df_clima['temperatura_max'].mean()
  total_precipitacao = df_clima['precipitacao'].sum()
  dias_chuva = (df_clima['precipitacao'] > 0.0).sum()

  # Exibe os KPIs em colunas no painel
  col1, col2, col3, col4 = st.columns(4)
  col1.metric('Temp. Mínima Média', f'{media_temp_min:.1f} °C')
  col2.metric('Temp. Máxima Média', f'{media_temp_max:.1f} °C')
  col3.metric('Chuva Acumulada', f'{total_precipitacao:.1f} mm')
  col4.metric('Dias com Chuva', f'{dias_chuva} dias')

  st.divider()

  # 3. Gráficos e Visualizações (Exigência do projeto)
  st.subheader('📈 Evolução das Temperaturas (Máxima e Mínima)')
  df_grafico_temp = df_clima.set_index('data')[
      ['temperatura_max', 'temperatura_min']
  ]
  st.line_chart(df_grafico_temp)

  st.subheader('🌧️ Precipitação Diária Acumulada')
  df_grafico_chuva = df_clima.set_index('data')['precipitacao']
  st.bar_chart(df_grafico_chuva)

  st.divider()

  # 4. Tabela de Dados Detalhados
  st.subheader('📋 Tabela de Dados Brutos Tratados')
  st.dataframe(df_clima, use_container_width=True)

else:
  st.warning(
      'Nenhum dado encontrado no banco DuckDB. Execute o script de carga'
      ' primeiro.'
  )