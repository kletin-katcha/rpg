from typing import Any


class ContentValidationError(ValueError):
    """Erro de validação de catálogo de conteúdo."""


def ensure_keys(data: dict[str, Any], required: set[str], context: str) -> None:
    missing = required.difference(data.keys())
    if missing:
        raise ContentValidationError(f"{context}: campos ausentes: {sorted(missing)}")


def ensure_positive_int(value: Any, field_name: str, context: str) -> None:
    if not isinstance(value, int) or value < 0:
        raise ContentValidationError(f"{context}: campo '{field_name}' deve ser inteiro >= 0")
