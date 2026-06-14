Plano de Testes

1. Objetivo da suíte

O objetivo é criar testes automatizados para validar o funcionamento da API da ServeRest.

2. Estratégia

2.1 Os testes serão executados na camada de API.

2.2 A linguagem de programação adotada é o Python, utilizando o framework Pytest para a estruturação e execução dos cenários.

2.3 Utilizarei a biblioteca requests para realizar as chamadas HTTP e a biblioteca nativa uuid para a geração de massa de dados dinâmica e e-mails únicos.

2.4 A gestão de dependências e a isolação do projeto serão feitas através de um ambiente virtual (.venv).

3. Escopo

3.1 Coberto: O escopo desta suíte de testes contempla a validação funcional das rotas de Usuários, Login e Produtos da API ServeRest.


3.2 Fora do Escopo: O endpoint de Carrinhos ficará de fora desta etapa inicial de automação. Testes de carga, performance ou segurança também não compõem o escopo atual.

4. Cenários a Implementar

4.1 Usuários: Listar usuários, cadastrar com sucesso, cadastrar com email duplicado, cadastrar com campos faltando, buscar por ID, atualizar e excluir.


4.2 Login: Validar autenticação com credenciais corretas, tentar login com senha incorreta, tentar login com email inexistente e testar o envio de requisição com campos vazios.


4.3 Produtos: Listar produtos, cadastrar possuindo token de administrador, tentar cadastrar sem possuir token de administrador, buscar produto por ID, atualizar e excluir.

5. Critérios de Qualidade 

5.1 Nomenclatura: Os testes devem possuir nomes claros e descritivos em relação ao cenário testado.

5.2 Independência: Cada teste deve ser capaz de rodar sozinho ou em paralelo de forma totalmente independente, sem depender do estado deixado por outro teste.

5.3 Validações: Todos os testes devem validar o status code retornado e a estrutura/mensagem do corpo da resposta (JSON).

5.4 Massa de Dados: É obrigatório o uso de geração de emails dinâmicos para a criação de usuários, evitando conflitos na base de dados da API.

5.5 Documentação: O projeto deve conter um arquivo README na raiz explicando o passo a passo para a execução da suíte.