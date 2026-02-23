from .common import ContentValidationError, ensure_keys


def validate_classe(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "papel", "habilidades_iniciais"}, context)
    if not isinstance(entry["id"], str) or not entry["id"].strip():
        raise ContentValidationError(f"{context}: 'id' inválido")
    if not isinstance(entry["nome"], str) or not entry["nome"].strip():
        raise ContentValidationError(f"{context}: 'nome' inválido")
    if not isinstance(entry["papel"], str) or not entry["papel"].strip():
        raise ContentValidationError(f"{context}: 'papel' inválido")
    habilidades = entry["habilidades_iniciais"]
    if not isinstance(habilidades, list) or not all(isinstance(h, str) for h in habilidades):
        raise ContentValidationError(f"{context}: 'habilidades_iniciais' inválido")
