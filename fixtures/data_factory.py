"""
Factory de dados dinâmicos.
Usa UUID para garantir unicidade de e-mails e nomes de produtos,
evitando conflitos de dados entre execuções e testes paralelos.
"""
import uuid


def gerar_usuario(administrador: str = "false") -> dict:
    """Gera payload completo de um usuário com e-mail único."""
    uid = uuid.uuid4().hex[:8]
    return {
        "nome": f"Usuario Teste {uid}",
        "email": f"usuario_{uid}@qa.com",
        "password": "teste@123",
        "administrador": administrador,
    }


def gerar_usuario_admin() -> dict:
    """Gera payload de um usuário administrador."""
    return gerar_usuario(administrador="true")


def gerar_produto() -> dict:
    """Gera payload completo de um produto com nome único."""
    uid = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto Teste {uid}",
        "preco": 100,
        "descricao": f"Descricao do produto {uid}",
        "quantidade": 10,
    }
