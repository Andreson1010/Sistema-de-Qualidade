# Ambientes Virtuais Python - Guia Completo

## 📚 Índice
1. [O que são Ambientes Virtuais?](#1-o-que-são-ambientes-virtuais)
2. [Por que são Importantes?](#2-por-que-são-importantes)
3. [Vantagens e Desvantagens](#3-vantagens-e-desvantagens)
4. [Quando Usar Ambientes Virtuais](#4-quando-usar-ambientes-virtuais)
5. [Ferramentas para Criar Ambientes Virtuais](#5-ferramentas-para-criar-ambientes-virtuais)
6. [Passo a Passo: Criando e Usando Ambientes Virtuais](#6-passo-a-passo-criando-e-usando-ambientes-virtuais)
7. [Comandos Essenciais](#7-comandos-essenciais)
   - [7.6 Exportar Dependências](#76-exportar-dependências)
   - [7.7 Workflow de Desenvolvimento: Criando e Mantendo requirements.txt](#77-workflow-de-desenvolvimento-criando-e-mantendo-requirementstxt)
8. [Boas Práticas](#8-boas-práticas)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. O que são Ambientes Virtuais?

### 1.1 Definição

Um **ambiente virtual** é um diretório isolado que contém uma instalação Python específica e seus pacotes. É como ter uma "caixa separada" para cada projeto, onde você pode instalar versões específicas de bibliotecas sem afetar outros projetos ou o Python do sistema.

### 1.2 Analogia Simples

Imagine que você tem:
- **Projeto A**: Precisa da versão 2.0 da biblioteca `pandas`
- **Projeto B**: Precisa da versão 1.5 da biblioteca `pandas`

Sem ambientes virtuais, você só pode ter uma versão instalada globalmente, causando conflitos. Com ambientes virtuais, cada projeto tem sua própria "caixa" com a versão correta.

### 1.3 Estrutura de um Ambiente Virtual

Quando você cria um ambiente virtual, ele contém:

```
.venv/                    # Nome comum do ambiente virtual
├── bin/                  # (Linux/Mac) Scripts executáveis
│   ├── activate          # Script de ativação
│   ├── python            # Interpretador Python
│   └── pip               # Gerenciador de pacotes
├── Scripts/              # (Windows) Scripts executáveis
│   ├── Activate          # Script de ativação (PowerShell)
│   ├── activate.bat      # Script de ativação (CMD)
│   ├── python.exe        # Interpretador Python
│   └── pip.exe           # Gerenciador de pacotes
├── lib/                  # Bibliotecas Python instaladas
│   └── python3.12/
│       └── site-packages/ # Pacotes instalados
└── pyvenv.cfg            # Configuração do ambiente
```

---

## 2. Por que são Importantes?

### 2.1 Isolamento de Dependências

**Problema sem ambiente virtual:**
- Você instala `pandas==2.0.0` para o Projeto A
- Depois precisa trabalhar no Projeto B que requer `pandas==1.5.0`
- Ao atualizar para 1.5.0, o Projeto A para de funcionar! ❌

**Solução com ambiente virtual:**
- Projeto A tem seu próprio ambiente com `pandas==2.0.0`
- Projeto B tem seu próprio ambiente com `pandas==1.5.0`
- Ambos funcionam perfeitamente! ✅

### 2.2 Controle de Versões

Cada projeto pode usar versões específicas de:
- Python (3.10, 3.11, 3.12, etc.)
- Bibliotecas (pandas 1.5, 2.0, 2.1, etc.)
- Ferramentas (pip, setuptools, etc.)

### 2.3 Reproducibilidade

Com ambientes virtuais, você pode:
- Documentar exatamente quais pacotes e versões cada projeto usa
- Compartilhar o projeto com outros desenvolvedores
- Garantir que todos tenham o mesmo ambiente
- Evitar o famoso "funciona na minha máquina" 😅

### 2.4 Organização

- Cada projeto tem suas próprias dependências
- Fácil de identificar o que cada projeto precisa
- Fácil de remover quando o projeto não é mais necessário

---

## 3. Vantagens e Desvantagens

### 3.1 ✅ Vantagens

1. **Isolamento Completo**
   - Dependências de um projeto não afetam outros
   - Evita conflitos de versões

2. **Reproducibilidade**
   - Mesmo ambiente em diferentes máquinas
   - Facilita colaboração em equipe

3. **Segurança**
   - Não modifica o Python do sistema
   - Pode testar pacotes sem risco

4. **Organização**
   - Cada projeto é autocontido
   - Fácil de gerenciar múltiplos projetos

5. **Facilidade de Limpeza**
   - Remover um projeto = deletar uma pasta
   - Não deixa "lixo" no sistema

### 3.2 ❌ Desvantagens

1. **Espaço em Disco**
   - Cada ambiente virtual ocupa espaço (geralmente 50-200 MB)
   - Múltiplos projetos = múltiplos ambientes

2. **Curva de Aprendizado**
   - Requer conhecimento de comandos básicos
   - Pode confundir iniciantes

3. **Gerenciamento**
   - Precisa lembrar de ativar antes de trabalhar
   - Múltiplos ambientes podem ser difíceis de gerenciar

4. **Tempo de Setup**
   - Precisa criar e configurar para cada projeto
   - Instalar dependências leva tempo

**Nota:** As vantagens superam muito as desvantagens! Os benefícios de isolamento e organização fazem valer a pena.

---

## 4. Quando Usar Ambientes Virtuais?

### 4.1 ✅ Sempre Use Quando:

1. **Desenvolvendo Projetos Python**
   - Qualquer projeto que use bibliotecas externas
   - Projetos que serão compartilhados
   - Projetos que precisam de versões específicas

2. **Trabalhando em Múltiplos Projetos**
   - Cada projeto com suas próprias dependências
   - Evita conflitos entre projetos

3. **Desenvolvimento em Equipe**
   - Garante que todos tenham o mesmo ambiente
   - Facilita onboarding de novos desenvolvedores

4. **Testando Bibliotecas**
   - Quer testar uma nova versão sem afetar outros projetos
   - Experimentar pacotes sem risco

5. **Deploy e Produção**
   - Garante que o ambiente de produção seja reproduzível
   - Facilita containerização (Docker)

### 4.2 ⚠️ Pode Não Ser Necessário Quando:

1. **Scripts Simples e Únicos**
   - Scripts que não usam bibliotecas externas
   - Scripts descartáveis

2. **Ambientes Já Isolados**
   - Containers Docker (já isolados)
   - Ambientes de CI/CD (criados do zero)

**Regra de Ouro:** Quando em dúvida, **USE um ambiente virtual**. É melhor ter e não precisar do que precisar e não ter!

---

## 5. Ferramentas para Criar Ambientes Virtuais

### 5.1 Ferramentas Disponíveis

| Ferramenta | Comando | Velocidade | Recomendado Para |
|------------|---------|------------|------------------|
| **venv** (built-in) | `python -m venv` | ⭐⭐⭐ | Uso geral, padrão |
| **uv** | `uv venv` | ⭐⭐⭐⭐⭐ | Projetos modernos, muito rápido |
| **virtualenv** | `virtualenv` | ⭐⭐⭐ | Projetos legados |
| **conda** | `conda create` | ⭐⭐⭐⭐ | Ciência de dados, pacotes complexos |
| **poetry** | `poetry env` | ⭐⭐⭐⭐ | Gerenciamento completo de projetos |

### 5.2 Recomendação para Este Projeto

Este projeto utiliza **uv** por ser:
- ⚡ Extremamente rápido
- 🎯 Moderno e eficiente
- 📦 Gerencia dependências de forma otimizada
- 🔧 Compatível com pip e requirements.txt

---

## 6. Passo a Passo: Criando e Usando Ambientes Virtuais

### 6.1 Pré-requisitos

Antes de começar, você precisa ter:
- ✅ Python 3.12 instalado
- ✅ uv instalado (ou outra ferramenta de sua escolha)

**Verificar instalação:**
```bash
python --version    # Deve mostrar Python 3.12.x
uv --version        # Deve mostrar a versão do uv
```

### 6.2 Passo 1: Navegar até o Diretório do Projeto

```bash
cd caminho/para/seu/projeto
```

**Exemplo:**
```bash
cd C:\Users\Francisco\Projetos\proj_6
```

### 6.3 Passo 2: Criar o Ambiente Virtual

**Com uv (recomendado para este projeto):**
```bash
uv venv
```

**Com venv (alternativa padrão):**
```bash
python -m venv .venv
```

**O que acontece:**
- Cria uma pasta `.venv` no diretório atual
- Instala uma cópia isolada do Python
- Configura o ambiente para instalar pacotes localmente

**Nomenclatura:**
- `.venv` é o nome mais comum (ponto no início = pasta oculta)
- Você pode usar outro nome: `uv venv meu_ambiente`

### 6.4 Passo 3: Ativar o Ambiente Virtual

**⚠️ IMPORTANTE:** Você DEVE ativar o ambiente antes de instalar pacotes ou executar scripts!

#### Windows PowerShell:
```powershell
.venv\Scripts\Activate
```

#### Windows CMD:
```cmd
.venv\Scripts\activate.bat
```

#### Linux/Mac (bash/zsh):
```bash
source .venv/bin/activate
```

**Como saber se está ativado?**
Quando ativado, você verá `(.venv)` no início do prompt:

```bash
# Antes da ativação:
C:\Users\Francisco\Projetos\proj_6>

# Depois da ativação:
(.venv) C:\Users\Francisco\Projetos\proj_6>
```

### 6.5 Passo 4: Instalar Dependências

Com o ambiente ativado, instale os pacotes necessários:

**Com uv:**
```bash
uv pip install -r requirements.txt
```

**Com pip tradicional:**
```bash
pip install -r requirements.txt
```

**Instalar pacote individual:**
```bash
uv pip install nome-do-pacote
# ou
pip install nome-do-pacote
```

### 6.6 Passo 5: Verificar Instalação

```bash
# Listar pacotes instalados
uv pip list
# ou
pip list

# Verificar versão de um pacote específico
uv pip show nome-do-pacote
# ou
pip show nome-do-pacote
```

### 6.7 Passo 6: Trabalhar no Projeto

Agora você pode executar seus scripts Python normalmente:

```bash
python treinamento/aivk_treina_modelo.py
python appaivk.py
```

**Lembre-se:** O ambiente deve estar **sempre ativado** enquanto você trabalha no projeto!

### 6.7 Passo 7: Desativar o Ambiente (quando terminar)

Quando terminar de trabalhar, você pode desativar:

```bash
deactivate
```

O prompt voltará ao normal (sem o `(.venv)`).

**Nota:** Desativar não remove o ambiente, apenas "sai" dele. Você pode ativar novamente depois.

---

## 7. Comandos Essenciais

### 7.1 Criação e Gerenciamento

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `uv venv` | Cria ambiente virtual | `uv venv` |
| `uv venv nome` | Cria com nome específico | `uv venv meu_env` |
| `uv venv --python 3.11` | Especifica versão Python | `uv venv --python 3.11` |

### 7.2 Ativação e Desativação

| Comando | Sistema | Descrição |
|---------|---------|-----------|
| `.venv\Scripts\Activate` | Windows PowerShell | Ativa o ambiente |
| `.venv\Scripts\activate.bat` | Windows CMD | Ativa o ambiente |
| `source .venv/bin/activate` | Linux/Mac | Ativa o ambiente |
| `deactivate` | Todos | Desativa o ambiente |

### 7.3 Instalação de Pacotes

| Comando | Descrição |
|---------|-----------|
| `uv pip install pacote` | Instala um pacote |
| `uv pip install pacote==1.0.0` | Instala versão específica |
| `uv pip install -r requirements.txt` | Instala de arquivo |
| `uv pip install --upgrade pacote` | Atualiza pacote |

### 7.4 Informações e Listagem

| Comando | Descrição |
|---------|-----------|
| `uv pip list` | Lista pacotes instalados |
| `uv pip show pacote` | Mostra info do pacote |
| `uv pip freeze` | Lista com versões (para requirements.txt) |
| `python --version` | Versão do Python no ambiente |

### 7.5 Remoção

| Comando | Descrição |
|---------|-----------|
| `uv pip uninstall pacote` | Remove um pacote |
| `rm -rf .venv` (Linux/Mac) | Remove ambiente virtual |
| `Remove-Item -Recurse .venv` (PowerShell) | Remove ambiente virtual |

### 7.6 Exportar Dependências

**⚠️ IMPORTANTE: Diferença entre os comandos**

#### Opção 1: `uv pip freeze` (Coletar do ambiente atual)
```bash
uv pip freeze > requirements.txt
```

**O que faz:**
- ✅ Captura **TODAS** as dependências atualmente instaladas no ambiente virtual ativo
- ✅ Inclui versões exatas de todos os pacotes
- ✅ Útil para "congelar" o estado atual do ambiente

**Quando usar:**
- Quando você já instalou tudo e quer documentar o estado atual
- Para criar um snapshot do ambiente

**Limitação:**
- Pode incluir dependências não diretamente usadas pelo projeto
- Não resolve conflitos de versões

#### Opção 2: `uv pip compile` (Compilar e resolver dependências)
```bash
uv pip compile requirements.in -o requirements.txt
```

**O que faz:**
- ✅ Lê um arquivo de entrada (`requirements.in` ou `pyproject.toml`)
- ✅ Resolve todas as dependências transitivas
- ✅ Gera um `requirements.txt` com versões fixas e compatíveis
- ✅ Garante que todas as dependências necessárias sejam incluídas

**Quando usar:**
- Quando você tem um arquivo `requirements.in` com apenas as dependências principais
- Para garantir que todas as dependências transitivas sejam incluídas
- Para resolver conflitos de versões automaticamente

**Exemplo de workflow:**
```bash
# 1. Criar requirements.in com dependências principais
echo "streamlit==1.43.0" > requirements.in
echo "scikit-learn==1.6.1" >> requirements.in
echo "pandas==2.2.3" >> requirements.in

# 2. Compilar para gerar requirements.txt completo
uv pip compile requirements.in -o requirements.txt
```

#### Qual usar?

| Situação | Comando Recomendado |
|----------|---------------------|
| Já instalei tudo e quero documentar | `uv pip freeze > requirements.txt` |
| Tenho dependências principais e quero resolver todas | `uv pip compile requirements.in` |
| Quero atualizar requirements.txt do ambiente atual | `uv pip freeze > requirements.txt` |
| Quero garantir compatibilidade de versões | `uv pip compile requirements.in` |

**Para este projeto:**
Como você já tem um `requirements.txt` completo, use:
```bash
uv pip freeze > requirements.txt
```
Isso atualizará o arquivo com as versões exatas do ambiente atual.

### 7.7 Workflow de Desenvolvimento: Criando e Mantendo requirements.txt

**Pergunta comum:** "O `requirements.txt` é criado manualmente durante o desenvolvimento?"

**Resposta:** Não é totalmente manual, mas também não é 100% automático. É um processo **semi-automático** que combina instalação de pacotes e atualização periódica do arquivo.

#### Abordagens Comuns

##### Abordagem 1: Semi-Automática (Mais Comum) ⭐ Recomendada

**Workflow típico:**

1. **Durante o desenvolvimento:**
   ```bash
   # Você instala pacotes conforme precisa
   uv pip install streamlit
   uv pip install pandas
   uv pip install scikit-learn
   ```

2. **Periodicamente (antes de commits importantes):**
   ```bash
   # "Congela" o estado atual do ambiente
   uv pip freeze > requirements.txt
   ```

3. **Quando adiciona nova dependência:**
   ```bash
   # Instala o novo pacote
   uv pip install novo-pacote
   
   # Atualiza o requirements.txt
   uv pip freeze > requirements.txt
   ```

**Vantagens:**
- ✅ Simples e direto
- ✅ Captura tudo automaticamente
- ✅ Não precisa lembrar de adicionar manualmente

**Desvantagens:**
- ⚠️ Pode incluir dependências indiretas (sub-dependências)
- ⚠️ Pode ficar grande

##### Abordagem 2: Manual Inicial + Freeze Periódico

**Workflow:**

1. **Início do projeto (manual):**
   ```txt
   # requirements.txt (criado manualmente)
   streamlit==1.43.0
   pandas==2.2.3
   scikit-learn==1.6.1
   numpy==2.1.3
   ```

2. **Instalação:**
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Quando adiciona dependência:**
   - **Opção A:** Adiciona manualmente no `requirements.txt` e depois instala
   - **Opção B:** Instala primeiro e depois faz `uv pip freeze`

##### Abordagem 3: requirements.in + compile (Mais Profissional)

**Workflow:**

1. **Criar `requirements.in` (manual, apenas dependências principais):**
   ```txt
   # requirements.in
   streamlit==1.43.0
   pandas==2.2.3
   scikit-learn==1.6.1
   numpy==2.1.3
   ```

2. **Compilar para gerar `requirements.txt` completo:**
   ```bash
   uv pip compile requirements.in -o requirements.txt
   ```

3. **Instalar:**
   ```bash
   uv pip install -r requirements.txt
   ```

**Vantagens:**
- ✅ Controle sobre dependências principais
- ✅ Resolve dependências transitivas automaticamente
- ✅ Garante compatibilidade

#### Workflow Recomendado para Este Projeto

**Sugestão: Abordagem Híbrida**

1. **Início do projeto:**
   - Criar `requirements.txt` manualmente com as dependências principais que você sabe que vai usar

2. **Durante o desenvolvimento:**
   ```bash
   # Quando precisa de um novo pacote
   uv pip install nome-do-pacote
   
   # Depois de instalar, atualiza o requirements.txt
   uv pip freeze > requirements.txt
   ```

3. **Antes de commits importantes:**
   ```bash
   # Sempre atualiza antes de commitar
   uv pip freeze > requirements.txt
   git add requirements.txt
   git commit -m "Atualiza dependências"
   ```

4. **Quando alguém clona o projeto:**
   ```bash
   # Instala tudo de uma vez
   uv pip install -r requirements.txt
   ```

#### Exemplo Prático do Dia a Dia

```bash
# Dia 1: Início do projeto
# Cria requirements.txt manualmente com:
# streamlit, pandas, scikit-learn, numpy

# Dia 2: Precisa de uma nova biblioteca
uv pip install matplotlib
uv pip freeze > requirements.txt  # Atualiza

# Dia 3: Precisa de outra
uv pip install seaborn
uv pip freeze > requirements.txt  # Atualiza novamente

# Dia 4: Antes de fazer commit
uv pip freeze > requirements.txt  # Garante que está atualizado
git add requirements.txt
git commit -m "Adiciona matplotlib e seaborn"
```

#### Dicas Importantes

1. **Sempre atualize antes de commitar:**
   ```bash
   uv pip freeze > requirements.txt
   ```

2. **Revise o `requirements.txt` periodicamente:**
   - Remova pacotes que não usa mais
   - Mantenha apenas o necessário

3. **Use comentários (como no seu arquivo atual):**
   ```txt
   streamlit==1.43.0  # Framework web
   pandas==2.2.3     # Manipulação de dados
   ```

4. **Versionamento:**
   - Use versões específicas (`==`) para produção
   - Use versões flexíveis (`>=`) apenas em desenvolvimento

#### Resumo

- ❌ **NÃO é 100% manual:** Você instala pacotes normalmente e usa `uv pip freeze` para atualizar o arquivo
- ❌ **NÃO é 100% automático:** Você decide quando atualizar e pode revisar/limpar o arquivo
- ✅ **Prática recomendada:** Atualizar o `requirements.txt` sempre que adicionar uma nova dependência e antes de commits importantes

---

## 8. Boas Práticas

### 8.1 ✅ Faça Isso:

1. **Sempre use ambiente virtual para projetos**
   - Crie um ambiente para cada projeto
   - Ative antes de trabalhar

2. **Documente as dependências**
   - Mantenha `requirements.txt` atualizado
   - Use `uv pip freeze > requirements.txt` regularmente

3. **Nomeie claramente**
   - Use `.venv` como padrão
   - Ou use nome descritivo: `projeto_ml_env`

4. **Adicione ao .gitignore**
   ```
   .venv/
   venv/
   env/
   *.pyc
   __pycache__/
   ```

5. **Ative antes de instalar**
   - Sempre verifique se está ativado
   - Confira o `(.venv)` no prompt

6. **Use versões específicas**
   ```txt
   # requirements.txt
   pandas==2.2.3
   numpy==2.1.3
   ```

### 8.2 ❌ Evite Isso:

1. **Não instale globalmente**
   - Evite `pip install` sem ambiente virtual
   - Pode causar conflitos

2. **Não commite o ambiente**
   - Não adicione `.venv/` ao Git
   - É grande e específico da máquina

3. **Não use o mesmo ambiente para múltiplos projetos**
   - Cada projeto = um ambiente
   - Evita conflitos de versões

4. **Não esqueça de ativar**
   - Sempre verifique o prompt
   - Pacotes instalados sem ativar vão para o sistema global

---

## 9. Troubleshooting

### 9.1 Problema: "Comando não encontrado" ao ativar

**Sintoma:**
```bash
.venv\Scripts\Activate: comando não encontrado
```

**Soluções:**
- Verifique se o ambiente foi criado: `ls .venv` (Linux/Mac) ou `dir .venv` (Windows)
- Use o caminho completo: `.\venv\Scripts\Activate.ps1` (PowerShell)
- Verifique se está no diretório correto

### 9.2 Problema: Pacotes instalados no lugar errado

**Sintoma:**
- Instalou pacote mas não encontra ao importar
- Pacote aparece no sistema global, não no ambiente

**Solução:**
- Verifique se o ambiente está ativado (deve ver `(.venv)`)
- Desative e reative o ambiente
- Reinstale os pacotes com ambiente ativado

### 9.3 Problema: Ambiente muito grande

**Sintoma:**
- Ambiente virtual ocupa muito espaço

**Soluções:**
- Remova pacotes não utilizados: `uv pip uninstall pacote`
- Recrie o ambiente: delete `.venv` e crie novamente
- Use `uv pip install` que é mais eficiente

### 9.4 Problema: Versão errada do Python

**Sintoma:**
- Ambiente criado com Python 3.10 mas precisa de 3.12

**Solução:**
```bash
# Remover ambiente antigo
rm -rf .venv  # Linux/Mac
Remove-Item -Recurse .venv  # PowerShell

# Criar com versão específica
uv venv --python 3.12
```

### 9.5 Problema: Não consegue desativar

**Sintoma:**
- Comando `deactivate` não funciona

**Solução:**
- Feche e abra o terminal
- Ou simplesmente abra um novo terminal

### 9.6 Problema: Conflitos de dependências

**Sintoma:**
- Erro ao instalar: "Cannot install X because Y requires Z"

**Soluções:**
- Atualize as versões no `requirements.txt`
- Use `uv pip install --upgrade pacote`
- Considere usar `uv pip sync` para resolver dependências

---

## 10. Resumo Rápido

### Checklist para Iniciar um Projeto:

- [ ] 1. Navegar até o diretório do projeto
- [ ] 2. Criar ambiente: `uv venv`
- [ ] 3. Ativar ambiente: `.venv\Scripts\Activate` (Windows) ou `source .venv/bin/activate` (Linux/Mac)
- [ ] 4. Verificar ativação: deve aparecer `(.venv)` no prompt
- [ ] 5. Instalar dependências: `uv pip install -r requirements.txt`
- [ ] 6. Trabalhar no projeto normalmente
- [ ] 7. Desativar quando terminar: `deactivate`

### Comandos Mais Usados:

```bash
# Criar
uv venv

# Ativar (Windows PowerShell)
.venv\Scripts\Activate

# Ativar (Linux/Mac)
source .venv/bin/activate

# Instalar dependências
uv pip install -r requirements.txt

# Listar pacotes
uv pip list

# Desativar
deactivate
```

---

## 11. Recursos Adicionais

- **Documentação oficial do uv**: https://github.com/astral-sh/uv
- **Documentação oficial do venv**: https://docs.python.org/3/library/venv.html
- **Python Packaging Guide**: https://packaging.python.org/

---

**Última atualização:** Janeiro 2025  
**Versão:** 1.0  
**Projeto:** Projeto 6 - AIVK

