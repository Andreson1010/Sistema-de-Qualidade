# Projeto 6 - Versionamento e Controle de Dados em Pipelines CI/CD com Github Actions e Kubernetes

# Imports
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
from datetime import datetime

# Gerar dados fictícios com valores realistas
np.random.seed(42)

peso = np.random.uniform(100, 500, 1250)
temperatura_interna = np.random.uniform(60, 100, 1250)
ph = np.random.uniform(3.5, 7.5, 1250)
nivel_umidade = np.random.uniform(5, 30, 1250)
tempo_cozimento = np.random.uniform(10, 120, 1250)

# Variável alvo simulando se o produto passou no teste de qualidade ou não
qualidade = ((temperatura_interna >= 75) & ((ph >= 4.0) & (ph <= 6.5)) & 
             (nivel_umidade < 20) & ((tempo_cozimento >= 30) & (tempo_cozimento <= 90))).astype(int)

# Preparar dataset
X = pd.DataFrame({
    "peso": peso,
    "temperatura_interna": temperatura_interna,
    "ph": ph,
    "nivel_umidade": nivel_umidade,
    "tempo_cozimento": tempo_cozimento
})

y = qualidade

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Avaliar o modelo
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Acurácia: {accuracy:.2f}")

# Versionamento automático do arquivo .pkl com timestamp (backup das versões anteriores)
modelo_dir = "modelos"
os.makedirs(modelo_dir, exist_ok=True)

# Backup do modelo anterior, caso exista
arquivo_final = os.path.join(modelo_dir, "modelo_qualidade_aivk.pkl")
if os.path.exists(arquivo_final):
    backup_nome = datetime.now().strftime("modelo_qualidade_aivk_%Y%m%d_%H%M%S.pkl")
    os.rename(arquivo_final, os.path.join(modelo_dir, backup_nome))

# Salvar o modelo ajustado sempre com o mesmo nome
joblib.dump(model, arquivo_final)
print(f"Modelo salvo como: {arquivo_final}")
