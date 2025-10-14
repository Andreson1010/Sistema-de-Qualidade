# Projeto 6 - Versionamento e Controle de Dados em Pipelines CI/CD com Github Actions e Kubernetes

# Imports
import streamlit as st
import joblib
import numpy as np

# Carregar o modelo
modelo_qualidade = joblib.load("modelos/modelo_qualidade_aivk.pkl")

# Configuração da página do Streamlit
st.set_page_config(page_title="Agência de IA Aivoraq", page_icon=":100:", layout="wide")

# Barra lateral com instruções
st.sidebar.title("Instruções")
st.sidebar.write("""
Esta aplicação prevê se um produto alimentar passou ou não no teste de qualidade.

Informe os dados coletados durante o processo de fabricação:

- **Peso (g)**
- **Temperatura de Fabricação (°C)**
- **pH do Produto**
- **Nível de Umidade da Sala de Produção (%)**
- **Tempo de Cozimento (minutos)**

Após inserir os valores, clique em **Prever**.
""")

# Botão de suporte na barra lateral
if st.sidebar.button("Suporte"):
    st.sidebar.write("Dúvidas? Envie um e-mail para: suporte@aivoraq.com.br")

# Título centralizado
st.title("Agência de IA Aivoraq - Controle de Qualidade")
st.title("Previsão de Qualidade do Produto")

# Campos para entrada dos dados
st.write("Insira os dados do produto:")

col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("Peso (g)", value=250.0)
    temperatura_interna = st.number_input("Temperatura de Fabricação (°C)", value=80.0)
    ph = st.number_input("pH do Produto", min_value=3.0, max_value=8.0, value=5.0)

with col2:
    nivel_umidade = st.number_input("Nível de Umidade da Sala de Produção (%)", value=15.0)
    tempo_cozimento = st.number_input("Tempo de Cozimento (minutos)", value=60.0)

# Botão de previsão
if st.button("Prever"):

    input_array = np.array([[peso, temperatura_interna, ph, nivel_umidade, tempo_cozimento]])
    prediction = modelo_qualidade.predict(input_array)
    prediction_proba = modelo_qualidade.predict_proba(input_array)[0]

    if prediction[0] == 1:
        st.success("✅ **Produto APROVADO no teste de qualidade!**")
    else:
        st.warning("❌ **Produto REPROVADO no teste de qualidade.**")

    st.subheader("Probabilidade por classe:")
    st.write(f"- **Produto Reprovado:** {prediction_proba[0]*100:.2f}%")
    st.write(f"- **Produto Aprovado:** {prediction_proba[1]*100:.2f}%")


