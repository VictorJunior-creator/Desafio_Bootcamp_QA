"""
Camada de abstração para o endpoint /usuarios da ServeRest.
Isola as chamadas HTTP dos testes, facilitando manutenção.
"""
from api.base_client import BaseClient


class UsuariosAPI(BaseClient):
    ENDPOINT = "/usuarios"

    def listar(self, params: dict = None):
        return self.get(self.ENDPOINT, params=params)

    def cadastrar(self, payload: dict):
        return self.post(self.ENDPOINT, json=payload)

    def buscar_por_id(self, usuario_id: str):
        return self.get(f"{self.ENDPOINT}/{usuario_id}")

    def atualizar(self, usuario_id: str, payload: dict):
        return self.put(f"{self.ENDPOINT}/{usuario_id}", json=payload)

    def excluir(self, usuario_id: str):
        return self.delete(f"{self.ENDPOINT}/{usuario_id}")
