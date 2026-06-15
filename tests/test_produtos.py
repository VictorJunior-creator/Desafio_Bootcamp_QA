"""
Testes automatizados para o endpoint /produtos da API ServeRest.

Cenários cobertos (6/6):
  1. Listar produtos
  2. Cadastrar produto com token de administrador
  3. Bloquear cadastro sem token
  4. Buscar produto por ID
  5. Atualizar produto
  6. Excluir produto
"""
import pytest

from fixtures.data_factory import gerar_produto
from schemas.produtos_schema import (
    SCHEMA_LISTAR_PRODUTOS,
    SCHEMA_PRODUTO,
    SCHEMA_CADASTRO_SUCESSO,
)
from utils.helpers import validar_schema


@pytest.mark.produtos
class TestListarProdutos:
    def test_listar_produtos_retorna_200_e_estrutura_correta(self, produtos_api):
        """GET /produtos deve retornar 200 e conter 'quantidade' e 'produtos'."""
        response = produtos_api.listar()

        assert response.status_code == 200
        body = response.json()
        validar_schema(body, SCHEMA_LISTAR_PRODUTOS)
        assert isinstance(body["quantidade"], int)
        assert isinstance(body["produtos"], list)


@pytest.mark.produtos
class TestCadastrarProduto:
    def test_cadastrar_produto_com_token_admin_retorna_201(
        self, produtos_api, token_admin
    ):
        """POST /produtos com token admin deve retornar 201 e o _id do produto."""
        produtos_api.set_auth_token(token_admin)
        payload = gerar_produto()

        response = produtos_api.cadastrar(payload)

        assert response.status_code == 201
        body = response.json()
        validar_schema(body, SCHEMA_CADASTRO_SUCESSO)
        assert body["message"] == "Cadastro realizado com sucesso"
        assert isinstance(body["_id"], str)
        assert len(body["_id"]) > 0

        produtos_api.excluir(body["_id"])
        produtos_api.clear_auth_token()

    def test_cadastrar_produto_sem_token_retorna_401(self, produtos_api):
        """POST /produtos sem Authorization header deve retornar 401."""
        produtos_api.clear_auth_token()
        payload = gerar_produto()

        response = produtos_api.cadastrar(payload)

        assert response.status_code == 401
        body = response.json()
        assert "message" in body
        assert body["message"] == "Token de acesso ausente, inválido, expirado ou usuário do token não existe mais"

    def test_cadastrar_produto_com_token_invalido_retorna_401(self, produtos_api):
        """POST /produtos com token inválido/malformado deve retornar 401."""
        produtos_api.set_auth_token("Bearer token_invalido_xyz")
        payload = gerar_produto()

        response = produtos_api.cadastrar(payload)

        assert response.status_code == 401
        body = response.json()
        assert "message" in body
        produtos_api.clear_auth_token()


@pytest.mark.produtos
class TestBuscarProduto:
    def test_buscar_produto_por_id_valido_retorna_200(
        self, produtos_api, produto_cadastrado
    ):
        """GET /produtos/{id} com ID existente deve retornar 200 e os dados do produto."""
        produto_id = produto_cadastrado["id"]
        response = produtos_api.buscar_por_id(produto_id)

        assert response.status_code == 200
        body = response.json()
        validar_schema(body, SCHEMA_PRODUTO)
        assert body["_id"] == produto_id
        assert body["nome"] == produto_cadastrado["nome"]
        assert body["preco"] == produto_cadastrado["preco"]

    def test_buscar_produto_com_id_malformado_retorna_400(self, produtos_api):
        """GET /produtos/{id} com ID de formato inválido deve retornar 400.

        A API valida o formato antes de consultar a base — IDs devem ter
        exatamente 16 caracteres alfanuméricos. A chave de erro retornada
        é "id", não "message" como nos demais erros da API (ver BUG-002).
        """
        response = produtos_api.buscar_por_id("id_invalido_xyz")

        assert response.status_code == 400
        body = response.json()
        assert "id" in body, f"Campo 'id' ausente na resposta: {body}"
        assert body["id"] == "id deve ter exatamente 16 caracteres alfanuméricos"

    def test_buscar_produto_com_id_inexistente_retorna_400(self, produtos_api):
        """GET /produtos/{id} com ID no formato correto mas inexistente na base deve retornar 400."""
        response = produtos_api.buscar_por_id("0000000000000000")

        assert response.status_code == 400
        body = response.json()
        assert "message" in body, f"Campo 'message' ausente na resposta: {body}"
        assert body["message"] == "Produto não encontrado"


@pytest.mark.produtos
class TestAtualizarProduto:
    def test_atualizar_produto_com_token_admin_retorna_200(
        self, produtos_api, produto_cadastrado
    ):
        """PUT /produtos/{id} com token admin deve retornar 200.

        Reutiliza o token já obtido pela fixture 'produto_cadastrado',
        evitando a criação de um segundo usuário administrador desnecessário.
        """
        produto_id = produto_cadastrado["id"]
        produtos_api.set_auth_token(produto_cadastrado["token"])
        payload_atualizado = gerar_produto()

        response = produtos_api.atualizar(produto_id, payload_atualizado)

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Registro alterado com sucesso"
        produtos_api.clear_auth_token()


@pytest.mark.produtos
class TestExcluirProduto:
    def test_excluir_produto_com_token_admin_retorna_200(
        self, produtos_api, token_admin
    ):
        """DELETE /produtos/{id} de um produto existente deve retornar 200."""
        produtos_api.set_auth_token(token_admin)
        payload = gerar_produto()
        criado = produtos_api.cadastrar(payload)
        assert criado.status_code == 201
        produto_id = criado.json()["_id"]

        response = produtos_api.excluir(produto_id)

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Registro excluído com sucesso"
        produtos_api.clear_auth_token()

    def test_excluir_produto_inexistente_retorna_200_sem_exclusao(
        self, produtos_api, token_admin
    ):
        """DELETE /produtos/{id} de ID inexistente deve retornar 200 — comportamento idempotente.

        A ServeRest exige token mesmo para IDs inexistentes em /produtos,
        diferente de /usuarios que não exige (ver BUG-001).
        """
        produtos_api.set_auth_token(token_admin)
        response = produtos_api.excluir("0000000000000000")

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Nenhum registro excluído"
        produtos_api.clear_auth_token()
