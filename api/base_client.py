"""
Cliente base HTTP — centraliza a URL e os headers padrão.
Todos os clientes de API herdam desta classe.
"""
import requests

BASE_URL = "https://serverest.dev"


class BaseClient:
    """Encapsula a sessão HTTP e a URL base da API ServeRest."""

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint: str, **kwargs):
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs):
        return self.session.post(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs):
        return self.session.put(f"{self.base_url}{endpoint}", json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

    def set_auth_token(self, token: str):
        """Injeta o Bearer token na sessão."""
        self.session.headers.update({"Authorization": token})

    def clear_auth_token(self):
        """Remove o Bearer token da sessão."""
        self.session.headers.pop("Authorization", None)
