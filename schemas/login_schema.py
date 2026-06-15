"""
Schemas de validação de contrato para o endpoint /login.
"""

# Campos retornados num login bem-sucedido
SCHEMA_LOGIN_SUCESSO = {"message", "authorization"}

# Campos retornados num login com falha
SCHEMA_LOGIN_FALHA = {"message"}
