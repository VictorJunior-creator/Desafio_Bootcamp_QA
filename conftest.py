"""
conftest.py global — fixtures compartilhadas por todos os módulos de teste.

Escopo 'function' em todas as fixtures garante isolamento total entre testes,
evitando efeitos colaterais de estado compartilhado.
"""
import pytest

from api.usuarios_api import UsuariosAPI
from api.login_api import LoginAPI
from api.produtos_api import ProdutosAPI
from fixtures.data_factory import gerar_usuario_admin, gerar_usuario, gerar_produto


@pytest.fixture
def usuarios_api():
    """Retorna uma instância limpa do cliente de Usuários."""
    return UsuariosAPI()


@pytest.fixture
def login_api():
    """Retorna uma instância limpa do cliente de Login."""
    return LoginAPI()


@pytest.fixture
def produtos_api():
    """Retorna uma instância limpa do cliente de Produtos."""
    return ProdutosAPI()


@pytest.fixture
def usuario_admin_cadastrado(usuarios_api):
    """Cria um usuário administrador antes do teste e o remove após."""
    payload = gerar_usuario_admin()
    response = usuarios_api.cadastrar(payload)
    assert response.status_code == 201, (
        f"Falha ao criar usuário admin no setup: {response.text}"
    )
    usuario_id = response.json()["_id"]

    yield {"id": usuario_id, **payload}

    usuarios_api.excluir(usuario_id)


@pytest.fixture
def usuario_cadastrado(usuarios_api):
    """Cria um usuário comum antes do teste e o remove após."""
    payload = gerar_usuario()
    response = usuarios_api.cadastrar(payload)
    assert response.status_code == 201, (
        f"Falha ao criar usuário no setup: {response.text}"
    )
    usuario_id = response.json()["_id"]

    yield {"id": usuario_id, **payload}

    usuarios_api.excluir(usuario_id)


@pytest.fixture
def token_admin(usuario_admin_cadastrado, login_api):
    """
    Autentica o usuário admin e retorna o token Bearer.
    Escopo 'function' garante token sempre válido — o token da ServeRest expira em 10 minutos.
    """
    credentials = {
        "email": usuario_admin_cadastrado["email"],
        "password": usuario_admin_cadastrado["password"],
    }
    response = login_api.autenticar(credentials)
    assert response.status_code == 200, (
        f"Falha ao autenticar admin no setup: {response.text}"
    )
    return response.json()["authorization"]


@pytest.fixture
def produto_cadastrado(token_admin, produtos_api):
    """
    Cria um produto com token admin antes do teste e o remove após.
    Expõe o token no dict retornado para evitar que testes dependentes
    precisem solicitar token_admin como fixture separada (evita duplo setup).
    """
    produtos_api.set_auth_token(token_admin)
    payload = gerar_produto()
    response = produtos_api.cadastrar(payload)
    assert response.status_code == 201, (
        f"Falha ao criar produto no setup: {response.text}"
    )
    produto_id = response.json()["_id"]

    yield {"id": produto_id, "token": token_admin, **payload}

    produtos_api.excluir(produto_id)
    produtos_api.clear_auth_token()
