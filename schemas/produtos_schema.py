"""
Schemas de validação de contrato para o endpoint /produtos.
"""

# Campos obrigatórios na listagem de produtos
SCHEMA_LISTAR_PRODUTOS = {"quantidade", "produtos"}

# Campos obrigatórios num objeto de produto individual
SCHEMA_PRODUTO = {"nome", "preco", "descricao", "quantidade", "_id"}

# Campos retornados no cadastro de produto
SCHEMA_CADASTRO_SUCESSO = {"message", "_id"}
