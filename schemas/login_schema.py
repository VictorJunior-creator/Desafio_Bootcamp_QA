"""
Schemas de validação de contrato para o endpoint /login.
"""

SCHEMA_LOGIN_SUCESSO = {
    "type": "object",
    "required": ["message", "authorization"],
    "properties": {
        "message": {"type": "string"},
        "authorization": {"type": "string"},
    },
    "additionalProperties": False,
}

SCHEMA_LOGIN_FALHA = {
    "type": "object",
    "required": ["message"],
    "properties": {"message": {"type": "string"}},
    "additionalProperties": False,
}
