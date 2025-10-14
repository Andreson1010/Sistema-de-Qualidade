# Projeto 6 - Versionamento e Controle de Dados em Pipelines CI/CD com Github Actions e Kubernetes

# Imagem base
FROM python:3.12-slim

# Pasta de trabalho
WORKDIR /app

# Copia o arquivo para a imagem
COPY requirements.txt .

# Executa a instalação das dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia os demais arquivos para o container
COPY . .

# Exposição da porta do Streamlit
EXPOSE 8501

# Executa o Streamlit
CMD ["streamlit", "run", "appaivk.py", "--server.port=8501", "--server.address=0.0.0.0"]
