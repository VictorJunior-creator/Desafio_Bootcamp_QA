"""
Schemas de validação de contrato para o endpoint /usuarios.
Usados para garantir que a estrutura do JSON de resposta é a esperada.
"""

SCHEMA_LISTAR_USUARIOS = {
    "type": "object",
    "required": ["quantidade", "usuarios"],
    "properties": {
        "quantidade": {"type": "integer"},
        "usuarios": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["_id", "nome", "email", "password", "administrador"],
                "properties": {
                    "_id": {"type": "string"},
                    "nome": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "administrador": {"type": "string"},
                },
                "additionalProperties": False,
            },
        },
    },
    "additionalProperties": False,
}

SCHEMA_USUARIO = {
    "type": "object",
    "required": ["_id", "nome", "email", "password", "administrador"],
    "properties": {
        "_id": {"type": "string"},
        "nome": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "administrador": {"type": "string"},
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
