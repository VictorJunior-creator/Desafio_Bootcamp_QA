"""
Camada de abstração para o endpoint /login da ServeRest.
"""
from api.base_client import BaseClient


class LoginAPI(BaseClient):
    ENDPOINT = "/login"

    def autenticar(self, payload: dict):
        return self.post(self.ENDPOINT, json=payload)
