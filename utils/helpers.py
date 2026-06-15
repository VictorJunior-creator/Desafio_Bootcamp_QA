"""
Funções auxiliares reutilizáveis para validações comuns nos testes.
"""


def validar_schema(body: dict, campos_esperados: set) -> None:
    """
    Valida que todos os campos esperados estão presentes no corpo da resposta.

    Args:
        body: dicionário retornado pela API
        campos_esperados: conjunto de chaves obrigatórias
    """
    campos_ausentes = campos_esperados - body.keys()
    assert not campos_ausentes, (
        f"Campos ausentes na resposta: {campos_ausentes}. "
        f"Resposta recebida: {body}"
    )
