# PRD - Product Requirements Document
## Projeto 6: Sistema de Controle de Qualidade com IA e Pipeline CI/CD

### 1. VISÃO GERAL DO PRODUTO

#### 1.1 Nome do Produto
**AIVK - Agência de IA Aivoraq - Sistema de Controle de Qualidade**

#### 1.2 Descrição
Sistema de machine learning para previsão de qualidade de produtos alimentares, integrado com pipeline CI/CD completo usando GitHub Actions e Kubernetes. O sistema permite que usuários insiram parâmetros de fabricação e recebam previsões sobre a aprovação/reprovação do produto no teste de qualidade.

#### 1.3 Objetivos
- Automatizar o processo de controle de qualidade em indústrias alimentícias
- Implementar pipeline CI/CD robusto para deploy automatizado
- Demonstrar boas práticas de DevOps e MLOps
- Criar sistema escalável e containerizado

### 2. ARQUITETURA DO SISTEMA

#### 2.1 Componentes Principais
- **Aplicação Web**: Interface Streamlit para interação do usuário
- **Modelo de ML**: RandomForestClassifier para classificação de qualidade
- **Pipeline CI/CD**: GitHub Actions para automação
- **Containerização**: Docker para empacotamento
- **Orquestração**: Kubernetes para deploy e gerenciamento

#### 2.2 Stack Tecnológica
- **Backend**: Python 3.12
- **ML Framework**: scikit-learn
- **Web Framework**: Streamlit
- **Containerização**: Docker
- **Orquestração**: Kubernetes (Minikube)
- **CI/CD**: GitHub Actions + Act (teste local)
- **Versionamento**: Git

### 3. FUNCIONALIDADES

#### 3.1 Funcionalidades Core
1. **Interface de Previsão**
   - Input de 5 parâmetros: Peso, Temperatura, pH, Umidade, Tempo de Cozimento
   - Output: Aprovação/Reprovação + Probabilidades
   - Interface intuitiva com validação de dados

2. **Modelo de Machine Learning**
   - Algoritmo: RandomForestClassifier
   - Dataset: 1.250 amostras sintéticas
   - Features: 5 variáveis de processo
   - Target: Binário (0=Reprovado, 1=Aprovado)

3. **Pipeline CI/CD**
   - Build automatizado de imagem Docker
   - Deploy automático no Kubernetes
   - Testes locais com Act
   - Versionamento de modelos

#### 3.2 Funcionalidades de Infraestrutura
1. **Containerização**
   - Dockerfile otimizado
   - Imagem base Python 3.12-slim
   - Dependências gerenciadas via requirements.txt

2. **Orquestração Kubernetes**
   - Deployment com 1 réplica
   - Service NodePort para exposição
   - Configuração de recursos

3. **CI/CD Pipeline**
   - **Workflow**: `AIVKProjeto6` (`.github/workflows/ci-cd.yml`)
   - **Triggers**: 
     - Push para branch `main`
     - Modificações em: `modelos/**`, `treinamento/**`, `appaivk.py`, `requirements.txt`, `Dockerfile`
   - **Etapas**:
     - Checkout do código
     - Instalação do Node.js e Python 3.12
     - Instalação de dependências
     - Treinamento do modelo de ML
     - Build da imagem Docker
     - Validação dos manifestos Kubernetes
   - **Teste Local**: Validação com Act antes do push

### 4. ESPECIFICAÇÕES TÉCNICAS

#### 4.1 Requisitos de Sistema
- **Sistema Operacional**: Windows 10/11, macOS, Linux
- **Docker Desktop**: Versão mais recente
- **Kubernetes**: Minikube
- **Python**: 3.12
- **Memória**: Mínimo 4GB RAM
- **Armazenamento**: 2GB livres

#### 4.2 Dependências Python
```
streamlit==1.43.0
scikit-learn==1.6.1
numpy==2.1.3
pandas==2.2.3
joblib==1.4.2
```

#### 4.3 Configurações de Rede
- **Porta da Aplicação**: 8501
- **Porta do Service**: 30002 (NodePort)
- **Protocolo**: TCP

#### 4.4 Estrutura de Diretórios
```
proj_6/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Workflow GitHub Actions
├── docs/                      # Documentação do projeto
├── k8s/                       # Manifestos Kubernetes
│   ├── deployment.yaml        # Configuração do Deployment
│   └── service.yaml           # Configuração do Service
├── modelos/                    # Modelos de ML treinados
│   └── modelo_qualidade_aivk.pkl
├── treinamento/               # Scripts de treinamento
│   └── aivk_treina_modelo.py
├── appaivk.py                 # Aplicação Streamlit principal
├── Dockerfile                 # Configuração do container
├── requirements.txt           # Dependências Python
└── LEIAME1.txt               # Documentação de setup
```

