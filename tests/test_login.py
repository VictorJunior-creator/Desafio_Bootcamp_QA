"""
Testes automatizados para o endpoint /login da API ServeRest.

Cenários cobertos (4/4):
  1. Login válido com credenciais corretas
  2. Login com senha incorreta
  3. Login com e-mail inexistente
  4. Login com campos vazios
"""
import pytest

from schemas.login_schema import SCHEMA_LOGIN_SUCESSO, SCHEMA_LOGIN_FALHA
from utils.helpers import validar_schema


@pytest.mark.login
class TestLoginValido:
    def test_login_com_credenciais_corretas_retorna_200_e_token(
        self, login_api, usuario_admin_cadastrado
    ):
        """POST /login com e-mail e senha válidos deve retornar 200 e um token Bearer."""
        payload = {
            "email": usuario_admin_cadastrado["email"],
            "password": usuario_admin_cadastrado["password"],
        }
        response = login_api.autenticar(payload)

        assert response.status_code == 200
        body = response.json()
        validar_schema(body, SCHEMA_LOGIN_SUCESSO)
        assert body["message"] == "Login realizado com sucesso"
        assert body["authorization"].startswith("Bearer ")


@pytest.mark.login
class TestLoginInvalido:
    def test_login_com_senha_incorreta_retorna_401(
        self, login_api, usuario_admin_cadastrado
    ):
        """POST /login com senha errada deve retornar 401."""
        payload = {
            "email": usuario_admin_cadastrado["email"],
            "password": "senha_errada_123",
        }
        response = login_api.autenticar(payload)

        assert response.status_code == 401
        body = response.json()
        validar_schema(body, SCHEMA_LOGIN_FALHA)
        assert body["message"] == "Email e/ou senha inválidos"

    def test_login_com_email_inexistente_retorna_401(self, login_api):
        """POST /login com e-mail que não existe deve retornar 401."""
        payload = {
            "email": "nao_existe_jamais@qa.com",
            "password": "qualquer_senha",
        }
        response = login_api.autenticar(payload)

        assert response.status_code == 401
        body = response.json()
        validar_schema(body, SCHEMA_LOGIN_FALHA)
        assert body["message"] == "Email e/ou senha inválidos"

    def test_login_com_campos_vazios_retorna_400(self, login_api):
        """POST /login com e-mail e senha em branco deve retornar 400.

        A API retorna ambos os campos de validação simultaneamente:
        {"email": "email não pode ficar em branco", "password": "password não pode ficar em branco"}
        """
        payload = {
            "email": "",
            "password": "",
        }
        response = login_api.autenticar(payload)

        assert response.status_code == 400
        body = response.json()
        assert "email" in body, f"Campo 'email' ausente na resposta: {body}"
        assert body["email"] == "email não pode ficar em branco"
        assert "password" in body, f"Campo 'password' ausente na resposta: {body}"
        assert body["password"] == "password não pode ficar em branco"
