# AIVK - Sistema de Controle de Qualidade com IA

![Status do Projeto](https://img.shields.io/badge/status-em_desenvolvimento-orange)
![Licença](https://img.shields.io/badge/license-MIT-green)
![Versão](https://img.shields.io/badge/version-1.0.0-blue)

> Sistema de machine learning para previsão de qualidade de produtos alimentares, integrado com pipeline CI/CD completo usando GitHub Actions e Kubernetes.
> Neste  projeto construimos um  pipeline de  Machine  Learning utilizando  Kubernetes para  otimizar  e  escalar  a  infraestrutura necessária  para  um  modelo  de  IA. E  para  automação criaremos um pipeline de CI/CD. Sempre que houver uma nova versão de scripts no repositório Git,  o  GitHub  Actions  vai  disparar  as  ações  para  execução  do  pipeline  de  Machine  Learning  e então atualização da web app

---

## 📖 Sobre

O **AIVK** é um sistema completo de controle de qualidade que utiliza machine learning para prever se um produto alimentar passará ou não no teste de qualidade baseado em parâmetros de fabricação. O projeto demonstra boas práticas de DevOps e MLOps, com pipeline CI/CD automatizado, containerização Docker e orquestração Kubernetes.

O sistema permite que usuários insiram 5 parâmetros de processo (Peso, Temperatura, pH, Umidade e Tempo de Cozimento) e recebam previsões instantâneas sobre a aprovação/reprovação do produto, além das probabilidades associadas.

### Funcionalidades Principais

* **Interface Web Intuitiva**: Aplicação Streamlit para interação do usuário
* **Modelo de ML Treinado**: RandomForestClassifier com dataset de 1.250 amostras sintéticas
* **Pipeline CI/CD Automatizado**: GitHub Actions para build e validação automática
* **Containerização Docker**: Imagem otimizada e pronta para deploy
* **Orquestração Kubernetes**: Deploy automatizado com Minikube
* **Versionamento de Modelos**: Backup automático com timestamp

---

## 📸 Screenshots / Demonstração

### Interface da Aplicação

![Aplicação AIVK - Previsão de Qualidade do Produto](docs/Sistema_Qualidade.png)

**Descrição da Interface:**

A aplicação Streamlit apresenta uma interface intuitiva onde o usuário pode inserir os seguintes parâmetros de fabricação:

* **Peso (g)**: Peso do produto em gramas
* **Temperatura de Fabricação (°C)**: Temperatura durante o processo
* **pH do Produto**: Nível de acidez/alcalinidade
* **Nível de Umidade da Sala de Produção (%)**: Umidade do ambiente
* **Tempo de Cozimento (minutos)**: Duração do processo de cozimento

Após inserir os valores e clicar em **"Prever"**, o sistema retorna:

* ✅ **Status de Aprovação/Reprovação** do produto
* 📊 **Probabilidades por classe** (Aprovado/Reprovado)



## 🛠 Tecnologias Utilizadas

As seguintes ferramentas foram usadas na construção do projeto:

* **Linguagem Principal**: Python 3.12
* **Framework Web**: Streamlit 1.43.0
* **Machine Learning**: scikit-learn 1.6.1
* **Processamento de Dados**: Pandas 2.2.3, NumPy 2.1.3
* **Containerização**: Docker
* **Orquestração**: Kubernetes (Minikube)
* **CI/CD**: GitHub Actions + Act (teste local)
* **Gerenciador de Pacotes**: uv
* **Versionamento**: Git

---

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

* **Docker Desktop** - Instalado e em execução
* **Kubectl** - Ferramenta de linha de comando do Kubernetes
* **Minikube** - Kubernetes local para desenvolvimento
* **Python 3.12** - Linguagem de programação
* **uv** - Gerenciador de pacotes Python (alternativa rápida ao pip)
* **Git** - Controle de versão
* **Act** (Opcional) - Para testar GitHub Actions localmente

### Validações Rápidas

```bash
kubectl version --client
minikube version
python --version  # Deve retornar Python 3.12.x
uv --version
```

### Links Úteis

* Git: https://git-scm.com/
* uv: https://github.com/astral-sh/uv
* Act: https://nektosact.com/installation/index.html
* Docker: https://www.docker.com/products/docker-desktop

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para rodar o ambiente de desenvolvimento:

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/proj_6.git
cd proj_6
```

### 2. Configurar Ambiente Python

#### 2.1 Instalar uv (se ainda não tiver)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/Mac:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### 2.2 Criar ambiente virtual

```bash
uv venv
```

#### 2.3 Ativar ambiente virtual

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate
```

**Windows CMD:**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

#### 2.4 Instalar dependências

```bash
uv pip install -r requirements.txt
```

### 3. Treinar o Modelo

```bash
python treinamento/aivk_treina_modelo.py
```

O modelo será salvo em `modelos/modelo_qualidade_aivk.pkl`. Versões anteriores são automaticamente renomeadas com timestamp.

### 4. Construir Imagem Docker

Certifique-se de que o Docker Desktop está ativo, depois execute:

```bash
docker build -t aivk-p6-app:latest .
```

### 5. Configurar Kubernetes (Minikube)

#### 5.1 Iniciar cluster local

```bash
minikube start --driver=docker
kubectl config current-context  # Deve retornar: minikube
```

#### 5.2 Carregar imagem no Minikube

```bash
minikube image load aivk-p6-app:latest
```

### 6. Deploy no Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods  # Verificar status
```

### 7. Acessar a Aplicação

```bash
minikube service aivk-p6-app-service
```

O navegador será aberto automaticamente com a aplicação rodando.

---

## 📂 Estrutura de Pastas

```
proj_6/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Workflow GitHub Actions
├── docs/                      # Documentação detalhada
│   ├── PRD.md                 # Product Requirements Document
|   |-- Sistema_Qualidade.png  # Imagem da aplicação com Streamlit
├── k8s/                       # Manifestos Kubernetes
│   ├── deployment.yaml        # Configuração do Deployment
│   └── service.yaml           # Configuração do Service
├── modelos/                   # Modelos de ML treinados
│   └── modelo_qualidade_aivk.pkl
├── treinamento/               # Scripts de treinamento
│   └── aivk_treina_modelo.py
├── appaivk.py                 # Aplicação Streamlit principal
├── Dockerfile                 # Configuração do container
├── requirements.txt           # Dependências Python       
└── README.md                 # Este arquivo
```

---

## 🔄 Pipeline CI/CD

O projeto possui um workflow GitHub Actions configurado em `.github/workflows/ci-cd.yml` que é acionado automaticamente quando:

* Há um push para a branch `main`
* E há modificações em: `modelos/**`, `treinamento/**`, `appaivk.py`, `requirements.txt`, ou `Dockerfile`

O workflow executa:
1. Checkout do código
2. Instalação do Node.js e Python 3.12
3. Instalação das dependências Python
4. Treinamento do modelo de ML
5. Construção da imagem Docker
6. Validação dos manifestos Kubernetes

### Testar Localmente com Act

```bash
act push
```

Para mais detalhes sobre CI/CD, consulte: [docs/GitHub_Actions_CI_CD.md](docs/GitHub_Actions_CI_CD.md)

---

## 📚 Documentação Adicional

Documentação detalhada está disponível na pasta `docs/`:

* **[PRD.md](docs/PRD.md)** - Product Requirements Document completo
* **[Ambientes_Virtuais_Python.md](docs/Ambientes_Virtuais_Python.md)** - Guia completo sobre ambientes virtuais
* **[Docker_Kubernetes_Guia_Completo.md](docs/Docker_Kubernetes_Guia_Completo.md)** - Guia detalhado de Docker e Kubernetes
* **[GitHub_Actions_CI_CD.md](docs/GitHub_Actions_CI_CD.md)** - Documentação do pipeline CI/CD
* **[LEIAME1.txt](LEIAME1.txt)** - Guia passo a passo de instalação e configuração

---

## 🤝 Como Contribuir

1. Faça um **fork** do projeto.

2. Crie uma nova branch com as suas alterações: `git checkout -b feature/minha-feature`

3. Salve as alterações e crie uma mensagem de commit descrevendo o que você fez: `git commit -m "Feature: Minha nova feature"`

4. Envie as suas alterações: `git push origin feature/minha-feature`

5. Abra um **Pull Request**.

---

## 🐛 Troubleshooting

### Problemas Comuns

**Imagem não encontrada no Kubernetes:**
```bash
minikube image load aivk-p6-app:latest
```

**Contexto incorreto do kubectl:**
```bash
kubectl config current-context  # Deve retornar: minikube
```

**Docker inativo:**
- Abra o Docker Desktop e aguarde a inicialização completa

**Pods com erro (CrashLoopBackOff):**
```bash
kubectl get pods
kubectl describe pod <nome-do-pod>
kubectl logs <nome-do-pod>
```

Para mais informações de troubleshooting, consulte a seção 10 do [LEIAME1.txt](LEIAME1.txt).

---

## 📝 Licença

Este projeto está sob a licença MIT.

---

## 👤 Autor

Feito com ❤️ por **Equipe AIVK - Agência de IA Aivoraq** 👋🏽

**Contato:** suporte@aivoraq.com.br

---

## 🔗 Links Relacionados

* [Documentação do Streamlit](https://docs.streamlit.io/)
* [Documentação do scikit-learn](https://scikit-learn.org/)
* [Documentação do Kubernetes](https://kubernetes.io/docs/)
* [Documentação do Docker](https://docs.docker.com/)
* [Documentação do GitHub Actions](https://docs.github.com/en/actions)

