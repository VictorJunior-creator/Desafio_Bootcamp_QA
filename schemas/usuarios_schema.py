"""
Schemas de validação de contrato para o endpoint /usuarios.
Usados para garantir que a estrutura do JSON de resposta é a esperada.
"""

# Campos obrigatórios na listagem de usuários
SCHEMA_LISTAR_USUARIOS = {"quantidade", "usuarios"}

# Campos obrigatórios num objeto de usuário individual
SCHEMA_USUARIO = {"nome", "email", "password", "administrador", "_id"}

# Campos retornados no cadastro de usuário
SCHEMA_CADASTRO_SUCESSO = {"message", "_id"}
