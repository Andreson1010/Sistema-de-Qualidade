# Guia Completo de Git e GitHub CLI

Este documento apresenta um guia passo a passo para trabalhar com Git e GitHub CLI, desde a instalação até o fluxo de trabalho diário.

## Índice

1. [Instalação do GitHub CLI](#1-instalação-do-github-cli)
2. [Configuração Inicial do Git](#2-configuração-inicial-do-git)
3. [Autenticação no GitHub](#3-autenticação-no-github)
4. [Inicialização de Repositório](#4-inicialização-de-repositório)
5. [Fluxo de Trabalho Diário](#5-fluxo-de-trabalho-diário)
6. [Comandos Essenciais](#6-comandos-essenciais)
7. [Casos Especiais](#7-casos-especiais)
8. [Ciclo de Trabalho Completo](#8-ciclo-de-trabalho-completo)

---

## 1. Instalação do GitHub CLI

### 1.1 Instalação no Linux/WSL2

#### Opção A: Usando apt (Recomendado)

```bash
# Adicionar a chave GPG oficial do GitHub
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Atualizar lista de pacotes
sudo apt update

# Instalar GitHub CLI
sudo apt install gh
```

**Explicação dos comandos:**
- `curl -fsSL`: Baixa a chave GPG do GitHub de forma segura (f=silent, s=show errors, L=follow redirects)
- `sudo dd of=...`: Salva a chave GPG no sistema
- `sudo chmod go+r`: Dá permissão de leitura para grupo e outros
- `echo "deb [...]" | sudo tee`: Adiciona o repositório do GitHub CLI à lista de fontes do apt
- `sudo apt update`: Atualiza a lista de pacotes disponíveis
- `sudo apt install gh`: Instala o GitHub CLI

#### Opção B: Usando snap

```bash
sudo snap install gh
```

#### Opção C: Usando script de instalação oficial

```bash
type -p curl >/dev/null || (apt update && apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

### 1.2 Verificar Instalação

```bash
gh --version
```

**Objetivo:** Confirma que o GitHub CLI foi instalado corretamente e mostra a versão.

---

## 2. Configuração Inicial do Git

### 2.1 Configurar Identidade Global

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

**Explicação:**
- `git config`: Comando para configurar o Git
- `--global`: Aplica a configuração para todos os repositórios do usuário
- `user.name`: Define o nome que aparecerá nos commits
- `user.email`: Define o email associado aos commits

**Objetivo:** Identificar o autor dos commits. O email deve ser o mesmo usado na conta do GitHub para que os commits sejam associados ao seu perfil.

### 2.2 Configurar Identidade Apenas para um Repositório

```bash
git config user.name "Seu Nome"
git config user.email "seu-email@exemplo.com"
```

**Diferença:** Sem `--global`, a configuração aplica apenas ao repositório atual.

### 2.3 Verificar Configurações

```bash
# Ver todas as configurações globais
git config --global --list

# Ver todas as configurações (global + local)
git config --list

# Ver uma configuração específica
git config user.name
git config user.email
```

**Objetivo:** Verificar se as configurações foram aplicadas corretamente.

### 2.4 Outras Configurações Úteis

```bash
# Configurar editor padrão (opcional)
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "nano"        # Nano
git config --global core.editor "vim"          # Vim

# Configurar branch padrão
git config --global init.defaultBranch main

# Configurar comportamento de push
git config --global push.default simple
```

---

## 3. Autenticação no GitHub

### 3.1 Login no GitHub CLI

```bash
gh auth login
```

**O que acontece:**
1. O CLI pergunta o tipo de autenticação (GitHub.com ou GitHub Enterprise)
2. Escolha o protocolo (HTTPS ou SSH)
3. Escolha como autenticar:
   - **Login via navegador** (recomendado)
   - **Token de acesso pessoal**

### 3.2 Login via Navegador (WSL2/Linux)

Se o navegador não abrir automaticamente:

1. O CLI mostrará uma URL e um código de dispositivo:
   ```
   ! First copy your one-time code: XXXX-XXXX
   Press Enter to open https://github.com/login/device in your browser...
   ```

2. Abra manualmente no navegador: `https://github.com/login/device`

3. Digite o código fornecido

4. Autorize o dispositivo

5. Volte ao terminal e pressione Enter

**Objetivo:** Autenticar o GitHub CLI para permitir operações como criar repositórios, fazer push, etc.

### 3.3 Login via Token

```bash
gh auth login --with-token
```

Depois cole um token pessoal. Para criar um token:

1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" > "Generate new token (classic)"
3. Selecione os escopos necessários (pelo menos `repo`)
4. Copie o token e cole no terminal

**Objetivo:** Alternativa quando o login via navegador não funciona.

### 3.4 Verificar Status de Autenticação

```bash
gh auth status
```

**Objetivo:** Verificar se você está autenticado e qual conta está sendo usada.

### 3.5 Logout

```bash
gh auth logout
```

**Objetivo:** Desconectar do GitHub CLI.

---

## 4. Inicialização de Repositório

### 4.1 Criar Repositório Local

```bash
# Inicializar repositório Git no diretório atual
git init
```

**Explicação:**
- `git init`: Cria a pasta `.git` que contém todo o histórico e configurações do repositório
- A pasta atual se torna a raiz do repositório Git

**Objetivo:** Transformar um diretório comum em um repositório Git versionado.

### 4.2 Criar Repositório no GitHub e Conectar

#### Opção A: Criar via GitHub CLI (Recomendado)

```bash
gh repo create nome-do-repositorio --public --source=. --remote=origin --push
```

**Explicação dos elementos:**
- `gh repo create`: Comando para criar repositório no GitHub
- `nome-do-repositorio`: Nome do repositório no GitHub
- `--public`: Repositório público (ou `--private` para privado)
- `--source=.`: Usa o diretório atual como fonte
- `--remote=origin`: Adiciona o remote como "origin"
- `--push`: Faz push automático após criar (requer commits)

**Objetivo:** Criar repositório no GitHub e conectar o repositório local automaticamente.

#### Opção B: Criar sem Push Automático

```bash
gh repo create nome-do-repositorio --public --source=. --remote=origin
git push -u origin main
```

**Objetivo:** Criar o repositório primeiro, depois fazer push manualmente.

#### Opção C: Criar Manualmente no GitHub

1. Acesse: https://github.com/new
2. Preencha o nome do repositório
3. Escolha público ou privado
4. **Não** inicialize com README, .gitignore ou licença (se já tiver código local)
5. Clique em "Create repository"

Depois conecte o repositório local:

```bash
git remote add origin https://github.com/seu-usuario/nome-do-repo.git
git branch -M main
git push -u origin main
```

**Explicação:**
- `git remote add origin`: Adiciona o repositório remoto com o nome "origin"
- `git branch -M main`: Renomeia a branch atual para "main" (se necessário)
- `git push -u origin main`: Envia commits e configura tracking

### 4.3 Gerenciar Remotes Configurados

```bash
# Ver remotes configurados
git remote -v
# -v: Flag "verbose" - mostra URL completa (fetch e push)

# Ver detalhes de um remote específico
git remote show origin
# Mostra informações sobre branches remotas, tracking, etc.

# Adicionar um novo remote
git remote add nome-do-remote https://github.com/usuario/repo.git

# Remover um remote
git remote remove origin
# ou
git remote rm origin

# Renomear um remote
git remote rename origin upstream

# Alterar URL de um remote
git remote set-url origin https://github.com/novo-usuario/repo.git
```

**Objetivo:** Gerenciar repositórios remotos configurados.

#### 4.3.1 Sobre Conexões com Remotes

**⚠️ Importante: Não há necessidade de "fechar" conexão com remoto!**

**Por quê?**
- O Git **não mantém conexões persistentes** com repositórios remotos
- Cada comando (`push`, `pull`, `fetch`) faz uma **conexão temporária** e a fecha automaticamente
- Após o comando terminar, a conexão já está fechada
- Não há processo em background mantendo conexão aberta

**Como funciona:**
```bash
git push    # 1. Abre conexão → 2. Envia dados → 3. Fecha conexão automaticamente
git pull    # 1. Abre conexão → 2. Baixa dados → 3. Fecha conexão automaticamente
git fetch   # 1. Abre conexão → 2. Busca informações → 3. Fecha conexão automaticamente
```

**O que você pode fazer:**
- **Remover um remote** se não precisar mais dele (mas isso não "fecha" conexão, apenas remove a configuração)
- **Alterar URL** se o repositório mudou de local
- **Verificar remotes** para ver quais estão configurados

**Quando remover um remote?**
- Se você não precisa mais desse repositório remoto
- Se mudou para outro repositório
- Se está limpando configurações antigas

**Exemplo de remoção (se necessário):**
```bash
# Ver remotes atuais
git remote -v
# origin  https://github.com/usuario/repo.git (fetch)
# origin  https://github.com/usuario/repo.git (push)

# Remover remote (se não precisar mais)
git remote remove origin

# Verificar que foi removido
git remote -v
# (não mostra nada)
```

**Resumo:** Não precisa fechar conexão porque ela não fica aberta. Cada comando Git abre e fecha sua própria conexão automaticamente.

### 4.4 Primeiro Commit

```bash
# Adicionar todos os arquivos ao staging
git add .

# Criar o primeiro commit
git commit -m "Initial commit"

# Fazer push para o GitHub
git push -u origin main
```

**Explicação:**
- `git add .`: Adiciona todos os arquivos ao staging area (respeitando `.gitignore`)
- `git commit -m "mensagem"`: Cria um commit com a mensagem especificada
- `git push -u origin main`: Envia commits para o GitHub e configura tracking (`-u` = `--set-upstream`)

**Objetivo:** Fazer o primeiro commit e enviar o código para o GitHub.

---

## 5. Fluxo de Trabalho Diário

### 5.1 Fluxo Básico (Três Estágios)

O Git trabalha com três áreas principais:

1. **Working Directory** (Diretório de Trabalho): Onde você edita arquivos
2. **Staging Area** (Área de Preparação): Arquivos selecionados para commit
3. **Repository** (Repositório): Histórico de commits

```
Working Directory → Staging Area → Repository
     (git add)         (git commit)
```

### 5.2 Comandos do Fluxo Básico

```bash
# 1. Ver status dos arquivos
git status

# 2. Adicionar arquivos ao staging
git add arquivo.txt           # Arquivo específico
git add .                     # Todos os arquivos modificados
git add src/                  # Diretório específico

# 3. Criar commit
git commit -m "Descrição das mudanças"

# 4. Enviar para o GitHub
git push
```

**Objetivo de cada comando:**
- `git status`: Ver quais arquivos foram modificados, adicionados ou removidos
- `git add`: Preparar arquivos para commit
- `git commit`: Criar um snapshot das mudanças
- `git push`: Enviar commits para o repositório remoto

### 5.3 Verificar Mudanças Antes de Commitar

```bash
# Ver diferenças no working directory
git diff

# Ver diferenças no staging area
git diff --staged
# ou
git diff --cached

# Ver histórico de commits
git log --oneline
```

**Objetivo:** Revisar mudanças antes de fazer commit.

---

## 6. Comandos Essenciais

### 6.1 Status e Informações

```bash
# Status do repositório
git status

# Status resumido
git status -s

# Ver branch atual
git branch

# Ver todas as branches (locais e remotas)
git branch -a

# Ver histórico de commits
git log

# Histórico resumido (uma linha por commit)
git log --oneline

# Histórico com gráfico
git log --oneline --graph --all

# Ver informações do remote
git remote -v
```

### 6.2 Adicionar e Remover Arquivos

```bash
# Adicionar arquivo específico
git add arquivo.txt

# Adicionar todos os arquivos modificados
git add .

# Adicionar arquivo interativo (escolher partes)
git add -p arquivo.txt

# Remover arquivo do Git (mantém no disco)
git rm --cached arquivo.txt

# Remover arquivo do Git e do disco
git rm arquivo.txt
```

### 6.3 Commits

```bash
# Commit com mensagem
git commit -m "Mensagem do commit"

# Commit abrindo editor para mensagem
git commit

# Commit adicionando todos os arquivos modificados (pula git add)
git commit -am "Mensagem"

# Modificar último commit (adicionar arquivos ou mudar mensagem)
git commit --amend

# Modificar último commit mantendo mensagem
git commit --amend --no-edit
```

**Objetivo:** `--amend` permite corrigir o último commit antes de fazer push.

### 6.4 Push e Pull

```bash
# Enviar commits para o remote
git push

# Enviar e configurar tracking
git push -u origin main

# Baixar mudanças do remote
git pull

# Baixar sem fazer merge (apenas atualizar referências)
git fetch

# Ver diferenças entre local e remote
git fetch
git diff main origin/main
```

**Diferença entre pull e fetch:**
- `git pull`: Faz `fetch` + `merge` automaticamente
- `git fetch`: Apenas baixa informações, não modifica seu código

### 6.5 Branches

#### 6.5.0 O Que São Branches? (Conceito Fundamental)

**⚠️ Importante: Uma branch NÃO é um projeto separado!**

Quando você cria uma branch, você **NÃO está criando outro projeto**. Você está criando uma **linha de desenvolvimento alternativa** dentro do **mesmo repositório**.

**Analogia simples:**
- Pense em branches como **diferentes "linhas do tempo"** do mesmo projeto
- É como ter **várias versões da história** que você pode alternar
- Todos os arquivos estão no **mesmo diretório físico**
- Você apenas muda **qual versão dos arquivos** está visível/trabalhando

**Exemplo prático:**

```bash
# Você está no diretório: /home/francisco/projects/traders
# Este é o SEU ÚNICO projeto

# Criar branch não cria novo diretório!
git checkout -b feature/nova-funcionalidade

# Você ainda está em: /home/francisco/projects/traders
# Os mesmos arquivos, mas agora você está vendo/trabalhando na "versão" da branch
```

**O que acontece quando você cria uma branch:**

1. ✅ **Mesmo diretório físico** - você continua no mesmo projeto
2. ✅ **Mesmos arquivos** - os arquivos não são duplicados
3. ✅ **Apenas muda o "ponteiro"** - Git marca qual versão dos arquivos você está vendo
4. ✅ **Histórico compartilhado** - branches compartilham o histórico até o ponto de criação

**Visualização:**

```
Repositório: traders/
├── Arquivos físicos (mesmos para todas as branches)
│   ├── src/
│   ├── config/
│   └── ...
│
└── Histórico Git (diferentes "linhas do tempo")
    ├── main ──────────────→ [commit 1] → [commit 2] → [commit 3]
    │
    └── feature/nova-func ──→ [commit 1] → [commit 2] → [commit 4] → [commit 5]
                              ↑
                         Divergem aqui
```

**Quando você muda de branch:**

```bash
# Está em main
git checkout main
# Arquivos mostram versão da main

# Muda para feature branch
git checkout feature/nova-funcionalidade
# Mesmos arquivos, mas mostram versão da feature branch
# Mudanças feitas aqui não aparecem em main (até fazer merge)
```

**Resumo:**
- ❌ **NÃO** cria novo projeto
- ❌ **NÃO** duplica arquivos
- ❌ **NÃO** cria novo diretório
- ✅ **SIM** cria linha de desenvolvimento alternativa
- ✅ **SIM** permite trabalhar em versões diferentes do mesmo código
- ✅ **SIM** permite alternar entre versões facilmente

#### 6.5.1 Comandos de Branches

```bash
# Criar nova branch
git branch nome-da-branch

# Criar e mudar para a branch
git checkout -b nome-da-branch
# ou (Git 2.23+)
git switch -c nome-da-branch

# Mudar de branch
git checkout nome-da-branch
# ou
git switch nome-da-branch

# Deletar branch local
git branch -d nome-da-branch

# Deletar branch forçadamente
git branch -D nome-da-branch

# Deletar branch remota
git push origin --delete nome-da-branch

# Ver branches remotas
git branch -r
```

**Objetivo:** Branches permitem trabalhar em features isoladas sem afetar o código principal, tudo dentro do mesmo projeto.

#### 6.5.2 Por Que Criar Branches?

Branches são uma das funcionalidades mais poderosas do Git. Aqui estão os principais motivos para usá-las:

**1. Isolamento de Funcionalidades**
- Trabalhar em uma nova feature sem afetar o código principal
- Testar mudanças experimentais sem risco
- Manter o código principal sempre estável e funcional

**2. Trabalho Paralelo**
- Trabalhar em múltiplas features simultaneamente
- Alternar entre diferentes contextos de trabalho facilmente
- Evitar misturar mudanças não relacionadas

**3. Histórico Organizado**
- Commits relacionados ficam agrupados em branches específicas
- Facilita revisão de código e entendimento do histórico
- Permite identificar facilmente quando uma feature foi adicionada

**4. Colaboração**
- Múltiplos desenvolvedores podem trabalhar sem conflitos
- Facilita code review através de Pull Requests
- Permite revisar mudanças antes de integrar ao código principal

**5. Segurança**
- Protege o código principal (main) de mudanças quebradas
- Permite reverter facilmente se algo der errado
- Facilita rollback de features problemáticas

**6. Experimentação**
- Testar ideias sem comprometer o código estável
- Comparar diferentes abordagens em branches separadas
- Descartar experimentos facilmente

#### 6.5.3 Quando Criar Branches?

**Após Criar o Repositório no GitHub:**

✅ **Recomendado:** Sim, é uma boa prática criar branches mesmo trabalhando sozinho.

**Por quê?**
- Mantém o código principal (`main`) sempre estável
- Facilita organização do trabalho
- Prepara o projeto para crescimento futuro
- Cria hábitos que serão úteis quando a equipe crescer

**Estratégia Recomendada:**
```bash
# 1. Após criar repositório e fazer primeiro commit
git push -u origin main

# 2. Criar branch de desenvolvimento
# Objetivo: Criar uma branch separada para desenvolvimento, mantendo main estável
git checkout -b develop
# git checkout: Comando para mudar de branch ou restaurar arquivos
# -b: Flag que significa "branch" - cria uma nova branch se ela não existir
# develop: Nome da nova branch de desenvolvimento
# Resultado: Cria a branch "develop" e muda para ela automaticamente

git push -u origin develop
# git push: Envia commits locais para o repositório remoto (GitHub)
# -u: Flag "--set-upstream" - configura a branch local para rastrear a branch remota
#     Isso permite usar apenas "git push" depois, sem especificar origin/develop
# origin: Nome do repositório remoto (geralmente o GitHub)
# develop: Nome da branch remota que será criada no GitHub
# Objetivo: Criar a branch develop no GitHub e configurar tracking

# 3. Para cada nova feature/funcionalidade
# Objetivo: Criar uma branch isolada para trabalhar em uma feature específica
git checkout develop
# git checkout: Muda para a branch especificada
# develop: Branch de destino
# Objetivo: Garantir que está na branch develop antes de criar a feature branch

git checkout -b feature/nome-da-feature
# git checkout -b: Cria nova branch e muda para ela
# -b: Cria a branch se não existir
# feature/nome-da-feature: Nome da branch seguindo convenção (feature/prefixo + nome descritivo)
# Objetivo: Criar branch isolada para a feature, baseada na develop atual

# ... trabalhar na feature ...
# (Aqui você edita arquivos, faz mudanças, testa, etc.)

git commit -m "feat: adiciona funcionalidade X"
# git commit: Cria um snapshot das mudanças no histórico
# -m: Flag que permite especificar mensagem diretamente na linha de comando
# "feat: adiciona funcionalidade X": Mensagem do commit seguindo convenção
#   - "feat:" indica que é uma nova funcionalidade
#   - Mensagem descritiva do que foi adicionado
# Objetivo: Salvar as mudanças da feature no histórico da branch

git push -u origin feature/nome-da-feature
# git push: Envia commits para o repositório remoto
# -u: Configura tracking entre branch local e remota
# origin: Repositório remoto (GitHub)
# feature/nome-da-feature: Nome da branch remota (mesma da local)
# Objetivo: Enviar a feature branch para o GitHub e configurar tracking

# 4. Quando feature estiver pronta, fazer merge em develop
# Objetivo: Integrar a feature completa na branch de desenvolvimento
git checkout develop
# git checkout: Muda de branch
# develop: Branch de destino (onde a feature será integrada)
# Objetivo: Mudar para develop para receber o merge da feature

git merge feature/nome-da-feature
# git merge: Integra mudanças de uma branch na branch atual
# feature/nome-da-feature: Branch que será integrada (fonte)
# Objetivo: Trazer todas as mudanças da feature branch para develop
# Resultado: develop agora contém as mudanças da feature

git push
# git push: Envia commits para o repositório remoto
# (Não precisa especificar origin/develop porque foi configurado com -u anteriormente)
# Objetivo: Atualizar a branch develop no GitHub com as mudanças da feature

# 5. Quando develop estiver estável, fazer merge em main
# Objetivo: Integrar o código estável de develop na branch principal (produção)
git checkout main
# git checkout: Muda de branch
# main: Branch principal do projeto (código de produção/estável)
# Objetivo: Mudar para main para receber o merge de develop

git merge develop
# git merge: Integra mudanças de uma branch na branch atual
# develop: Branch que será integrada (contém todas as features testadas)
# Objetivo: Trazer todas as mudanças estáveis de develop para main
# Resultado: main agora contém todas as features validadas

git push
# git push: Envia commits para o repositório remoto
# Objetivo: Atualizar a branch main no GitHub com o código estável

#### 6.5.4 Devo Criar uma Branch para Cada Alteração?

**Depende do tamanho e complexidade da alteração:**

✅ **Crie uma branch para:**
- Nova funcionalidade completa
- Correção de bug que requer múltiplos arquivos
- Refatoração significativa
- Experimentos ou testes
- Qualquer mudança que possa quebrar o código

❌ **Não precisa criar branch para:**
- Correções de typo em comentários
- Ajustes de formatação simples
- Atualizações de documentação pequenas
- Mudanças muito pequenas e isoladas

**Regra prática:**
- Se a mudança levar mais de 15-30 minutos → crie uma branch
- Se a mudança afetar múltiplos arquivos → crie uma branch
- Se houver risco de quebrar algo → crie uma branch
- Se for uma mudança experimental → crie uma branch

**Exemplo de organização:**
```bash
# Feature grande - branch separada
git checkout -b feature/autenticacao-oauth

# Bug fix médio - branch separada
git checkout -b fix/correcao-calculo-saldo

# Ajuste pequeno - pode commitar direto em develop/main
git checkout develop
# ... fazer mudança pequena ...
git commit -m "docs: corrige typo no README"
```

#### 6.5.5 Trabalhando Sozinho: Manter Main como Branch Principal?

**Sim, mantenha `main` como branch principal**, mas use uma estratégia adequada:

**Opção A: Estratégia Simples (Recomendada para projetos pequenos/solo)**

```bash
# Trabalhar diretamente em main para mudanças pequenas
git checkout main
git pull
# ... fazer mudanças ...
git add .
git commit -m "feat: adiciona funcionalidade X"
git push

# Criar branch apenas para features grandes ou experimentos
git checkout -b feature/experimento-grande
# ... trabalhar ...
git checkout main
git merge feature/experimento-grande
```

**Vantagens:**
- Simplicidade
- Menos overhead
- Adequado para projetos pequenos

**Desvantagens:**
- Menos organização
- Risco de quebrar main

**Opção B: Estratégia com Develop (Recomendada para projetos maiores)**

```bash
# Estrutura:
# main → código em produção/estável
# develop → desenvolvimento ativo
# feature/* → features individuais

# Trabalhar sempre em develop ou feature branches
git checkout develop
git checkout -b feature/nova-funcionalidade
# ... trabalhar ...
git checkout develop
git merge feature/nova-funcionalidade
git push

# Quando develop estiver estável, fazer merge em main
git checkout main
git merge develop
git push
```

**Vantagens:**
- Organização melhor
- Main sempre estável
- Fácil escalar quando equipe crescer

**Desvantagens:**
- Mais overhead
- Pode ser excessivo para projetos muito pequenos

**Opção C: Híbrida (Boa para maioria dos casos)**

```bash
# main → código estável
# feature/* → features e mudanças significativas

# Mudanças pequenas → direto em main
git checkout main
git commit -m "docs: atualiza README"

# Mudanças grandes → branch separada
git checkout -b feature/refatoracao-banco-dados
# ... trabalhar ...
git checkout main
git merge feature/refatoracao-banco-dados
```

#### 6.5.6 Convenções de Nomenclatura de Branches

Use nomes descritivos e consistentes:

```bash
# Features
feature/autenticacao-oauth
feature/dashboard-admin

# Correções de bugs
fix/correcao-calculo
fix/memory-leak

# Hotfixes (correções urgentes)
hotfix/seguranca-critica

# Experimentos
experiment/nova-arquitetura
test/implementacao-alternativa

# Documentação
docs/atualiza-guia-instalacao

# Refatoração
refactor/reorganiza-estrutura
```

**Boas práticas:**
- Use letras minúsculas
- Separe palavras com hífen (`-`)
- Seja descritivo mas conciso
- Use prefixos para categorizar (feature/, fix/, etc.)

#### 6.5.7 Resumo: Estratégia Recomendada para Trabalho Solo

**Para você, trabalhando sozinho:**

1. **Mantenha `main` como branch principal** (código estável)
2. **Crie branches para:**
   - Features que levam tempo significativo
   - Experimentos ou testes
   - Mudanças que podem quebrar o código
3. **Trabalhe direto em `main` para:**
   - Correções pequenas
   - Atualizações de documentação
   - Ajustes simples e isolados
4. **Sempre faça pull antes de trabalhar:**
   ```bash
   git checkout main
   git pull
   ```
5. **Após completar uma feature em branch:**
   ```bash
   git checkout main
   git merge feature/nome-da-feature
   git push
   git branch -d feature/nome-da-feature  # deletar branch local
   ```

**Exemplo de fluxo diário:**
```bash
# Início do dia
git checkout main
git pull

# Trabalhar em feature grande
git checkout -b feature/nova-funcionalidade
# ... trabalhar ...
git add .
git commit -m "feat: implementa funcionalidade X"
git push -u origin feature/nova-funcionalidade

# Quando feature estiver completa
git checkout main
# Objetivo: Mudar para a branch main para receber o merge da feature

git pull
# Objetivo: Atualizar a branch main local com as últimas mudanças do repositório remoto
# Por quê fazer pull ANTES do merge?
# 1. Garante que main local está sincronizada com main remota (GitHub)
# 2. Evita conflitos: se houver mudanças remotas, você as integra antes do merge
# 3. Boa prática: sempre atualizar antes de fazer merge para evitar problemas
# 4. Se outras pessoas (ou você em outra máquina) fizeram push, você pega essas mudanças
# 5. Previne erros de merge que podem ocorrer se main local estiver desatualizada
# Resultado: main local agora está atualizada e pronta para receber a feature

git merge feature/nova-funcionalidade
# Objetivo: Integrar todas as mudanças da feature branch na main
# Agora o merge é seguro porque main está atualizada (graças ao pull anterior)

git push
# Objetivo: Enviar o merge para o GitHub, atualizando main remota

git branch -d feature/nova-funcionalidade
# Objetivo: Deletar a branch local da feature (já foi integrada, não é mais necessária)
# -d: Deleta apenas se a branch foi totalmente mergeada (seguro)
```

Esta estratégia mantém `main` estável enquanto permite experimentação e organização do trabalho.

### 6.6 Merge e Rebase

```bash
# Fazer merge de uma branch na atual
git merge nome-da-branch

# Fazer rebase da branch atual na main
git rebase main

# Continuar rebase após resolver conflitos
git rebase --continue

# Cancelar rebase
git rebase --abort
```

**Diferença:**
- **Merge**: Cria um commit de merge, preserva histórico completo
- **Rebase**: Reaplica commits em cima de outra branch, histórico linear

### 6.7 Desfazer Mudanças

```bash
# Desfazer mudanças em arquivo não commitado
git checkout -- arquivo.txt
# ou (Git 2.23+)
git restore arquivo.txt

# Remover arquivo do staging (mas manter mudanças)
git reset HEAD arquivo.txt
# ou
git restore --staged arquivo.txt

# Desfazer último commit (mantém mudanças no working directory)
git reset --soft HEAD~1

# Desfazer último commit (remove mudanças)
git reset --hard HEAD~1

# Voltar para um commit específico
git reset --hard <hash-do-commit>
```

**⚠️ Cuidado:** `--hard` descarta mudanças permanentemente!

---

## 7. Casos Especiais

### 7.1 Resolver Conflitos de Merge

Quando há conflitos durante merge ou pull:

```bash
# 1. Git marca os conflitos nos arquivos
# 2. Edite os arquivos manualmente, removendo marcadores:
#    <<<<<<< HEAD
#    seu código
#    =======
#    código do remote
#    >>>>>>> branch-name

# 3. Adicione os arquivos resolvidos
git add arquivo-resolvido.txt

# 4. Complete o merge
git commit
```

**Objetivo:** Resolver conflitos quando o mesmo arquivo foi modificado em branches diferentes.

### 7.2 Trabalhar com Arquivos Grandes

```bash
# Ver tamanho do repositório
du -sh .git

# Ver arquivos grandes no histórico
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sed -n 's/^blob //p' | sort --numeric-sort --key=2 | tail -10
```

**Dica:** Use Git LFS para arquivos grandes (imagens, vídeos, datasets).

### 7.3 Stash (Guardar Mudanças Temporariamente)

```bash
# Guardar mudanças não commitadas
git stash

# Guardar com mensagem
git stash save "trabalho em progresso"

# Ver lista de stashes
git stash list

# Aplicar último stash
git stash apply

# Aplicar e remover do stash
git stash pop

# Aplicar stash específico
git stash apply stash@{0}

# Deletar stash
git stash drop stash@{0}

# Limpar todos os stashes
git stash clear
```

**Objetivo:** Guardar mudanças temporariamente para mudar de branch ou fazer pull sem perder trabalho.

### 7.4 Ignorar Arquivos

Crie ou edite `.gitignore`:

```
# Python
__pycache__/
*.py[cod]
*.so

# Ambiente virtual
venv/
env/

# Arquivos de ambiente
.env
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

**Objetivo:** Evitar commitar arquivos desnecessários ou sensíveis.

### 7.5 Trabalhar com Submódulos

```bash
# Adicionar submódulo
git submodule add https://github.com/usuario/repo.git pasta/

# Inicializar submódulos
git submodule init

# Atualizar submódulos
git submodule update

# Clonar repositório com submódulos
git clone --recursive https://github.com/usuario/repo.git
```

**Objetivo:** Incluir outros repositórios Git dentro do seu projeto.

### 7.6 Tags (Versões)

```bash
# Criar tag anotada
git tag -a v1.0.0 -m "Versão 1.0.0"

# Criar tag simples
git tag v1.0.0

# Listar tags
git tag

# Enviar tags para remote
git push origin v1.0.0

# Enviar todas as tags
git push origin --tags

# Deletar tag local
git tag -d v1.0.0

# Deletar tag remota
git push origin --delete v1.0.0
```

**Objetivo:** Marcar versões específicas do projeto.

### 7.7 Reverter Commits

```bash
# Reverter um commit específico (cria novo commit)
git revert <hash-do-commit>

# Reverter último commit
git revert HEAD
```

**Diferença entre revert e reset:**
- `revert`: Cria novo commit desfazendo mudanças (seguro para commits já enviados)
- `reset`: Remove commits do histórico (perigoso para commits já enviados)

---

## 8. Ciclo de Trabalho Completo

### 8.1 Início do Dia (Retomando Trabalho)

```bash
# 1. Verificar branch atual
git branch

# 2. Mudar para branch de trabalho (se necessário)
git checkout main
# ou
git switch main

# 3. Baixar últimas mudanças do GitHub
git pull

# 4. Ver status do repositório
git status

# 5. Verificar se há mudanças locais não commitadas
# Se houver stash anterior, aplicar:
git stash list
git stash pop  # se necessário
```

**Objetivo:** Sincronizar com o código mais recente e preparar ambiente de trabalho.

### 8.2 Durante o Trabalho

```bash
# 1. Fazer mudanças nos arquivos
# (editar arquivos normalmente)

# 2. Verificar o que foi modificado
git status

# 3. Ver diferenças específicas
git diff arquivo.txt

# 4. Adicionar arquivos ao staging
git add arquivo.txt
# ou
git add .

# 5. Verificar o que será commitado
git diff --staged

# 6. Criar commit
git commit -m "Descrição clara das mudanças"

# 7. Continuar trabalhando ou fazer push
```

**Objetivo:** Trabalhar de forma organizada, fazendo commits frequentes e descritivos.

### 8.3 Antes de Fazer Push

```bash
# 1. Verificar status
git status

# 2. Ver histórico local
git log --oneline -5

# 3. Baixar mudanças remotas (se houver)
git fetch

# 4. Ver diferenças com remote
git log origin/main..main  # commits locais não enviados
git log main..origin/main  # commits remotos não baixados

# 5. Se houver mudanças remotas, fazer pull primeiro
git pull

# 6. Resolver conflitos se necessário (ver seção 7.1)

# 7. Fazer push
git push
```

**Objetivo:** Garantir que o código local está sincronizado antes de enviar.

### 8.4 Fim do Dia (Interrompendo Trabalho)

```bash
# 1. Verificar status
git status

# 2. Se houver mudanças não commitadas:
#    Opção A: Fazer commit
git add .
git commit -m "WIP: trabalho em progresso"
git push

#    Opção B: Guardar em stash (se não quiser commitar)
git stash save "trabalho em progresso - [data]"
git push  # se houver commits

# 3. Verificar que tudo está sincronizado
git status
git log --oneline -3
```

**Objetivo:** Salvar trabalho e deixar repositório em estado limpo para retomar no dia seguinte.

### 8.5 Exemplo Completo: Um Dia de Trabalho

```bash
# ===== INÍCIO DO DIA =====

# 1. Abrir terminal e navegar para o projeto
cd ~/projects/meu-projeto

# 2. Verificar branch e status
git branch
git status

# 3. Mudar para branch de desenvolvimento (se necessário)
git checkout develop
# ou criar nova branch para feature
git checkout -b feature/nova-funcionalidade

# 4. Baixar últimas mudanças
git pull

# 5. Aplicar stash anterior (se houver)
git stash list
git stash pop  # se necessário

# ===== TRABALHANDO =====

# 6. Fazer mudanças nos arquivos
# (editar código normalmente)

# 7. Verificar mudanças
git status
git diff

# 8. Adicionar arquivos modificados
git add src/arquivo.py

# 9. Criar commit
git commit -m "feat: adiciona nova funcionalidade X"

# 10. Continuar trabalhando...
# (repetir passos 6-9 conforme necessário)

# ===== ANTES DE FAZER PUSH =====

# 11. Verificar se há mudanças remotas
git fetch
git status

# 12. Se houver, fazer pull e resolver conflitos
git pull
# (resolver conflitos se necessário)

# 13. Fazer push
git push

# ===== FIM DO DIA =====

# 14. Verificar status final
git status

# 15. Se houver trabalho não finalizado:
git stash save "WIP: funcionalidade X - $(date +%Y-%m-%d)"

# 16. Ou fazer commit de trabalho em progresso
git add .
git commit -m "WIP: funcionalidade X em desenvolvimento"
git push

# 17. Verificar que está tudo ok
git log --oneline -5
```

### 8.6 Convenções de Mensagens de Commit

Use mensagens descritivas e siga convenções:

```
tipo(escopo): descrição curta

Corpo da mensagem (opcional)
Explicação mais detalhada das mudanças

Rodapé (opcional)
```

**Tipos comuns:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

**Exemplos:**
```bash
git commit -m "feat(ui): adiciona botão de exportar dados"
git commit -m "fix(auth): corrige validação de token expirado"
git commit -m "docs: atualiza guia de instalação"
```

---

## 9. Comandos Úteis Adicionais

### 9.1 Buscar no Histórico

```bash
# Buscar commits por mensagem
git log --grep="palavra-chave"

# Buscar commits que modificaram um arquivo
git log -- arquivo.txt

# Buscar commits por autor
git log --author="Nome"

# Buscar commits por data
git log --since="2024-01-01" --until="2024-12-31"
```

### 9.2 Limpar Repositório

```bash
# Remover arquivos não rastreados
git clean -n  # dry-run (mostra o que será removido)
git clean -f  # remove arquivos
git clean -fd # remove arquivos e diretórios

# Limpar referências remotas obsoletas
git remote prune origin
```

### 9.3 Informações Detalhadas

```bash
# Ver estatísticas de um commit
git show <hash>

# Ver diferenças entre dois commits
git diff <hash1> <hash2>

# Ver quem modificou cada linha de um arquivo
git blame arquivo.txt

# Ver histórico de um arquivo específico
git log -p arquivo.txt
```

### 9.4 GitHub CLI - Comandos Úteis

```bash
# Listar repositórios
gh repo list

# Ver informações de um repositório
gh repo view

# Criar issue
gh issue create --title "Título" --body "Descrição"

# Listar issues
gh issue list

# Criar pull request
gh pr create --title "Título" --body "Descrição"

# Listar pull requests
gh pr list

# Ver pull request
gh pr view

# Fazer merge de PR
gh pr merge
```

---

## 10. Boas Práticas

### 10.1 Commits Frequentes e Pequenos

✅ **Bom:**
- Commits pequenos e focados
- Uma funcionalidade por commit
- Mensagens descritivas

❌ **Evitar:**
- Commits gigantes com muitas mudanças
- Commits genéricos como "fix" ou "update"
- Commits que misturam várias funcionalidades

### 10.2 Nunca Fazer Push de Informações Sensíveis

✅ **Sempre:**
- Use `.gitignore` para arquivos sensíveis
- Nunca commite senhas, tokens ou chaves
- Use variáveis de ambiente para configurações

### 10.3 Trabalhar com Branches

✅ **Recomendado:**
- `main` ou `master`: código em produção/estável
- `develop`: desenvolvimento principal (opcional para projetos pequenos)
- `feature/nome`: novas funcionalidades
- `fix/nome`: correções de bugs
- `hotfix/nome`: correções urgentes

**Estratégia para Trabalho Solo:**
- Mantenha `main` sempre estável e funcional
- Crie branches para features grandes, experimentos ou mudanças arriscadas
- Trabalhe direto em `main` apenas para mudanças pequenas e seguras
- Mesmo trabalhando sozinho, usar branches cria bons hábitos e organiza o trabalho

### 10.4 Antes de Fazer Push

✅ **Sempre:**
- Execute testes
- Verifique que o código compila
- Revise mudanças com `git diff`
- Faça pull antes de push

### 10.5 Mensagens de Commit

✅ **Boa mensagem:**
```
feat(auth): implementa autenticação OAuth2

Adiciona suporte para login via Google e GitHub.
Inclui validação de tokens e refresh automático.
```

❌ **Má mensagem:**
```
fix
```

ou

```
mudanças
```

---

## 11. Troubleshooting

### 11.1 Erro: "Repository not found"

**Causa:** Repositório não existe ou sem permissão.

**Solução:**
```bash
# Verificar se repositório existe
gh repo view usuario/repositorio

# Verificar autenticação
gh auth status

# Recriar remote se necessário
git remote remove origin
git remote add origin https://github.com/usuario/repositorio.git
```

### 11.2 Erro: "Permission denied"

**Causa:** Problema de autenticação ou permissões.

**Solução:**
```bash
# Reautenticar
gh auth login

# Verificar permissões do token
gh auth status
```

### 11.3 Conflitos de Merge

**Solução:**
```bash
# Ver arquivos em conflito
git status

# Resolver manualmente nos arquivos
# Depois:
git add arquivo-resolvido.txt
git commit
```

### 11.4 Commit Acidental em Branch Errada

**Solução:**
```bash
# 1. Criar branch a partir do commit atual
git branch nome-correto

# 2. Voltar branch anterior para antes do commit
git reset --hard HEAD~1

# 3. Mudar para branch correta
git checkout nome-correto
```

### 11.5 Perdeu Commits (Reset Acidental)

**Solução:**
```bash
# Ver histórico de referências (últimas 2 semanas)
git reflog

# Recuperar commit específico
git checkout <hash-do-commit>
git branch nome-da-branch  # criar branch para não perder novamente
```

---

## 12. Recursos Adicionais

### 12.1 Documentação Oficial

- Git: https://git-scm.com/doc
- GitHub CLI: https://cli.github.com/manual/
- GitHub Docs: https://docs.github.com/

### 12.2 Tutoriais Interativos

- Learn Git Branching: https://learngitbranching.js.org/
- GitHub Learning Lab: https://lab.github.com/

### 12.3 Referência Rápida

```bash
# Ver ajuda de qualquer comando
git help <comando>
git <comando> --help
gh <comando> --help
```

---

## Conclusão

Este guia cobre desde a instalação até o fluxo de trabalho diário com Git e GitHub CLI. Pratique os comandos regularmente para se familiarizar com o fluxo de trabalho.

**Lembre-se:**
- Faça commits frequentes e descritivos
- Sempre faça pull antes de push
- Use branches para trabalhar em features isoladas
- Nunca commite informações sensíveis
- Revise mudanças antes de commitar

Bom trabalho! 🚀

