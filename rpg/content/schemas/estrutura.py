from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_estrutura(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "custo_base", "max_nivel"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")
    ensure_positive_int(entry["custo_base"], "custo_base", context)
    ensure_positive_int(entry["max_nivel"], "max_nivel", context)
    if entry["max_nivel"] < 1:
        raise ContentValidationError(f"{context}: 'max_nivel' deve ser >= 1")
