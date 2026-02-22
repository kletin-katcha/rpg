from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_faccao(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "reputacao_inicial"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: id inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: nome inválido")
    ensure_positive_int(entry["reputacao_inicial"], "reputacao_inicial", context)
