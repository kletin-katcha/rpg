from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_plano_automacao(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "estrutura_requerida", "ganhos"}, context)
    for key in ("id", "nome", "estrutura_requerida"):
        if not isinstance(entry[key], str) or not entry[key].strip():
            raise ContentValidationError(f"{context}: '{key}' inválido")

    ganhos = entry["ganhos"]
    if not isinstance(ganhos, dict) or not ganhos:
        raise ContentValidationError(f"{context}: 'ganhos' deve ser objeto não vazio")
    for item_id, qtd in ganhos.items():
        if not isinstance(item_id, str) or not item_id.strip():
            raise ContentValidationError(f"{context}: item inválido em ganhos")
        ensure_positive_int(qtd, f"ganhos.{item_id}", context)
