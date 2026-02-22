from .common import ContentValidationError, ensure_keys, ensure_positive_int


def validate_receita(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "insumos", "resultado"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")

    for campo in ("insumos", "resultado"):
        bloco = entry[campo]
        if not isinstance(bloco, dict) or not bloco:
            raise ContentValidationError(f"{context}: '{campo}' deve ser objeto não vazio")
        for item_id, qtd in bloco.items():
            if not isinstance(item_id, str) or not item_id.strip():
                raise ContentValidationError(f"{context}: item inválido em {campo}")
            ensure_positive_int(qtd, f"{campo}.{item_id}", context)
