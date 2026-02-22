from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_contrato(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "objetivo", "xp", "ouro", "faccao_id", "reputacao_ganho"}, context)
    for key in ("id", "nome", "objetivo", "faccao_id"):
        if not isinstance(entry[key], str) or not entry[key].strip():
            raise ContentValidationError(f"{context}: {key} inválido")
    ensure_positive_int(entry["xp"], "xp", context)
    ensure_positive_int(entry["ouro"], "ouro", context)
    ensure_positive_int(entry["reputacao_ganho"], "reputacao_ganho", context)
