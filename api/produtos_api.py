"""
Camada de abstração para o endpoint /produtos da ServeRest.
"""
from api.base_client import BaseClient


class ProdutosAPI(BaseClient):
    ENDPOINT = "/produtos"

    def listar(self, params: dict = None):
        return self.get(self.ENDPOINT, params=params)

    def cadastrar(self, payload: dict):
        return self.post(self.ENDPOINT, json=payload)

    def buscar_por_id(self, produto_id: str):
        return self.get(f"{self.ENDPOINT}/{produto_id}")

    def atualizar(self, produto_id: str, payload: dict):
        return self.put(f"{self.ENDPOINT}/{produto_id}", json=payload)

    def excluir(self, produto_id: str):
        return self.delete(f"{self.ENDPOINT}/{produto_id}")
