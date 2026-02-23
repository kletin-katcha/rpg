from .common import ContentValidationError, ensure_keys


def validate_raca(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "descricao", "bonus"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")
    if not isinstance(entry["descricao"], str):
        raise ContentValidationError(f"{context}: 'descricao' deve ser string")
    bonus = entry["bonus"]
    if not isinstance(bonus, dict):
        raise ContentValidationError(f"{context}: 'bonus' deve ser objeto")
    for atributo, valor in bonus.items():
        if not isinstance(atributo, str) or not isinstance(valor, int):
            raise ContentValidationError(f"{context}: bonus inválido em {atributo}")
