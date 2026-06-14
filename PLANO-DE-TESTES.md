#  Plano de Testes

##  1. Objetivo da Suíte
O objetivo principal deste projeto é implementar testes automatizados robustos para validar o funcionamento correto, a integridade e as regras de negócio da API pública **ServeRest**.

---

##  2. Estratégia e Arquitetura

Para garantir uma suíte modular e de rápida execução, a estratégia técnica foi definida com as seguintes tecnologias:

* **Camada de Teste** Automação focada exclusivamente na camada de API.
* **Linguagem:** Python 3
* **Framework Principal:** Pytest (estruturação, fixtures e execução dos cenários).
* **Comunicação HTTP:** Biblioteca `requests` para requisições e asserções.
* **Massa de Dados:** Biblioteca nativa `uuid` para geração de dados dinâmicos e e-mails únicos.
* **Isolamento:** Gerenciamento de dependências via ambiente virtual nativo (`.venv`).

---

##  3. Escopo do Projeto

| Seção | Descrição | Endpoints / Tipos de Teste |
| :--- | :--- | :--- |
| **Dentro do Escopo** | Validação funcional e de contrato das rotas principais. | ` /usuarios`<br>` /login`<br>` /produtos` |
| **Fora do Escopo** | Fluxos complexos de e-commerce e testes não-funcionais. | ` /carrinhos`<br>` Carga e Performance`<br>` Segurança (Pentest)` |

---

##  4. Cenários de Teste a Implementar

###  Rota: Usuários (`/usuarios`)
- [ ] Listar todos os usuários cadastrados.
- [ ] Cadastrar novo usuário com sucesso.
- [ ] Impedir cadastro com e-mail duplicado.
- [ ] Validar payload de campos obrigatórios ausentes.
- [ ] Buscar usuário específico por ID.
- [ ] Atualizar dados de um usuário existente.
- [ ] Excluir usuário do sistema.

###  Rota: Login (`/login`)
- [ ] Autenticar com credenciais válidas (geração de token).
- [ ] Bloquear autenticação com senha incorreta.
- [ ] Bloquear autenticação com e-mail inexistente.
- [ ] Validar envio de requisição com campos vazios.

###  Rota: Produtos (`/produtos`)
- [ ] Listar todos os produtos cadastrados.
- [ ] Cadastrar produto válido (requer token de administrador).
- [ ] Bloquear cadastro de produto sem token de administrador.
- [ ] Buscar produto específico por ID.
- [ ] Atualizar dados de um produto.
- [ ] Excluir produto do sistema.

---

##  5. Critérios de Qualidade

Para que um teste seja aceito na suíte oficial, ele deve cumprir os cinco pilares abaixo:

1. **Nomenclatura Semântica:** Os nomes das funções de teste devem ser autoexplicativos (ex: `test_cadastro_usuario_com_sucesso`).
2. **Independência Total:** Nenhum teste pode depender do resultado ou estado deixado por outro. Devem rodar de forma isolada e em paralelo.
3. **Asserções:** Os cenários devem validar o *Status Code* e o Contrato *(JSON Schema)*.
4. **Massa Dinâmica:** Proibido o uso de e-mails fixos (*hardcoded*) para fluxos de criação, evitando conflitos na base.
5. **Documentação Viva:** O projeto deve conter um `README.md` detalhando os pré-requisitos, instalação e comandos de execução.
