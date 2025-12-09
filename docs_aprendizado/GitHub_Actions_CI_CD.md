# GitHub Actions CI/CD - Guia Completo

## 📚 Índice
1. [O que é CI/CD?](#1-o-que-é-cicd)
2. [O que é GitHub Actions?](#2-o-que-é-github-actions)
3. [Workflow do Projeto AIVK](#3-workflow-do-projeto-aivk)
4. [Análise Detalhada do Workflow](#4-análise-detalhada-do-workflow)
5. [Triggers e Quando o Workflow é Executado](#5-triggers-e-quando-o-workflow-é-executado)
6. [Etapas do Pipeline](#6-etapas-do-pipeline)
7. [Relação com o Projeto](#7-relação-com-o-projeto)
8. [Testando Localmente com Act](#8-testando-localmente-com-act)
9. [Troubleshooting](#9-troubleshooting)
10. [Boas Práticas](#10-boas-práticas)

---

## 1. O que é CI/CD?

### 1.1 Definição

**CI/CD** significa **Continuous Integration** (Integração Contínua) e **Continuous Deployment/Delivery** (Deploy/Distribuição Contínua).

### 1.2 Integração Contínua (CI)

**CI** é a prática de integrar código frequentemente em um repositório compartilhado, onde cada integração é verificada automaticamente por builds e testes automatizados.

**Benefícios:**
- ✅ Detecta erros rapidamente
- ✅ Reduz conflitos de merge
- ✅ Garante qualidade do código
- ✅ Feedback imediato para desenvolvedores

### 1.3 Deploy/Distribuição Contínua (CD)

**CD** é a prática de automatizar o processo de deploy, permitindo que mudanças no código sejam automaticamente testadas, construídas e implantadas em ambientes de produção ou staging.

**Benefícios:**
- ✅ Deploy mais rápido e confiável
- ✅ Reduz erros manuais
- ✅ Permite releases frequentes
- ✅ Facilita rollback

### 1.4 Pipeline CI/CD

Um **pipeline CI/CD** é uma série de etapas automatizadas que:
1. Detecta mudanças no código
2. Executa testes
3. Constrói a aplicação
4. Valida a qualidade
5. Faz deploy (opcional)

---

## 2. O que é GitHub Actions?

### 2.1 Definição

**GitHub Actions** é uma plataforma de automação integrada ao GitHub que permite criar workflows de CI/CD diretamente no repositório.

### 2.2 Características Principais

- ✅ **Integrado ao GitHub**: Não precisa de ferramentas externas
- ✅ **Gratuito para projetos públicos**: Até 2000 minutos/mês
- ✅ **Baseado em YAML**: Configuração simples e versionada
- ✅ **Marketplace de Actions**: Reutiliza ações da comunidade
- ✅ **Multiplataforma**: Linux, Windows, macOS

### 2.3 Conceitos Fundamentais

#### Workflow
Arquivo YAML que define um processo automatizado. Fica em `.github/workflows/`.

#### Job
Conjunto de etapas (steps) que rodam no mesmo runner. Jobs podem rodar em paralelo ou sequencialmente.

#### Step
Tarefa individual dentro de um job. Pode ser um comando shell ou uma action.

#### Action
Unidade reutilizável de código que executa uma tarefa específica. Pode ser criada por você ou obtida do marketplace.

#### Runner
Máquina virtual que executa os workflows. GitHub fornece runners (Ubuntu, Windows, macOS) ou você pode usar seus próprios.

### 2.4 Estrutura de um Workflow

```yaml
name: Nome do Workflow

on:  # Quando executar
  push:
    branches: [main]

jobs:  # O que executar
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Passo 1
        run: comando
```

---

## 3. Workflow do Projeto AIVK

### 3.1 Visão Geral

O projeto AIVK possui um workflow de CI/CD configurado em `.github/workflows/ci-cd.yml` que automatiza:

1. ✅ Treinamento do modelo de Machine Learning
2. ✅ Construção da imagem Docker
3. ✅ Validação dos manifestos Kubernetes

### 3.2 Nome do Workflow

```yaml
name: AIVKProjeto6
```

**Função:** Identifica o workflow no GitHub Actions. Aparece na interface do GitHub.

### 3.3 Objetivo do Workflow

Este workflow garante que:
- Modelo de ML seja retreinado quando necessário
- Imagem Docker seja construída com o modelo atualizado
- Configurações Kubernetes estejam corretas
- Qualidade seja mantida antes de fazer deploy

---

## 4. Análise Detalhada do Workflow

### 4.1 Arquivo Completo

```yaml
# Workflow de CI/CD para o Projeto AIVK
# Este pipeline automatiza o processo de treinamento de modelo, construção de imagem Docker
# e validação de manifestos Kubernetes quando há mudanças nos arquivos importantes.
# Ele é acionado automaticamente em dois cenários:
  # Quando há um push na branch main
  # Quando há modificações nos seguintes arquivos ou diretórios:
    # modelos/**
    # treinamento/**
    # appaivk.py
    # requirements.txt
    # Dockerfile

name: AIVKProjeto6

# Configuração de triggers - define quando o workflow deve ser executado
on:
  push:
    branches:
      - main  # Executa apenas na branch main
    paths:
      # Executa apenas se houver mudanças nestes arquivos/pastas específicos
      - 'modelos/**'      # Mudanças nos modelos de ML
      - 'treinamento/**'  # Mudanças nos scripts de treinamento
      - 'appaivk.py'      # Mudanças na aplicação principal
      - 'requirements.txt' # Mudanças nas dependências
      - 'Dockerfile'      # Mudanças na configuração do container

jobs:
  build-test:
    # Ambiente de execução: Ubuntu com container específico para GitHub Actions
    runs-on: ubuntu-latest
    container:
      image: catthehacker/ubuntu:act-latest
    
    steps:
      # Etapa 1: Baixar o código do repositório para o ambiente de execução
      - name: Checkout do código
        uses: actions/checkout@v4

      # Etapa 2: Instalar Node.js (necessário para algumas ferramentas do projeto)
      - name: Instalar Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      # Etapa 3: Configurar Python 3.12 (versão específica do projeto)
      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      # Etapa 4: Instalar todas as dependências Python do projeto
      - name: Instalar dependências Python
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      # Etapa 5: Treinar novo modelo de ML com dados atualizados
      - name: Treinar modelo
        run: python treinamento/aivk_treina_modelo.py

      # Etapa 6: Construir imagem Docker com o modelo recém-treinado
      - name: Construir imagem Docker com novo modelo
        run: docker build -t aivk-p6-app:latest .

      # Etapa 7: Validar sintaxe e configuração dos manifestos Kubernetes
      - name: Validar manifestos Kubernetes
        uses: stefanprodan/kube-tools@v1
        with:
          command: |
            kubeconform -summary -strict k8s/
```

---

## 5. Triggers e Quando o Workflow é Executado

### 5.1 Configuração de Triggers

```yaml
on:
  push:
    branches:
      - main
    paths:
      - 'modelos/**'
      - 'treinamento/**'
      - 'appaivk.py'
      - 'requirements.txt'
      - 'Dockerfile'
```

### 5.2 Quando o Workflow é Executado?

O workflow é acionado quando **AMBAS** as condições são verdadeiras:

1. ✅ **Push na branch `main`**
   - Apenas commits na branch principal disparam o workflow
   - Commits em outras branches não disparam

2. ✅ **E** há mudanças em arquivos específicos:
   - `modelos/**` - Qualquer arquivo na pasta modelos
   - `treinamento/**` - Qualquer arquivo na pasta treinamento
   - `appaivk.py` - Arquivo principal da aplicação
   - `requirements.txt` - Dependências Python
   - `Dockerfile` - Configuração do container

### 5.3 Exemplos Práticos

#### ✅ Workflow SERÁ executado:
```bash
# Cenário 1: Push na main com mudança no appaivk.py
git add appaivk.py
git commit -m "Atualiza interface"
git push origin main
# ✅ Workflow executa

# Cenário 2: Push na main com mudança no requirements.txt
git add requirements.txt
git commit -m "Adiciona nova dependência"
git push origin main
# ✅ Workflow executa

# Cenário 3: Push na main com mudança no Dockerfile
git add Dockerfile
git commit -m "Otimiza Dockerfile"
git push origin main
# ✅ Workflow executa
```

#### ❌ Workflow NÃO será executado:
```bash
# Cenário 1: Push em outra branch
git checkout -b feature/nova-funcionalidade
git add appaivk.py
git commit -m "Nova funcionalidade"
git push origin feature/nova-funcionalidade
# ❌ Workflow NÃO executa (não é branch main)

# Cenário 2: Push na main mas sem mudanças nos arquivos monitorados
git add README.md
git commit -m "Atualiza documentação"
git push origin main
# ❌ Workflow NÃO executa (README.md não está na lista)

# Cenário 3: Mudança apenas em arquivos não monitorados
git add docs/novo-doc.md
git commit -m "Adiciona documentação"
git push origin main
# ❌ Workflow NÃO executa
```

### 5.4 Por que Filtrar por Arquivos?

**Vantagens:**
- ⚡ **Economiza recursos**: Não executa quando não é necessário
- ⚡ **Mais rápido**: Workflows desnecessários não rodam
- ⚡ **Foco**: Executa apenas quando arquivos relevantes mudam

**Arquivos monitorados e por quê:**
- `modelos/**` - Modelo pode ter sido atualizado manualmente
- `treinamento/**` - Script de treinamento mudou
- `appaivk.py` - Aplicação principal mudou
- `requirements.txt` - Dependências mudaram
- `Dockerfile` - Configuração do container mudou

---

## 6. Etapas do Pipeline

### 6.1 Estrutura do Job

```yaml
jobs:
  build-test:
    runs-on: ubuntu-latest
    container:
      image: catthehacker/ubuntu:act-latest
```

**Explicação:**
- `build-test`: Nome do job
- `runs-on: ubuntu-latest`: Executa em runner Ubuntu mais recente
- `container`: Usa container específico (compatível com Act para testes locais)

### 6.2 Etapa 1: Checkout do Código

```yaml
- name: Checkout do código
  uses: actions/checkout@v4
```

**O que faz:**
- Baixa o código do repositório para o runner
- Disponibiliza arquivos para as próximas etapas
- Versão v4 é a mais recente e estável

**Por que é necessário:**
- Runner começa vazio
- Precisa do código para executar os próximos passos

### 6.3 Etapa 2: Instalar Node.js

```yaml
- name: Instalar Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '20'
```

**O que faz:**
- Instala Node.js versão 20 no runner
- Configura ambiente Node.js

**Por que é necessário:**
- Algumas ferramentas do projeto podem precisar de Node.js
- Ferramentas de validação Kubernetes podem usar Node.js

### 6.4 Etapa 3: Configurar Python

```yaml
- name: Configurar Python
  uses: actions/setup-python@v5
  with:
    python-version: 3.12
```

**O que faz:**
- Instala Python 3.12 no runner
- Configura ambiente Python
- Versão específica garante consistência

**Por que é necessário:**
- Projeto usa Python 3.12
- Precisa do Python para executar scripts e instalar dependências

### 6.5 Etapa 4: Instalar Dependências Python

```yaml
- name: Instalar dependências Python
  run: |
    pip install --upgrade pip
    pip install -r requirements.txt
```

**O que faz:**
1. Atualiza o pip para versão mais recente
2. Instala todas as dependências listadas em `requirements.txt`

**Por que é necessário:**
- Scripts Python precisam das bibliotecas instaladas
- Treinamento do modelo requer scikit-learn, pandas, etc.
- Aplicação Streamlit precisa do streamlit

**Dependências principais:**
- `streamlit` - Framework web
- `scikit-learn` - Machine Learning
- `pandas` - Manipulação de dados
- `numpy` - Computação numérica
- `joblib` - Serialização do modelo

### 6.6 Etapa 5: Treinar Modelo

```yaml
- name: Treinar modelo
  run: python treinamento/aivk_treina_modelo.py
```

**O que faz:**
- Executa o script de treinamento
- Gera dataset sintético (1.250 amostras)
- Treina modelo RandomForestClassifier
- Salva modelo em `modelos/modelo_qualidade_aivk.pkl`
- Faz backup de versões anteriores com timestamp

**Por que é necessário:**
- Garante que o modelo está sempre atualizado
- Se script de treinamento mudou, modelo é retreinado
- Versionamento automático de modelos

**O que acontece:**
1. Gera dados sintéticos
2. Divide em treino e teste
3. Treina RandomForestClassifier
4. Avalia acurácia
5. Salva modelo com versionamento

### 6.7 Etapa 6: Construir Imagem Docker

```yaml
- name: Construir imagem Docker com novo modelo
  run: docker build -t aivk-p6-app:latest .
```

**O que faz:**
- Constrói imagem Docker usando o Dockerfile
- Nomeia a imagem como `aivk-p6-app:latest`
- Inclui modelo recém-treinado na imagem

**Por que é necessário:**
- Imagem Docker contém aplicação completa
- Modelo treinado é incluído na imagem
- Pronta para deploy em Kubernetes

**O que acontece:**
1. Docker lê o Dockerfile
2. Baixa imagem base Python 3.12-slim
3. Instala dependências do sistema
4. Instala dependências Python
5. Copia código e modelo treinado
6. Cria imagem final

### 6.8 Etapa 7: Validar Manifestos Kubernetes

```yaml
- name: Validar manifestos Kubernetes
  uses: stefanprodan/kube-tools@v1
  with:
    command: |
      kubeconform -summary -strict k8s/
```

**O que faz:**
- Valida sintaxe dos arquivos YAML do Kubernetes
- Verifica se estão corretos antes do deploy
- Usa `kubeconform` para validação

**Por que é necessário:**
- Evita erros no deploy
- Detecta problemas antes de chegar em produção
- Garante que manifestos estão corretos

**O que valida:**
- `k8s/deployment.yaml` - Configuração do Deployment
- `k8s/service.yaml` - Configuração do Service
- Sintaxe YAML correta
- Campos obrigatórios presentes
- Valores válidos

---

## 7. Relação com o Projeto

### 7.1 Fluxo Completo do Projeto

```
┌─────────────────────────────────────────────────────────────┐
│              DESENVOLVIMENTO LOCAL                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Desenvolver  │  │ Treinar      │  │ Testar       │    │
│  │ Código       │→ │ Modelo       │→ │ Localmente   │    │
│  └──────────────┘  └──────────────┘  └──────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              GIT PUSH PARA MAIN                             │
│  git add .                                                  │
│  git commit -m "Atualização"                               │
│  git push origin main                                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              GITHUB ACTIONS (CI/CD)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. Checkout código                                   │  │
│  │ 2. Instalar Node.js e Python                        │  │
│  │ 3. Instalar dependências                            │  │
│  │ 4. Treinar modelo ML                                │  │
│  │ 5. Construir imagem Docker                          │  │
│  │ 6. Validar Kubernetes                                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              RESULTADO                                     │
│  ✅ Modelo treinado e atualizado                          │
│  ✅ Imagem Docker construída                              │
│  ✅ Manifestos Kubernetes validados                       │
│  ✅ Pronto para deploy                                    │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Integração com Outros Componentes

#### Com Docker
- Workflow constrói imagem Docker automaticamente
- Imagem contém modelo mais recente
- Pronta para uso em containers

#### Com Kubernetes
- Valida manifestos antes do deploy
- Garante que configurações estão corretas
- Facilita deploy manual ou automatizado

#### Com Modelo de ML
- Retreina modelo quando necessário
- Versionamento automático
- Garante que modelo está atualizado

### 7.3 Benefícios para o Projeto

1. **Automação**
   - Não precisa executar comandos manualmente
   - Processo repetível e confiável

2. **Qualidade**
   - Validações automáticas
   - Detecta erros antes do deploy

3. **Consistência**
   - Mesmo processo sempre
   - Ambiente isolado e limpo

4. **Rastreabilidade**
   - Histórico de execuções no GitHub
   - Logs de cada execução

5. **Colaboração**
   - Time vê status dos builds
   - Feedback imediato

---

## 8. Testando Localmente com Act

### 8.1 O que é Act?

**Act** é uma ferramenta que permite executar GitHub Actions localmente, simulando o ambiente do GitHub sem fazer push.

### 8.2 Por que Usar Act?

- ✅ Testa workflows antes de commitar
- ✅ Debug local de problemas
- ✅ Economiza tempo (não precisa fazer push)
- ✅ Valida configurações localmente

### 8.3 Instalação do Act

#### Windows (Chocolatey)
```powershell
choco install act-cli
```

#### Linux/Mac
```bash
# Via curl
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Via Homebrew (Mac)
brew install act
```

### 8.4 Executando o Workflow Localmente

```bash
# No diretório do projeto
act push
```

**O que acontece:**
1. Act lê o workflow `.github/workflows/ci-cd.yml`
2. Simula evento "push"
3. Executa todas as etapas localmente
4. Mostra logs de cada etapa

### 8.5 Primeira Execução

Na primeira vez, Act pedirá para escolher o tamanho da imagem Docker:

```
? Please choose the default image you want to use with act:

  [Use arrows to move, type to filter]
  > Medium
    Large
    Micro
```

**Para este projeto, escolha: Medium**

### 8.6 Comandos Úteis do Act

```bash
# Executar workflow
act push

# Listar workflows disponíveis
act -l

# Executar workflow específico
act -W .github/workflows/ci-cd.yml push

# Executar apenas um job específico
act push -j build-test

# Ver dry-run (sem executar)
act push --dry-run

# Apple Silicon (forçar arquitetura)
act push --container-architecture linux/amd64
```

### 8.7 Limitações do Act

- ⚠️ Não executa em ambiente idêntico ao GitHub
- ⚠️ Algumas actions podem não funcionar
- ⚠️ Secrets do GitHub não estão disponíveis
- ⚠️ Pode ser mais lento que GitHub Actions

**Mas é excelente para:**
- ✅ Validar sintaxe do workflow
- ✅ Testar lógica básica
- ✅ Debug local

---

## 9. Troubleshooting

### 9.1 Workflow Não Executa

**Problema:** Workflow não é acionado após push

**Soluções:**
1. Verificar se está na branch `main`
   ```bash
   git branch
   ```

2. Verificar se arquivos modificados estão na lista de paths
   - Workflow só executa se mudanças estão em: `modelos/**`, `treinamento/**`, `appaivk.py`, `requirements.txt`, `Dockerfile`

3. Verificar se workflow está no caminho correto
   - Deve estar em: `.github/workflows/ci-cd.yml`

4. Verificar sintaxe YAML
   - Usar validador YAML online
   - Verificar indentação (espaços, não tabs)

### 9.2 Erro na Instalação de Dependências

**Problema:** `pip install -r requirements.txt` falha

**Soluções:**
1. Verificar se `requirements.txt` existe
2. Verificar sintaxe do arquivo
3. Verificar se versões são compatíveis
4. Ver logs completos no GitHub Actions

### 9.3 Erro no Treinamento do Modelo

**Problema:** Script de treinamento falha

**Soluções:**
1. Testar script localmente primeiro
   ```bash
   python treinamento/aivk_treina_modelo.py
   ```

2. Verificar se todas as dependências estão instaladas
3. Verificar logs de erro no GitHub Actions
4. Verificar se há espaço em disco suficiente

### 9.4 Erro no Build Docker

**Problema:** `docker build` falha

**Soluções:**
1. Verificar se Dockerfile está correto
2. Verificar se todos os arquivos necessários estão presentes
3. Testar build localmente:
   ```bash
   docker build -t aivk-p6-app:latest .
   ```

4. Verificar logs completos no GitHub Actions

### 9.5 Erro na Validação Kubernetes

**Problema:** `kubeconform` encontra erros

**Soluções:**
1. Validar YAML localmente:
   ```bash
   # Instalar kubeconform
   # Validar arquivos
   kubeconform -strict k8s/
   ```

2. Verificar sintaxe YAML
3. Verificar se campos obrigatórios estão presentes
4. Consultar documentação Kubernetes

### 9.6 Comandos de Diagnóstico

```bash
# Ver status do workflow no GitHub
# Acesse: https://github.com/seu-usuario/seu-repo/actions

# Ver logs de uma execução específica
# Clique na execução → Ver logs de cada etapa

# Testar workflow localmente
act push

# Validar sintaxe YAML
yamllint .github/workflows/ci-cd.yml
```

---

## 10. Boas Práticas

### 10.1 ✅ Faça Isso

1. **Teste Localmente Primeiro**
   - Execute comandos manualmente antes de commitar
   - Use `act` para testar workflow

2. **Commits Atômicos**
   - Um commit = uma mudança relacionada
   - Facilita identificar problemas

3. **Mensagens de Commit Descritivas**
   ```bash
   git commit -m "Atualiza modelo de ML com novos parâmetros"
   ```

4. **Monitore Execuções**
   - Verifique status no GitHub Actions
   - Corrija problemas rapidamente

5. **Mantenha Workflow Simples**
   - Evite lógica complexa no workflow
   - Use scripts separados quando necessário

### 10.2 ❌ Evite Isso

1. **Não Commite Direto na Main**
   - Use branches e pull requests
   - Permite revisão antes de merge

2. **Não Ignore Falhas**
   - Corrija workflows quebrados imediatamente
   - Workflows falhando indicam problemas

3. **Não Use Secrets em Logs**
   - GitHub Actions oculta secrets automaticamente
   - Não imprima secrets em comandos

4. **Não Faça Workflows Muito Longos**
   - Divida em múltiplos jobs se necessário
   - Jobs podem rodar em paralelo

5. **Não Esqueça de Atualizar Requirements**
   - Mantenha `requirements.txt` atualizado
   - Workflow usa este arquivo

### 10.3 Melhorias Futuras

Possíveis melhorias para o workflow:

1. **Testes Automatizados**
   ```yaml
   - name: Executar testes
     run: pytest
   ```

2. **Notificações**
   ```yaml
   - name: Notificar sucesso
     uses: 8398a7/action-slack@v3
   ```

3. **Deploy Automático**
   ```yaml
   - name: Deploy no Kubernetes
     run: kubectl apply -f k8s/
   ```

4. **Cache de Dependências**
   ```yaml
   - uses: actions/cache@v3
     with:
       path: ~/.cache/pip
   ```

5. **Matrix de Versões**
   ```yaml
   strategy:
     matrix:
       python-version: [3.11, 3.12]
   ```

---

## 11. Resumo

### 11.1 Conceitos Principais

1. **CI/CD**: Automação de integração e deploy
2. **GitHub Actions**: Plataforma de automação do GitHub
3. **Workflow**: Arquivo YAML que define processo automatizado
4. **Triggers**: Eventos que disparam o workflow
5. **Jobs e Steps**: Estrutura do workflow

### 11.2 Workflow do Projeto

```
Push na main + Mudanças em arquivos específicos
    ↓
Checkout código
    ↓
Instalar Node.js e Python
    ↓
Instalar dependências
    ↓
Treinar modelo ML
    ↓
Construir imagem Docker
    ↓
Validar Kubernetes
    ↓
✅ Pronto para deploy
```

### 11.3 Comandos Essenciais

```bash
# Testar workflow localmente
act push

# Ver workflows
act -l

# Executar workflow no GitHub
git add .
git commit -m "Mensagem"
git push origin main
```

---

**Última atualização:** Janeiro 2025  
**Versão:** 1.0  
**Projeto:** Projeto 6 - AIVK

