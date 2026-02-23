from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.systems.inventory.rules import adicionar_item, remover_item


def forjar_receita(inventario: dict[str, int], receita_id: str) -> dict[str, int]:
    receitas = load_catalog("receitas")
    if receita_id not in receitas:
        raise RegraNegocioError(f"Receita inválida: {receita_id}")

    receita = receitas[receita_id]
    for item_id, qtd in receita["insumos"].items():
        if inventario.get(item_id, 0) < qtd:
            raise RegraNegocioError(f"Insumo insuficiente: {item_id}")

    for item_id, qtd in receita["insumos"].items():
        remover_item(inventario, item_id, qtd)

    for item_id, qtd in receita["resultado"].items():
        adicionar_item(inventario, item_id, qtd)

    return inventario
