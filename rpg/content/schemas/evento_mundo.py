from .common import ContentValidationError, ensure_keys


def validate_evento_mundo(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "efeito"}, context)
    for key in ("id", "nome", "efeito"):
        if not isinstance(entry[key], str) or not entry[key].strip():
            raise ContentValidationError(f"{context}: {key} inválido")
