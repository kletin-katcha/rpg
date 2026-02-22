from rpg.core.errors import RecursoInsuficienteError


def adicionar_item(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]:
    if qtd <= 0:
        return inventario
    inventario[item_id] = inventario.get(item_id, 0) + qtd
    return inventario


def remover_item(inventario: dict[str, int], item_id: str, qtd: int = 1) -> dict[str, int]:
    if qtd <= 0:
        return inventario

    atual = inventario.get(item_id, 0)
    if atual < qtd:
        raise RecursoInsuficienteError(
            f"Quantidade insuficiente de '{item_id}'. Atual: {atual}, necessário: {qtd}"
        )

    novo_valor = atual - qtd
    if novo_valor == 0:
        inventario.pop(item_id, None)
    else:
        inventario[item_id] = novo_valor
    return inventario
