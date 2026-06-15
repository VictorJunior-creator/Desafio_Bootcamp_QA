"""
Testes automatizados para o endpoint /usuarios da API ServeRest.

Cenários cobertos (7/7):
  1. Listar usuários
  2. Cadastrar usuário válido
  3. Cadastrar usuário com e-mail duplicado
  4. Cadastrar usuário com campos obrigatórios ausentes
  5. Buscar usuário por ID
  6. Atualizar usuário
  7. Excluir usuário
"""
import pytest

from fixtures.data_factory import gerar_usuario
from schemas.usuarios_schema import (
    SCHEMA_LISTAR_USUARIOS,
    SCHEMA_USUARIO,
)
from utils.helpers import validar_schema


@pytest.mark.usuarios
class TestListarUsuarios:
    def test_listar_usuarios_retorna_200_e_estrutura_correta(self, usuarios_api):
        """GET /usuarios deve retornar 200 e conter 'quantidade' e 'usuarios'."""
        response = usuarios_api.listar()

        assert response.status_code == 200
        body = response.json()
        validar_schema(body, SCHEMA_LISTAR_USUARIOS)
        assert isinstance(body["quantidade"], int)
        assert isinstance(body["usuarios"], list)


@pytest.mark.usuarios
class TestCadastrarUsuario:
    def test_cadastrar_usuario_valido_retorna_201(self, usuario_cadastrado):
        """POST /usuarios com dados válidos deve retornar 201 e o _id do usuário.

        Usa a fixture 'usuario_cadastrado' que gerencia setup e teardown
        automaticamente, mantendo consistência com os demais testes da suíte.
        """
        assert usuario_cadastrado["id"] is not None
        assert isinstance(usuario_cadastrado["id"], str)
        assert len(usuario_cadastrado["id"]) > 0
        assert usuario_cadastrado["email"].endswith("@qa.com")

    def test_cadastrar_usuario_email_duplicado_retorna_400(
        self, usuarios_api, usuario_cadastrado
    ):
        """POST /usuarios com e-mail já existente deve retornar 400."""
        payload = gerar_usuario()
        payload["email"] = usuario_cadastrado["email"]

        response = usuarios_api.cadastrar(payload)

        assert response.status_code == 400
        body = response.json()
        assert "message" in body
        assert body["message"] == "Este email já está sendo usado"

    def test_cadastrar_usuario_sem_nome_retorna_400(self, usuarios_api):
        """POST /usuarios sem o campo 'nome' deve retornar 400."""
        payload = gerar_usuario()
        del payload["nome"]

        response = usuarios_api.cadastrar(payload)

        assert response.status_code == 400
        body = response.json()
        assert "nome" in body  # API retorna o nome do campo que falhou, não "message"

    def test_cadastrar_usuario_sem_email_retorna_400(self, usuarios_api):
        """POST /usuarios sem o campo 'email' deve retornar 400."""
        payload = gerar_usuario()
        del payload["email"]

        response = usuarios_api.cadastrar(payload)

        assert response.status_code == 400
        body = response.json()
        assert "email" in body

    def test_cadastrar_usuario_sem_password_retorna_400(self, usuarios_api):
        """POST /usuarios sem o campo 'password' deve retornar 400."""
        payload = gerar_usuario()
        del payload["password"]

        response = usuarios_api.cadastrar(payload)

        assert response.status_code == 400
        body = response.json()
        assert "password" in body


@pytest.mark.usuarios
class TestBuscarUsuario:
    def test_buscar_usuario_por_id_valido_retorna_200(
        self, usuarios_api, usuario_cadastrado
    ):
        """GET /usuarios/{id} com ID existente deve retornar 200 e os dados do usuário."""
        usuario_id = usuario_cadastrado["id"]
        response = usuarios_api.buscar_por_id(usuario_id)

        assert response.status_code == 200
        body = response.json()
        validar_schema(body, SCHEMA_USUARIO)
        assert body["_id"] == usuario_id
        assert body["email"] == usuario_cadastrado["email"]
        assert body["nome"] == usuario_cadastrado["nome"]

    def test_buscar_usuario_com_id_malformado_retorna_400(self, usuarios_api):
        """GET /usuarios/{id} com ID de formato inválido deve retornar 400.

        A API valida o formato antes de consultar a base — IDs devem ter
        exatamente 16 caracteres alfanuméricos. A chave de erro retornada
        é "id", não "message" como nos demais erros da API (ver BUG-002).
        """
        response = usuarios_api.buscar_por_id("id_invalido_xyz")

        assert response.status_code == 400
        body = response.json()
        assert "id" in body, f"Campo 'id' ausente na resposta: {body}"
        assert body["id"] == "id deve ter exatamente 16 caracteres alfanuméricos"

    def test_buscar_usuario_com_id_inexistente_retorna_400(self, usuarios_api):
        """GET /usuarios/{id} com ID no formato correto mas inexistente na base deve retornar 400."""
        response = usuarios_api.buscar_por_id("0000000000000000")

        assert response.status_code == 400
        body = response.json()
        assert "message" in body, f"Campo 'message' ausente na resposta: {body}"
        assert body["message"] == "Usuário não encontrado"


@pytest.mark.usuarios
class TestAtualizarUsuario:
    def test_atualizar_usuario_retorna_200(self, usuarios_api, usuario_cadastrado):
        """PUT /usuarios/{id} com dados válidos deve retornar 200."""
        usuario_id = usuario_cadastrado["id"]
        payload_atualizado = gerar_usuario()
        payload_atualizado["administrador"] = usuario_cadastrado["administrador"]

        response = usuarios_api.atualizar(usuario_id, payload_atualizado)

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Registro alterado com sucesso"


@pytest.mark.usuarios
class TestExcluirUsuario:
    def test_excluir_usuario_existente_retorna_200(self, usuarios_api):
        """DELETE /usuarios/{id} de um usuário existente deve retornar 200."""
        payload = gerar_usuario()
        criado = usuarios_api.cadastrar(payload)
        assert criado.status_code == 201
        usuario_id = criado.json()["_id"]

        response = usuarios_api.excluir(usuario_id)

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Registro excluído com sucesso"

    def test_excluir_usuario_inexistente_retorna_200_sem_exclusao(self, usuarios_api):
        """DELETE /usuarios/{id} de ID inexistente deve retornar 200 — comportamento idempotente da API."""
        response = usuarios_api.excluir("id_inexistente_xyz")

        assert response.status_code == 200
        body = response.json()
        assert "message" in body
        assert body["message"] == "Nenhum registro excluído"
