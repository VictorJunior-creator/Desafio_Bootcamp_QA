"""
Schemas de validação de contrato para o endpoint /produtos.
"""

SCHEMA_LISTAR_PRODUTOS = {
    "type": "object",
    "required": ["quantidade", "produtos"],
    "properties": {
        "quantidade": {"type": "integer"},
        "produtos": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["_id", "nome", "preco", "descricao", "quantidade"],
                "properties": {
                    "_id": {"type": "string"},
                    "nome": {"type": "string"},
                    "preco": {"type": "number"},
                    "descricao": {"type": "string"},
                    "quantidade": {"type": "integer"},
                },
                "additionalProperties": False,
            },
        },
    },
    "additionalProperties": False,
}

SCHEMA_PRODUTO = {
    "type": "object",
    "required": ["_id", "nome", "preco", "descricao", "quantidade"],
    "properties": {
        "_id": {"type": "string"},
        "nome": {"type": "string"},
        "preco": {"type": "number"},
        "descricao": {"type": "string"},
        "quantidade": {"type": "integer"},
    },
    "additionalProperties": False,
}

SCHEMA_CADASTRO_SUCESSO = {
    "type": "object",
    "required": ["message", "_id"],
    "properties": {
        "message": {"type": "string"},
        "_id": {"type": "string"},
    },
    "additionalProperties": False,
}
