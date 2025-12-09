# Projeto 6 - Versionamento e Controle de Dados em Pipelines CI/CD com Github Actions e Kubernetes

# Imagem base mais estável
FROM python:3.12-slim

# Atualizar sistema e instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Pasta de trabalho
WORKDIR /app

# Copia o arquivo para a imagem
COPY requirements.txt .

# Executa a instalação das dependências com cache otimizado
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia os demais arquivos para o container
COPY . .

# Exposição da porta do Streamlit
EXPOSE 8501

# Executa o Streamlit
CMD ["streamlit", "run", "appaivk.py", "--server.port=8501", "--server.address=0.0.0.0"]
