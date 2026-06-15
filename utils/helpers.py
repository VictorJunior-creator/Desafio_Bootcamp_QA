"""
Funções auxiliares reutilizáveis para validações comuns nos testes.
"""

from jsonschema import ValidationError, validate


def validar_schema(body: dict, schema: dict) -> None:
    """
    Valida a resposta JSON contra um schema JSON Schema.

    Args:
        body: dicionário retornado pela API
        schema: JSON Schema que descreve a estrutura esperada
    """
    try:
        validate(instance=body, schema=schema)
    except ValidationError as error:
        raise AssertionError(
            f"Resposta não corresponde ao schema: {error.message}\nResposta: {body}"
        )
