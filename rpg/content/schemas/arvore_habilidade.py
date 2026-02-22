from .common import ContentValidationError, ensure_keys


def validate_arvore_habilidade(entry: dict, context: str) -> None:
    ensure_keys(entry, {"id", "nome", "dominio", "nodos"}, context)
    for key in ("id", "nome", "dominio"):
        if not isinstance(entry[key], str) or not entry[key].strip():
            raise ContentValidationError(f"{context}: '{key}' inválido")

    nodos = entry["nodos"]
    if not isinstance(nodos, list) or not nodos:
        raise ContentValidationError(f"{context}: 'nodos' deve ser lista não vazia")
    for i, nodo in enumerate(nodos):
        if not isinstance(nodo, dict):
            raise ContentValidationError(f"{context}: nodo[{i}] inválido")
        if not isinstance(nodo.get("id"), str) or not nodo["id"].strip():
            raise ContentValidationError(f"{context}: nodo[{i}].id inválido")
        req = nodo.get("requer")
        if req is not None and (not isinstance(req, list) or not all(isinstance(x, str) for x in req)):
            raise ContentValidationError(f"{context}: nodo[{i}].requer inválido")
