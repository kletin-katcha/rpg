from .common import ContentValidationError, ensure_keys, ensure_positive_int


TIERS_VALIDOS = {"bronze", "prata", "ouro", "lendario"}


def validate_contrato(entry: dict, context: str) -> None:
    ensure_keys(
        entry,
        {"id", "nome", "objetivo", "tier", "xp", "ouro", "faccao_id", "reputacao_ganho", "reputacao_perda"},
        context,
    )
    for key in ("id", "nome", "objetivo", "faccao_id", "tier"):
        if not isinstance(entry[key], str) or not entry[key].strip():
            raise ContentValidationError(f"{context}: {key} inválido")

    if entry["tier"] not in TIERS_VALIDOS:
        raise ContentValidationError(f"{context}: tier inválido")

    ensure_positive_int(entry["xp"], "xp", context)
    ensure_positive_int(entry["ouro"], "ouro", context)
    ensure_positive_int(entry["reputacao_ganho"], "reputacao_ganho", context)
    ensure_positive_int(entry["reputacao_perda"], "reputacao_perda", context)
