# Docker, Kubernetes e Minikube - Guia Completo

## 📚 Índice
1. [O que é Docker?](#1-o-que-é-docker)
2. [Objetivos e Benefícios do Docker](#2-objetivos-e-benefícios-do-docker)
3. [Conceitos Fundamentais](#3-conceitos-fundamentais)
4. [Construindo uma Imagem Docker - Passo a Passo](#4-construindo-uma-imagem-docker---passo-a-passo)
5. [Análise do Dockerfile do Projeto](#5-análise-do-dockerfile-do-projeto)
6. [O que é Kubernetes?](#6-o-que-é-kubernetes)
7. [O que é kubectl?](#7-o-que-é-kubectl)
   - [7.2 Instalação do kubectl](#72-instalação-do-kubectl)
8. [O que é Minikube?](#8-o-que-é-minikube)
   - [8.2 Instalação do Minikube](#82-instalação-do-minikube)
9. [Encadeamento Completo: Docker → Minikube → Kubernetes](#9-encadeamento-completo-docker--minikube--kubernetes)
10. [Comandos do Projeto](#10-comandos-do-projeto)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. O que é Docker?

### 1.1 Definição

**Docker** é uma plataforma de containerização que permite empacotar aplicações e suas dependências em **containers** leves e portáteis. Um container é uma unidade de software que contém tudo o que é necessário para executar uma aplicação: código, runtime, bibliotecas, variáveis de ambiente e arquivos de configuração.

### 1.2 Analogia Simples

Imagine que você precisa enviar um bolo para alguém:

**Sem Docker (Método Tradicional):**
- Você envia a receita
- A pessoa precisa ter todos os ingredientes, utensílios e o forno
- Pode não funcionar se a pessoa tiver ingredientes diferentes ou um forno diferente

**Com Docker:**
- Você envia o bolo já pronto em uma caixa hermética
- A pessoa só precisa abrir a caixa e o bolo funciona perfeitamente
- Funciona em qualquer lugar, independente do ambiente

### 1.3 Diferença entre Container e Máquina Virtual

| Aspecto | Container (Docker) | Máquina Virtual (VM) |
|---------|-------------------|---------------------|
| **Tamanho** | Leve (MBs) | Pesado (GBs) |
| **Inicialização** | Segundos | Minutos |
| **Recursos** | Compartilha o kernel do host | Kernel próprio |
| **Isolamento** | Processo isolado | Sistema operacional completo |
| **Uso** | Aplicações | Sistemas completos |

---

## 2. Objetivos e Benefícios do Docker

### 2.1 Objetivos Principais

1. **Portabilidade**
   - "Funciona na minha máquina" → "Funciona em qualquer máquina"
   - Aplicação roda igual em desenvolvimento, teste e produção

2. **Isolamento**
   - Cada aplicação roda em seu próprio ambiente
   - Dependências não conflitam entre aplicações

3. **Consistência**
   - Mesmo ambiente em todas as etapas do desenvolvimento
   - Reduz problemas de "funcionava antes"

4. **Escalabilidade**
   - Fácil criar múltiplas instâncias da aplicação
   - Distribuição de carga entre containers

5. **Versionamento**
   - Cada imagem pode ser versionada (tags)
   - Fácil rollback para versões anteriores

### 2.2 Benefícios Práticos

- ✅ **Desenvolvimento mais rápido**: Setup de ambiente em minutos
- ✅ **Deploy simplificado**: Uma imagem funciona em qualquer lugar
- ✅ **Recursos otimizados**: Containers são mais leves que VMs
- ✅ **CI/CD facilitado**: Integração contínua mais simples
- ✅ **Microserviços**: Facilita arquitetura de microserviços

---

## 3. Conceitos Fundamentais

### 3.1 Imagem (Image)

Uma **imagem Docker** é um template read-only usado para criar containers. É como um "molde" que contém:
- Sistema operacional base
- Aplicação
- Dependências
- Configurações

**Exemplo:** `aivk-p6-app:latest` é uma imagem que contém Python 3.12, Streamlit e sua aplicação.

### 3.2 Container

Um **container** é uma instância em execução de uma imagem. É como uma "cópia viva" da imagem rodando.

**Analogia:**
- **Imagem** = Receita de bolo (template)
- **Container** = Bolo assado (instância em execução)

### 3.3 Dockerfile

O **Dockerfile** é um arquivo de texto que contém instruções para construir uma imagem Docker. É como uma "receita" que o Docker segue para criar a imagem.

### 3.4 Docker Hub / Registry

Repositório onde imagens Docker são armazenadas e compartilhadas. É como o "GitHub das imagens Docker".

---

## 4. Construindo uma Imagem Docker - Passo a Passo

### 4.1 Pré-requisitos

Antes de construir uma imagem, você precisa:

1. **Docker Desktop instalado e rodando**
   - Verifique se está ativo (ícone na bandeja do sistema)
   - Windows: Docker Desktop deve estar em execução

2. **Dockerfile no diretório do projeto**
   - Arquivo chamado `Dockerfile` (sem extensão)
   - Contém as instruções de build

3. **Arquivos do projeto prontos**
   - Código da aplicação
   - Dependências documentadas (requirements.txt)

### 4.2 Comando de Build

No diretório do projeto, execute:

```bash
docker build -t aivk-p6-app:latest .
```

### 4.3 Análise do Comando

Vamos quebrar o comando em partes:

| Parte | Função |
|-------|--------|
| `docker build` | Comando para construir uma imagem Docker |
| `-t aivk-p6-app:latest` | Define o nome e tag da imagem |
| `.` | Especifica o contexto de build (diretório atual) |

**Detalhamento:**
- `-t` ou `--tag`: Define o nome e tag da imagem
- `aivk-p6-app`: Nome da imagem
- `latest`: Tag (versão) da imagem
- `.`: Contexto de build (onde está o Dockerfile)

### 4.4 O que Acontece Durante o Build?

1. **Docker lê o Dockerfile**
   - Procura por um arquivo chamado `Dockerfile` no diretório atual
   - Lê as instruções linha por linha

2. **Executa as instruções**
   - Segue cada comando do Dockerfile
   - Cria camadas (layers) da imagem
   - Baixa dependências se necessário

3. **Cria a imagem**
   - Gera uma imagem Docker com o nome especificado
   - Armazena localmente no Docker

4. **Armazena localmente**
   - A imagem fica disponível no Docker local
   - Pode ser usada para criar containers

### 4.5 Processo Visual

```
Diretório do Projeto
├── Dockerfile          ← Docker lê este arquivo
├── appaivk.py         ← Copiado para a imagem
├── requirements.txt    ← Usado para instalar dependências
└── modelos/           ← Copiado para a imagem
    └── modelo_qualidade_aivk.pkl

         ↓ docker build

    Imagem Docker
    aivk-p6-app:latest
    ├── Python 3.12
    ├── Dependências instaladas
    ├── Código da aplicação
    └── Modelo treinado
```

---

## 5. Análise do Dockerfile do Projeto

Vamos analisar o Dockerfile do projeto linha por linha:

### 5.1 Dockerfile Completo

```dockerfile
# Projeto 6 - Versionamento e Controle de Dados em Pipelines CI/CD
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
```

### 5.2 Explicação Linha por Linha

#### `FROM python:3.12-slim`
- **Função**: Define a imagem base
- **O que faz**: Usa uma imagem Python 3.12 oficial e "slim" (versão reduzida)
- **Por quê**: Imagem menor, mais rápida de baixar e construir

#### `RUN apt-get update && apt-get install -y gcc g++ && rm -rf /var/lib/apt/lists/*`
- **Função**: Instala dependências do sistema
- **O que faz**:
  - `apt-get update`: Atualiza lista de pacotes
  - `apt-get install -y gcc g++`: Instala compiladores C/C++ (necessários para algumas bibliotecas Python)
  - `rm -rf /var/lib/apt/lists/*`: Remove cache para reduzir tamanho da imagem
- **Por quê**: Algumas bibliotecas Python (como NumPy, SciPy) precisam compilar código C

#### `WORKDIR /app`
- **Função**: Define o diretório de trabalho
- **O que faz**: Cria e muda para o diretório `/app` dentro do container
- **Por quê**: Organiza os arquivos da aplicação em um local específico

#### `COPY requirements.txt .`
- **Função**: Copia o arquivo de dependências
- **O que faz**: Copia `requirements.txt` do host para `/app` no container
- **Por quê**: Instalar dependências primeiro aproveita cache do Docker (otimização)

#### `RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt`
- **Função**: Instala dependências Python
- **O que faz**:
  - Atualiza o pip
  - Instala todos os pacotes listados em `requirements.txt`
  - `--no-cache-dir`: Não armazena cache (reduz tamanho da imagem)
- **Por quê**: Garante que todas as bibliotecas necessárias estejam disponíveis

#### `COPY . .`
- **Função**: Copia todos os arquivos do projeto
- **O que faz**: Copia todo o conteúdo do diretório atual para `/app` no container
- **Por quê**: Inclui código da aplicação, modelos treinados, etc.

#### `EXPOSE 8501`
- **Função**: Documenta a porta que a aplicação usa
- **O que faz**: Informa que o container escuta na porta 8501
- **Por quê**: Documentação e ajuda na configuração de rede

#### `CMD ["streamlit", "run", "appaivk.py", "--server.port=8501", "--server.address=0.0.0.0"]`
- **Função**: Define o comando padrão ao iniciar o container
- **O que faz**: Executa o Streamlit quando o container inicia
- **Parâmetros**:
  - `--server.port=8501`: Porta do servidor
  - `--server.address=0.0.0.0`: Aceita conexões de qualquer IP (não apenas localhost)

### 5.3 Estratégia de Build Otimizada

O Dockerfile usa uma estratégia inteligente:

1. **Instala dependências primeiro** (`COPY requirements.txt .`)
2. **Depois copia o código** (`COPY . .`)

**Por quê?**
- Dependências mudam menos frequentemente que o código
- Docker usa cache de camadas (layers)
- Se o código mudar mas dependências não, Docker reutiliza a camada de dependências
- Builds mais rápidos! ⚡

---

## 6. O que é Kubernetes?

### 6.1 Definição

**Kubernetes** (também conhecido como **K8s**) é uma plataforma open-source para orquestração de containers. Ele automatiza o deploy, escalonamento e gerenciamento de aplicações containerizadas.

### 6.2 Objetivos Principais

1. **Orquestração de Containers**
   - Gerencia múltiplos containers
   - Distribui carga entre instâncias
   - Garante alta disponibilidade

2. **Escalonamento Automático**
   - Aumenta ou diminui instâncias conforme demanda
   - Auto-scaling baseado em métricas

3. **Auto-recuperação**
   - Reinicia containers que falharam
   - Substitui containers não responsivos
   - Health checks automáticos

4. **Gerenciamento de Recursos**
   - Aloca CPU e memória
   - Balanceia recursos entre aplicações

5. **Rolling Updates**
   - Atualiza aplicações sem downtime
   - Rollback automático em caso de problemas

### 6.3 Conceitos Fundamentais

#### Pod
- Menor unidade de deploy no Kubernetes
- Pode conter um ou mais containers
- Containers no mesmo pod compartilham rede e armazenamento

#### Deployment
- Gerencia réplicas de pods
- Garante que o número desejado de pods esteja rodando
- Gerencia atualizações e rollbacks

#### Service
- Expõe pods para acesso externo ou interno
- Fornece IP estável e balanceamento de carga
- Tipos: ClusterIP, NodePort, LoadBalancer

#### Node
- Máquina (física ou virtual) que roda pods
- Pode ser um servidor ou VM

#### Cluster
- Conjunto de nodes trabalhando juntos
- Um cluster pode ter múltiplos nodes

---

## 7. O que é kubectl?

### 7.1 Definição

**kubectl** (pronuncia-se "kube-control" ou "kube-cuttle") é a ferramenta de linha de comando para interagir com clusters Kubernetes.

### 7.2 Instalação do kubectl

#### Windows

**Opção 1: Via Chocolatey (Recomendado)**
```powershell
# Instalar Chocolatey (se ainda não tiver)
# Abra PowerShell como Administrador e execute:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar kubectl
choco install kubernetes-cli
```

**Opção 2: Via curl**
```powershell
# Baixar kubectl
curl.exe -LO "https://dl.k8s.io/release/v1.28.0/bin/windows/amd64/kubectl.exe"

# Mover para pasta no PATH (exemplo: C:\Windows\System32)
# Ou adicionar ao PATH manualmente
```

**Opção 3: Via winget**
```powershell
winget install -e --id Kubernetes.kubectl
```

**Verificar instalação:**
```powershell
kubectl version --client
```

#### Linux

**Opção 1: Via curl**
```bash
# Baixar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Tornar executável
chmod +x kubectl

# Mover para PATH
sudo mv kubectl /usr/local/bin/
```

**Opção 2: Via apt (Ubuntu/Debian)**
```bash
# Adicionar repositório
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

# Baixar chave GPG
sudo curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Adicionar repositório
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Instalar
sudo apt-get update
sudo apt-get install -y kubectl
```

**Verificar instalação:**
```bash
kubectl version --client
```

#### macOS

**Opção 1: Via Homebrew (Recomendado)**
```bash
brew install kubectl
```

**Opção 2: Via curl**
```bash
# Baixar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"

# Tornar executável
chmod +x kubectl

# Mover para PATH
sudo mv kubectl /usr/local/bin/
```

**Verificar instalação:**
```bash
kubectl version --client
```

#### Links Úteis
- **Documentação oficial**: https://kubernetes.io/docs/tasks/tools/
- **Versões disponíveis**: https://github.com/kubernetes/kubernetes/releases

### 7.3 Função

**kubectl** é como o "controle remoto" do Kubernetes. Ele permite:
- Criar e gerenciar recursos (pods, deployments, services)
- Verificar status de aplicações
- Visualizar logs
- Executar comandos dentro de containers
- Aplicar configurações (manifestos YAML)

### 7.4 Comandos Comuns

| Comando | Função |
|---------|--------|
| `kubectl get pods` | Lista todos os pods |
| `kubectl apply -f arquivo.yaml` | Aplica configuração de um arquivo |
| `kubectl describe pod <nome>` | Mostra detalhes de um pod |
| `kubectl logs <pod>` | Mostra logs de um pod |
| `kubectl config current-context` | Mostra contexto atual |

### 7.5 Contexto (Context)

**Contexto** é a configuração que define:
- Qual cluster usar
- Qual namespace usar
- Credenciais de autenticação

**No projeto:**
- Contexto: `minikube` (cluster local)
- Verificar: `kubectl config current-context`

---

## 8. O que é Minikube?

### 8.1 Definição

**Minikube** é uma ferramenta que permite executar Kubernetes localmente em uma única máquina. É ideal para desenvolvimento e testes.

### 8.2 Instalação do Minikube

#### Pré-requisitos

Antes de instalar o Minikube, você precisa ter:
- ✅ **kubectl** instalado (veja seção 7.2)
- ✅ **Docker Desktop** instalado e rodando (para usar driver docker)
- ✅ **Hipervisor** (opcional, se não usar Docker): VirtualBox, Hyper-V, ou VMware

#### Windows

**Opção 1: Via Chocolatey (Recomendado)**
```powershell
# Instalar Chocolatey (se ainda não tiver)
# Abra PowerShell como Administrador e execute:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Instalar Minikube
choco install minikube
```

**Opção 2: Via winget**
```powershell
winget install -e --id Kubernetes.minikube
```

**Opção 3: Download Manual**
```powershell
# Baixar Minikube
# Acesse: https://github.com/kubernetes/minikube/releases
# Baixe: minikube-windows-amd64.exe
# Renomeie para: minikube.exe
# Mova para uma pasta no PATH (ex: C:\Windows\System32)
```

**Verificar instalação:**
```powershell
minikube version
```

#### Linux

**Opção 1: Via curl**
```bash
# Baixar Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

# Tornar executável
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Limpar arquivo temporário
rm minikube-linux-amd64
```

**Opção 2: Via apt (Ubuntu/Debian)**
```bash
# Baixar e instalar
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```

**Verificar instalação:**
```bash
minikube version
```

#### macOS

**Opção 1: Via Homebrew (Recomendado)**
```bash
brew install minikube
```

**Opção 2: Via curl**
```bash
# Baixar Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64

# Tornar executável
sudo install minikube-darwin-amd64 /usr/local/bin/minikube

# Limpar arquivo temporário
rm minikube-darwin-amd64
```

**Verificar instalação:**
```bash
minikube version
```

#### Primeira Configuração

Após instalar, configure o Minikube:

```bash
# Iniciar Minikube com driver Docker (recomendado)
minikube start --driver=docker

# Verificar status
minikube status

# Verificar contexto do kubectl
kubectl config current-context
# Deve retornar: minikube
```

**Nota:** Se o Docker não estiver disponível, você pode usar outros drivers:
- `minikube start --driver=virtualbox` (requer VirtualBox)
- `minikube start --driver=hyperv` (Windows com Hyper-V)
- `minikube start --driver=vmware` (requer VMware)

#### Links Úteis
- **Documentação oficial**: https://minikube.sigs.k8s.io/docs/start/
- **Releases**: https://github.com/kubernetes/minikube/releases
- **Guia de instalação**: https://minikube.sigs.k8s.io/docs/start/

### 8.3 Objetivos

1. **Ambiente Local de Kubernetes**
   - Permite testar Kubernetes sem um cluster real
   - Roda em uma VM ou container local

2. **Desenvolvimento e Aprendizado**
   - Ideal para aprender Kubernetes
   - Testa aplicações antes de deploy em produção

3. **CI/CD Local**
   - Testa pipelines localmente
   - Valida configurações antes de enviar

### 8.4 Como Funciona

```
Sua Máquina
├── Minikube (VM ou Container)
│   ├── Kubernetes Master
│   ├── Kubernetes Nodes
│   └── Sua Aplicação (Pods)
└── Docker Desktop
    └── Imagens Docker
```

### 8.5 Comandos Principais

| Comando | Função |
|---------|--------|
| `minikube start` | Inicia o cluster Kubernetes local |
| `minikube stop` | Para o cluster |
| `minikube image load <imagem>` | Carrega imagem Docker no cluster |
| `minikube service <nome>` | Abre serviço no navegador |
| `minikube status` | Mostra status do cluster |
| `minikube delete` | Remove o cluster completamente |

### 8.6 Por que Usar Minikube?

- ✅ **Gratuito**: Não precisa de cloud ou servidor
- ✅ **Rápido**: Setup em minutos
- ✅ **Isolado**: Não afeta outros projetos
- ✅ **Realista**: Simula ambiente de produção
- ✅ **Educacional**: Perfeito para aprender

---

## 9. Encadeamento Completo: Docker → Minikube → Kubernetes

### 9.1 Visão Geral do Fluxo

```
1. Desenvolvimento
   ↓
2. Build da Imagem Docker
   ↓
3. Iniciar Minikube
   ↓
4. Carregar Imagem no Minikube
   ↓
5. Deploy no Kubernetes
   ↓
6. Acesso à Aplicação
```

### 9.2 Passo a Passo Detalhado

#### Passo 1: Desenvolvimento e Treinamento do Modelo

```bash
# 1.1 Criar e ativar ambiente virtual
uv venv
.venv\Scripts\Activate  # Windows PowerShell

# 1.2 Instalar dependências
uv pip install -r requirements.txt

# 1.3 Treinar o modelo
python treinamento/aivk_treina_modelo.py
```

**Resultado:**
- Modelo treinado salvo em `modelos/modelo_qualidade_aivk.pkl`
- Código da aplicação pronto

#### Passo 2: Construir Imagem Docker

```bash
# 2.1 Verificar se Docker Desktop está rodando
# (Verificar ícone na bandeja do sistema)

# 2.2 Construir a imagem
docker build -t aivk-p6-app:latest .
```

**O que acontece:**
1. Docker lê o `Dockerfile`
2. Baixa imagem base `python:3.12-slim`
3. Instala dependências do sistema (gcc, g++)
4. Copia `requirements.txt` e instala dependências Python
5. Copia código da aplicação e modelo treinado
6. Cria imagem `aivk-p6-app:latest`

**Resultado:**
- Imagem Docker criada localmente
- Pronta para ser usada em containers

#### Passo 3: Iniciar Minikube

```bash
# 3.1 Iniciar cluster Kubernetes local
minikube start --driver=docker

# 3.2 Verificar contexto
kubectl config current-context
# Deve retornar: minikube
```

**O que acontece:**
1. Minikube cria uma VM ou container
2. Instala e configura Kubernetes completo
3. Configura kubectl para apontar para o cluster local

**Resultado:**
- Cluster Kubernetes rodando localmente
- kubectl configurado para usar Minikube

#### Passo 4: Carregar Imagem no Minikube

```bash
# 4.1 Carregar imagem Docker no cluster Minikube
minikube image load aivk-p6-app:latest
```

**Por que é necessário?**
- Minikube roda em uma VM/container isolada
- Kubernetes dentro do Minikube não vê imagens do Docker host
- Precisa "transferir" a imagem para dentro do cluster

**O que acontece:**
1. Minikube localiza a imagem `aivk-p6-app:latest` no Docker local
2. Transfere a imagem para dentro da VM do Minikube
3. Imagem fica disponível para o Kubernetes criar pods

**Resultado:**
- Imagem disponível no cluster Kubernetes
- Pronta para ser usada em deployments

#### Passo 5: Deploy no Kubernetes

```bash
# 5.1 Aplicar Deployment
kubectl apply -f k8s/deployment.yaml

# 5.2 Aplicar Service
kubectl apply -f k8s/service.yaml

# 5.3 Verificar status
kubectl get pods
```

**O que acontece:**

**5.1 Deployment:**
- Kubernetes lê `k8s/deployment.yaml`
- Cria pods usando a imagem `aivk-p6-app:latest`
- Garante que 1 réplica esteja rodando
- Configura porta 8501

**5.2 Service:**
- Kubernetes lê `k8s/service.yaml`
- Cria serviço NodePort
- Expõe aplicação na porta 30002
- Conecta tráfego aos pods

**5.3 Verificação:**
- Lista pods em execução
- Mostra status (Running, Pending, Error)

**Resultado:**
- Aplicação rodando no Kubernetes
- Acessível via Service

#### Passo 6: Acessar a Aplicação

```bash
# 6.1 Abrir aplicação no navegador
minikube service aivk-p6-app-service
```

**O que acontece:**
1. Minikube encontra o serviço `aivk-p6-app-service`
2. Obtém URL de acesso (ex: `http://192.168.49.2:30002`)
3. Abre navegador automaticamente
4. Aplicação Streamlit é exibida

**Resultado:**
- Aplicação acessível no navegador
- Pipeline completo funcionando!

### 9.3 Diagrama Completo do Fluxo

```
┌─────────────────────────────────────────────────────────────┐
│                    DESENVOLVIMENTO                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Código Python│  │ Treinar Modelo│  │ requirements  │    │
│  │  appaivk.py  │→ │   ML (.pkl)   │  │    .txt       │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    DOCKER BUILD                              │
│  ┌──────────────┐                                           │
│  │  Dockerfile  │ → docker build -t aivk-p6-app:latest .    │
│  └──────────────┘                                           │
│                            ↓                                │
│  ┌──────────────────────────────────────┐                  │
│  │  Imagem Docker: aivk-p6-app:latest   │                  │
│  │  - Python 3.12                       │                  │
│  │  - Dependências instaladas           │                  │
│  │  - Código da aplicação               │                  │
│  │  - Modelo treinado                   │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    MINIKUBE                                 │
│  minikube start --driver=docker                             │
│                            ↓                                │
│  ┌──────────────────────────────────────┐                  │
│  │  Cluster Kubernetes Local            │                  │
│  │  - Master Node                       │                  │
│  │  - Worker Nodes                      │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    CARREGAR IMAGEM                           │
│  minikube image load aivk-p6-app:latest                     │
│                            ↓                                │
│  Imagem disponível dentro do cluster Minikube               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    KUBERNETES DEPLOY                         │
│  ┌──────────────────┐  ┌──────────────────┐               │
│  │ deployment.yaml  │  │  service.yaml     │               │
│  └──────────────────┘  └──────────────────┘               │
│           ↓                          ↓                       │
│  ┌──────────────────────────────────────┐                  │
│  │  Pods rodando a aplicação            │                  │
│  │  Service expondo na porta 30002      │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    ACESSO                                    │
│  minikube service aivk-p6-app-service                        │
│                            ↓                                │
│  ┌──────────────────────────────────────┐                  │
│  │  Navegador: http://192.168.49.2:30002│                  │
│  │  Aplicação Streamlit rodando!        │                  │
│  └──────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. Comandos do Projeto

### 10.1 Comandos Docker

#### Construir Imagem
```bash
docker build -t aivk-p6-app:latest .
```

**Parâmetros:**
- `-t aivk-p6-app:latest`: Nome e tag da imagem
- `.`: Contexto de build (diretório atual)

#### Listar Imagens
```bash
docker images
```

#### Remover Imagem
```bash
docker rmi aivk-p6-app:latest
```

#### Executar Container Localmente (teste)
```bash
docker run -p 8501:8501 aivk-p6-app:latest
```

### 10.2 Comandos Minikube

#### Iniciar Cluster
```bash
minikube start --driver=docker
```

**Parâmetros:**
- `--driver=docker`: Usa Docker como driver (mais leve)

#### Parar Cluster
```bash
minikube stop
```

#### Carregar Imagem
```bash
minikube image load aivk-p6-app:latest
```

#### Abrir Serviço no Navegador
```bash
minikube service aivk-p6-app-service
```

#### Obter URL do Serviço (sem abrir navegador)
```bash
minikube service aivk-p6-app-service --url
```

### 10.3 Comandos kubectl

#### Verificar Contexto
```bash
kubectl config current-context
```

#### Aplicar Manifestos
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

#### Listar Recursos
```bash
kubectl get pods                    # Lista pods
kubectl get deployments             # Lista deployments
kubectl get services                # Lista services
kubectl get all                     # Lista todos os recursos
```

#### Ver Detalhes
```bash
kubectl describe pod <nome-do-pod>
kubectl describe deployment aivk-p6-app-deployment
kubectl describe service aivk-p6-app-service
```

#### Ver Logs
```bash
kubectl logs <nome-do-pod>
kubectl logs -f <nome-do-pod>      # Segue logs em tempo real
```

#### Atualizar Deployment
```bash
kubectl set image deployment/aivk-p6-app-deployment \
  aivk-p6-app-container=aivk-p6-app:latest
```

#### Remover Recursos
```bash
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
```

### 10.4 Sequência Completa de Comandos

```bash
# 1. Build da imagem
docker build -t aivk-p6-app:latest .

# 2. Iniciar Minikube
minikube start --driver=docker

# 3. Verificar contexto
kubectl config current-context

# 4. Carregar imagem
minikube image load aivk-p6-app:latest

# 5. Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# 6. Verificar status
kubectl get pods

# 7. Acessar aplicação
minikube service aivk-p6-app-service
```

---

## 11. Troubleshooting

### 11.1 Problemas com Docker

#### Erro: "Cannot connect to the Docker daemon"
**Causa:** Docker Desktop não está rodando

**Solução:**
1. Abrir Docker Desktop
2. Aguardar inicialização completa
3. Verificar ícone na bandeja do sistema

#### Erro: "No space left on device"
**Causa:** Disco cheio ou muitas imagens

**Solução:**
```bash
# Limpar imagens não utilizadas
docker system prune -a

# Ver uso de espaço
docker system df
```

#### Erro: "Failed to build"
**Causa:** Erro no Dockerfile ou dependências

**Solução:**
1. Verificar logs do build
2. Verificar se Dockerfile está correto
3. Verificar se requirements.txt está atualizado

### 11.2 Problemas com Minikube

#### Erro: "minikube start" falha
**Causa:** Docker não está rodando ou recursos insuficientes

**Solução:**
```bash
# Verificar status do Docker
docker ps

# Limpar Minikube e recriar
minikube delete
minikube start --driver=docker
```

#### Erro: "Image not found" no Kubernetes
**Causa:** Imagem não foi carregada no Minikube

**Solução:**
```bash
# Carregar imagem
minikube image load aivk-p6-app:latest

# Verificar se foi carregada
minikube image ls
```

### 11.3 Problemas com Kubernetes

#### Pod em CrashLoopBackOff
**Causa:** Container está falhando ao iniciar

**Solução:**
```bash
# Ver logs do pod
kubectl logs <nome-do-pod>

# Ver detalhes
kubectl describe pod <nome-do-pod>

# Verificar se imagem está correta
kubectl describe pod <nome-do-pod> | grep Image
```

#### Service não acessível
**Causa:** Porta incorreta ou service não configurado

**Solução:**
```bash
# Verificar service
kubectl get services

# Ver detalhes
kubectl describe service aivk-p6-app-service

# Verificar se pods estão rodando
kubectl get pods
```

#### Contexto incorreto
**Causa:** kubectl apontando para cluster errado

**Solução:**
```bash
# Ver contexto atual
kubectl config current-context

# Listar contextos disponíveis
kubectl config get-contexts

# Mudar contexto
kubectl config use-context minikube
```

### 11.4 Comandos de Diagnóstico

```bash
# Status geral
kubectl get all

# Logs em tempo real
kubectl logs -f <pod> --tail=50

# Executar comando dentro do pod
kubectl exec -it <pod> -- /bin/bash

# Ver eventos
kubectl get events --sort-by='.lastTimestamp'
```

---

## 12. Resumo e Próximos Passos

### 12.1 Resumo dos Conceitos

1. **Docker**: Empacota aplicação em containers portáteis
2. **Dockerfile**: Receita para construir imagens
3. **Imagem**: Template read-only usado para criar containers
4. **Container**: Instância em execução de uma imagem
5. **Kubernetes**: Orquestra múltiplos containers
6. **kubectl**: Ferramenta CLI para gerenciar Kubernetes
7. **Minikube**: Kubernetes local para desenvolvimento

### 12.2 Fluxo do Projeto

```
Desenvolvimento → Docker Build → Minikube → Kubernetes Deploy → Acesso
```

### 12.3 Próximos Passos

- ✅ Entender conceitos de Pods, Deployments e Services
- ✅ Aprender sobre ConfigMaps e Secrets
- ✅ Explorar auto-scaling
- ✅ Estudar Ingress para roteamento
- ✅ Aprender sobre Helm para gerenciamento de pacotes

---

**Última atualização:** Janeiro 2025  
**Versão:** 1.0  
**Projeto:** Projeto 6 - AIVK