### 5. FLUXO DE TRABALHO

#### 5.1 Pipeline de Desenvolvimento
1. **Desenvolvimento Local**
   - Criação/atualização do código
   - Treinamento do modelo
   - Testes locais

2. **Versionamento**
   - Git add/commit
   - Push para repositório

3. **CI/CD Automatizado**
   - GitHub Actions trigger
   - Build da imagem Docker
   - Deploy no Kubernetes

#### 5.2 Pipeline de ML
1. **Treinamento**
   - Geração de dados sintéticos
   - Treinamento do RandomForest
   - Salvamento do modelo (.pkl)

2. **Versionamento de Modelo**
   - Backup automático com timestamp (formato: `modelo_qualidade_aivk_YYYYMMDD_HHMMSS.pkl`)
   - Nomenclatura padronizada: `modelo_qualidade_aivk.pkl` (sempre o mais recente)
   - Armazenamento em `modelos/`
   - Versões anteriores são preservadas automaticamente

### 6. CRITÉRIOS DE ACEITAÇÃO

#### 6.1 Funcionalidade
- ✅ Interface web carrega corretamente
- ✅ Modelo faz previsões precisas
- ✅ Validação de inputs funciona
- ✅ Outputs são apresentados claramente

#### 6.2 Performance
- ✅ Aplicação inicia em < 30 segundos
- ✅ Previsões são geradas em < 2 segundos
- ✅ Interface responsiva

#### 6.3 Infraestrutura
- ✅ Docker build executa sem erros
- ✅ Kubernetes deploy funciona
- ✅ Aplicação acessível via browser
- ✅ Pipeline CI/CD executa completamente

#### 6.4 Qualidade
- ✅ Código bem documentado
- ✅ Estrutura de projeto organizada
- ✅ Versionamento adequado
- ✅ Testes locais passam

### 7. RISCOS E MITIGAÇÕES

#### 7.1 Riscos Técnicos
- **Risco**: Falha no build Docker
  - **Mitigação**: Testes locais com Act
- **Risco**: Problemas de conectividade K8s
  - **Mitigação**: Verificação de contexto kubectl
- **Risco**: Dependências desatualizadas
  - **Mitigação**: Versionamento fixo no requirements.txt

#### 7.2 Riscos de Negócio
- **Risco**: Modelo com baixa acurácia
  - **Mitigação**: Validação com métricas de performance
- **Risco**: Interface não intuitiva
  - **Mitigação**: Testes de usabilidade

### 8. CRONOGRAMA DE DESENVOLVIMENTO

#### 8.1 Fase 1: Setup Inicial (1-2 dias)
- Configuração do ambiente Python
- Instalação de dependências
- Configuração do Git

#### 8.2 Fase 2: Desenvolvimento Core (2-3 dias)
- Implementação da aplicação Streamlit
- Treinamento do modelo ML
- Testes básicos

#### 8.3 Fase 3: Containerização (1 dia)
- Criação do Dockerfile
- Build e testes da imagem
- Otimização do container

#### 8.4 Fase 4: Kubernetes (1-2 dias)
- Configuração do Minikube
- Criação dos manifestos K8s
- Deploy e testes

#### 8.5 Fase 5: CI/CD (1-2 dias)
- Configuração do GitHub Actions
- Testes locais com Act
- Validação do pipeline completo

### 9. MÉTRICAS DE SUCESSO

#### 9.1 Métricas Técnicas
- **Build Time**: < 5 minutos
- **Deploy Time**: < 2 minutos
- **Uptime**: > 99%
- **Response Time**: < 2 segundos

#### 9.2 Métricas de Qualidade
- **Acurácia do Modelo**: > 85%
- **Cobertura de Testes**: > 80%
- **Documentação**: 100% das funcionalidades

### 10. CONSIDERAÇÕES FUTURAS

#### 10.1 Melhorias Planejadas
- Implementação de monitoramento (Prometheus/Grafana)
- Adição de testes automatizados
- Integração com banco de dados
- Sistema de logging avançado

#### 10.2 Escalabilidade
- Suporte a múltiplas réplicas
- Load balancing
- Auto-scaling baseado em métricas
- Integração com cloud providers

### 11. DOCUMENTAÇÃO E SUPORTE

#### 11.1 Documentação Técnica
- README.md com instruções de setup
- Documentação de API
- Guias de troubleshooting
- Arquitetura do sistema

#### 11.2 Suporte
- Email: suporte@aivoraq.com.br
- Documentação online
- Exemplos de uso
- FAQ técnico

---

**Versão**: 1.0  
**Data**: Janeiro 2025  
**Autor**: Equipe AIVK  
**Status**: Em Desenvolvimento
