# ServeRest API - Testes Automatizados

Suíte de testes automatizados para validação de funcionalidade e contrato da API pública **ServeRest**.

## API Testada

- **Nome:** ServeRest
- **URL:** https://serverest.dev
- **Documentação:** [ServeRest API Docs](https://serverest.dev/)

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pytest](https://img.shields.io/badge/Pytest-9.1.0-green)
![Requests](https://img.shields.io/badge/Requests-2.34.2-orange)
![pytest-cov](https://img.shields.io/badge/pytest--cov-7.1.0-yellow)
![Coverage](https://img.shields.io/badge/coverage-7.14.1-brightgreen)

## Estrutura do Projeto

```
api/               → Camada de clientes HTTP abstratos
fixtures/          → Data factory para geração de dados dinâmicos
schemas/           → Validação de contrato (JSON schemas)
tests/             → Casos de teste por endpoint
utils/             → Funções auxiliares (validação de schema)
conftest.py        → Fixtures globais pytest
pytest.ini         → Configuração pytest e cobertura
requirements.txt   → Dependências do projeto
```

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- Acesso à internet (API é pública)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/VictorJunior-creator/Desafio_Bootcamp_QA
   cd Python_Desafio_Bootcamp
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente virtual:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar os Testes

**Executar toda a suíte:**

```bash
pytest
```

**Executar com logs detalhados:**

```bash
pytest -v
```

**Executar testes de um endpoint específico:**

```bash
pytest -m usuarios      # Testes de /usuarios
pytest -m login         # Testes de /login
pytest -m produtos      # Testes de /produtos
```

**Executar um arquivo específico:**

```bash
pytest tests/test_usuarios.py
```

**Gerar relatório de cobertura:**

```bash
pytest --cov=api --cov=fixtures --cov=schemas --cov=utils --cov-report=html
```

## Cenários de Teste Implementados

### /usuarios

- Listar usuários com sucesso
- Cadastrar usuário com dados válidos
- Bloquear cadastro com e-mail duplicado
- Validar campos obrigatórios ausentes
- Buscar usuário por ID válido/inválido
- Atualizar usuário existente
- Excluir usuário do sistema

### /login

- Autenticar com credenciais válidas (geração de token)
- Bloquear autenticação com senha incorreta
- Bloquear autenticação com e-mail inexistente
- Validar rejeição com campos vazios

### /produtos

- Listar produtos com sucesso
- Cadastrar produto com token de admin
- Bloquear cadastro sem token de autenticação
- Bloquear cadastro com token inválido
- Buscar produto por ID válido/inválido
- Atualizar produto existente
- Excluir produto do sistema

## Melhorias Futuras

- Implementação de testes para endpoint `/carrinhos`
- Testes de carga e performance
- Integração com CI/CD (GitHub Actions)
- Relatórios em formato HTML com histórico
- Testes de segurança (validação de inputs maliciosos)
