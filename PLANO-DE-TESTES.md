# Plano de Testes

## OBJETIVO

Validar automaticamente os principais fluxos da API pública ServeRest, garantindo a operação correta dos endpoints `/usuarios`, `/login` e `/produtos`. O foco é verificar funcionalidade, contrato de resposta e comportamentos de autenticação, tanto em cenários positivos quanto negativos.

## ESTRATÉGIA

A estratégia de testes identificada no projeto é baseada em uma suíte funcional de API com separação clara entre camada de clientes HTTP, massa de dados e casos de teste.

- Testes funcionais de API usando `pytest` e `requests`
- Testes positivos para fluxos autorizados e válidos
- Testes negativos para erros de validação, autenticação e dados incorretos
- Testes de contrato simplificados via validação de campos esperados em resposta
- Testes de autenticação com token Bearer para operações em `/produtos`
- Uso de fixtures para setup/teardown automático e isolamento de estado

## ESCOPO

Endpoints e funcionalidades cobertas pelos testes existentes:

- `/usuarios`
  - Listar usuários
  - Cadastrar usuário válido
  - Cadastrar usuário com e-mail duplicado
  - Validar campos obrigatórios ausentes
  - Buscar usuário por ID
  - Atualizar usuário
  - Excluir usuário

- `/login`
  - Autenticação com credenciais válidas
  - Autenticação com senha incorreta
  - Autenticação com e-mail inexistente
  - Requisição com campos vazios

- `/produtos`
  - Listar produtos
  - Cadastrar produto com token admin
  - Cadastrar produto sem token
  - Cadastrar produto com token inválido
  - Buscar produto por ID válido
  - Buscar produto por ID malformado
  - Buscar produto por ID inexistente
  - Atualizar produto com token admin
  - Excluir produto existente
  - Excluir produto inexistente

## ITENS FORA DO ESCOPO

Funcionalidades e endpoints não cobertos pelo projeto atual:

- `/carrinhos`
- Testes de carga e performance
- Testes de segurança
- Testes de UI ou front-end
- Testes de integração além dos endpoints listados

## CENÁRIOS DE TESTE A IMPLEMENTAR

### `/usuarios`

- Listar usuários retorna 200 e estrutura correta
- Cadastrar usuário válido retorna 201
- Cadastrar usuário com e-mail duplicado retorna 400
- Cadastrar usuário sem nome retorna 400
- Cadastrar usuário sem email retorna 400
- Cadastrar usuário sem password retorna 400
- Buscar usuário por ID válido retorna 200
- Buscar usuário por ID malformado retorna 400
- Buscar usuário por ID inexistente retorna 400
- Atualizar usuário existente retorna 200
- Excluir usuário existente retorna 200
- Excluir usuário inexistente retorna 200 sem exclusão

### `/login`

- Autenticar com credenciais corretas retorna 200 e token
- Autenticar com senha incorreta retorna 401
- Autenticar com e-mail inexistente retorna 401
- Autenticar com campos vazios retorna 400

### `/produtos`

- Listar produtos retorna 200 e estrutura correta
- Cadastrar produto com token admin retorna 201
- Cadastrar produto sem token retorna 401
- Cadastrar produto com token inválido retorna 401
- Buscar produto por ID válido retorna 200
- Buscar produto com ID malformado retorna 400
- Buscar produto com ID inexistente retorna 400
- Atualizar produto com token admin retorna 200
- Excluir produto existente retorna 200
- Excluir produto inexistente retorna 200 sem exclusão

## CRITÉRIOS DE QUALIDADE

Os testes devem seguir os critérios identificados no projeto:

1. **Clareza:** nomes de teste claros e descritivos.
2. **Isolamento:** uso de fixtures com escopo `function` para evitar dependência entre testes.
3. **Dados dinâmicos:** geração de dados com UUID para evitar conflitos e duplicidade.
4. **Validação de contrato:** verificar campos esperados nas respostas usando schemas simples.
5. **Validação de status:** checar status codes esperados para cada cenário.
6. **Reutilização de componentes:** usar clients HTTP e fixtures compartilhadas para reduzir duplicação.
7. **Automação de setup/teardown:** criação e exclusão de dados via fixtures para manter ambiente limpo.
8. **Marcação de testes:** uso de `pytest.mark.usuarios`, `pytest.mark.login` e `pytest.mark.produtos`.
