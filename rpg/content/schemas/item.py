from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_item(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "tipo", "valor"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")
    if not isinstance(entry["tipo"], str) or not entry["tipo"].strip():
        raise ContentValidationError(f"{context}: 'tipo' inválido")
    ensure_positive_int(entry["valor"], "valor", context)
