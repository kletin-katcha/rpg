from .common import ContentValidationError, ensure_keys, ensure_positive_int

ARQUETIPOS_VALIDOS = {"agressivo", "defensivo", "venenoso", "boss"}


def validate_monstro(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "nivel", "hp_max", "ataque_base", "xp", "loot"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")
    ensure_positive_int(entry["nivel"], "nivel", context)
    ensure_positive_int(entry["hp_max"], "hp_max", context)
    ensure_positive_int(entry["ataque_base"], "ataque_base", context)
    ensure_positive_int(entry["xp"], "xp", context)

    if "velocidade" in entry:
        ensure_positive_int(entry["velocidade"], "velocidade", context)

    if "arquetipo" in entry and entry["arquetipo"] not in ARQUETIPOS_VALIDOS:
        raise ContentValidationError(f"{context}: arquetipo inválido")

    if "areas" in entry:
        if not isinstance(entry["areas"], list) or not entry["areas"]:
            raise ContentValidationError(f"{context}: 'areas' deve ser lista não vazia")
        for area in entry["areas"]:
            if not isinstance(area, str) or not area.strip():
                raise ContentValidationError(f"{context}: area inválida em 'areas'")

    if not isinstance(entry["loot"], dict):
        raise ContentValidationError(f"{context}: 'loot' deve ser objeto")
    for item_id, qtd in entry["loot"].items():
        if not isinstance(item_id, str) or not item_id:
            raise ContentValidationError(f"{context}: loot item inválido")
        ensure_positive_int(qtd, f"loot.{item_id}", context)
