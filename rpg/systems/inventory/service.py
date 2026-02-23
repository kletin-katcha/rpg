from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError

from .rules import adicionar_item, remover_item


def adicionar_item_catalogado(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]:
    itens = load_catalog("itens")
    if item_id not in itens:
        raise RegraNegocioError(f"Item não cadastrado no catálogo: {item_id}")
    return adicionar_item(inventario, item_id, qtd)


def remover_item_catalogado(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]:
    return remover_item(inventario, item_id, qtd)
