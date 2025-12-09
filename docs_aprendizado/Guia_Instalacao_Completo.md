# Guia de Instalação Completo - Projeto AIVK

Este documento fornece instruções detalhadas passo a passo para instalação e configuração de todas as ferramentas necessárias para executar o projeto AIVK.

## 📋 Índice

1. [Instalação do Git](#1-instalação-do-git)
2. [Instalação do Python 3.12](#2-instalação-do-python-312)
3. [Instalação do uv](#3-instalação-do-uv)
4. [Instalação do Docker Desktop](#4-instalação-do-docker-desktop)
5. [Instalação do kubectl](#5-instalação-do-kubectl)
6. [Instalação do Minikube](#6-instalação-do-minikube)
7. [Instalação do Act (Opcional)](#7-instalação-do-act-opcional)
8. [Validação da Instalação](#8-validação-da-instalação)

---

## 1. Instalação do Git

### Windows

**Opção 1: Download Oficial (Recomendado)**
1. Acesse: https://git-scm.com/download/win
2. Baixe o instalador
3. Execute e siga o assistente de instalação
4. Durante a instalação, escolha:
   - Editor padrão (recomendado: VS Code ou Notepad++)
   - Terminal (Git Bash, PowerShell ou CMD)
   - Line endings: "Checkout Windows-style, commit Unix-style line endings"

**Opção 2: Via Chocolatey**
```powershell
choco install git
```

**Opção 3: Via winget**
```powershell
winget install --id Git.Git -e --source winget
```

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install git
```

### macOS

```bash
brew install git
```

**Verificar instalação:**
```bash
git --version
```

---

## 2. Instalação do Python 3.12

### Windows

**Opção 1: Download Oficial**
1. Acesse: https://www.python.org/downloads/
2. Baixe Python 3.12.x
3. Execute o instalador
4. **IMPORTANTE**: Marque "Add Python to PATH"
5. Escolha "Install Now"

**Opção 2: Via Microsoft Store**
1. Abra Microsoft Store
2. Procure por "Python 3.12"
3. Clique em "Instalar"

### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3.12 python3.12-venv python3.12-pip
```

### macOS

```bash
brew install python@3.12
```

**Verificar instalação:**
```bash
python --version  # Deve retornar Python 3.12.x
# ou
python3 --version
```

---

## 3. Instalação do uv

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Após instalar, feche e reabra o terminal.

### Linux/Mac

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Alternativa: Via pip

```bash
pip install uv
```

**Verificar instalação:**
```bash
uv --version
```

---

## 4. Instalação do Docker Desktop

### Windows

1. Acesse: https://www.docker.com/products/docker-desktop/
2. Baixe "Docker Desktop for Windows"
3. Execute o instalador
4. Siga o assistente de instalação
5. Reinicie o computador se solicitado
6. Abra o Docker Desktop e aguarde a inicialização

**Requisitos:**
- Windows 10 64-bit: Pro, Enterprise ou Education (Build 19041 ou superior)
- Windows 11 64-bit
- WSL 2 habilitado (o instalador pode fazer isso automaticamente)

### Linux (Ubuntu/Debian)

```bash
# Remover versões antigas
sudo apt-get remove docker docker-engine docker.io containerd runc

# Instalar dependências
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# Adicionar chave GPG oficial
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Configurar repositório
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER
```

**Reiniciar sessão ou executar:**
```bash
newgrp docker
```

### macOS

1. Acesse: https://www.docker.com/products/docker-desktop/
2. Baixe "Docker Desktop for Mac"
3. Abra o arquivo .dmg
4. Arraste Docker para a pasta Applications
5. Abra Docker Desktop

**Verificar instalação:**
```bash
docker --version
docker ps  # Deve funcionar sem erros
```

---

## 5. Instalação do kubectl

### Windows

**Opção 1: Via Chocolatey**
```powershell
choco install kubernetes-cli
```

**Opção 2: Via winget**
```powershell
winget install -e --id Kubernetes.kubectl
```

**Opção 3: Download Manual**
1. Acesse: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
2. Baixe kubectl.exe
3. Adicione ao PATH ou coloque em uma pasta no PATH

### Linux

```bash
# Baixar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Tornar executável
chmod +x kubectl

# Mover para PATH
sudo mv kubectl /usr/local/bin/
```

### macOS

```bash
brew install kubectl
```

**Verificar instalação:**
```bash
kubectl version --client
```

---

## 6. Instalação do Minikube

### Windows

**Opção 1: Via Chocolatey**
```powershell
choco install minikube
```

**Opção 2: Via winget**
```powershell
winget install -e --id Kubernetes.minikube
```

**Opção 3: Download Manual**
1. Acesse: https://minikube.sigs.k8s.io/docs/start/
2. Baixe minikube-installer.exe
3. Execute o instalador

### Linux

```bash
# Baixar Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

# Tornar executável
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Limpar arquivo temporário
rm minikube-linux-amd64
```

### macOS

```bash
brew install minikube
```

**Verificar instalação:**
```bash
minikube version
```

---

## 7. Instalação do Act (Opcional)

O Act é usado para testar GitHub Actions localmente. É opcional, mas recomendado.

### Windows

**Via Chocolatey:**
```powershell
choco install act-cli
```

### Linux

```bash
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

### macOS

```bash
brew install act
```

**Verificar instalação:**
```bash
act --version
```

---

## 8. Validação da Instalação

Execute os seguintes comandos para verificar se tudo está instalado corretamente:

```bash
# Git
git --version

# Python
python --version  # Deve retornar Python 3.12.x

# uv
uv --version

# Docker
docker --version
docker ps  # Deve funcionar sem erros

# kubectl
kubectl version --client

# Minikube
minikube version

# Act (opcional)
act --version
```

### Teste Completo do Ambiente

1. **Iniciar Minikube:**
```bash
minikube start --driver=docker
```

2. **Verificar contexto:**
```bash
kubectl config current-context  # Deve retornar: minikube
```

3. **Verificar Docker:**
```bash
docker ps  # Deve listar containers (pode estar vazio)
```

Se todos os comandos funcionarem sem erros, seu ambiente está configurado corretamente! ✅

---

## 🔗 Links Úteis

* **Git**: https://git-scm.com/
* **Python**: https://www.python.org/
* **uv**: https://github.com/astral-sh/uv
* **Docker**: https://www.docker.com/
* **Kubernetes**: https://kubernetes.io/
* **Minikube**: https://minikube.sigs.k8s.io/
* **Act**: https://nektosact.com/

---

## ⚠️ Problemas Comuns

### Docker não inicia no Windows

**Solução:**
1. Verifique se o WSL 2 está habilitado
2. Verifique se a virtualização está habilitada no BIOS
3. Reinicie o computador
4. Execute Docker Desktop como Administrador

### Minikube não inicia

**Solução:**
1. Verifique se Docker está rodando: `docker ps`
2. Tente com driver diferente: `minikube start --driver=virtualbox`
3. Limpe e recrie: `minikube delete && minikube start --driver=docker`

### Python não encontrado

**Solução:**
1. Verifique se Python está no PATH
2. No Windows, reinstale marcando "Add Python to PATH"
3. Reinicie o terminal após instalar

---

**Última atualização:** Janeiro 2025  
**Versão:** 1.0  
**Projeto:** Projeto 6 - AIVK

