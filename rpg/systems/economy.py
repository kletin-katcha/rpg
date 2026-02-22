from rpg.content.loader import load_catalog
from rpg.core.errors import RegraNegocioError
from rpg.systems.inventory.rules import remover_item, adicionar_item


def iniciar_mercado() -> dict[str, float]:
    itens = load_catalog("itens")
    return {item_id: 1.0 for item_id in itens}


def atualizar_mercado(mercado: dict[str, float], dia: int) -> dict[str, float]:
    itens = sorted(load_catalog("itens").keys())
    for idx, item_id in enumerate(itens):
        ciclo = (dia + idx) % 5
        mercado[item_id] = 0.8 + (ciclo * 0.1)
    return mercado


def vender_item(inventario: dict[str, int], cidade_ouro: int, item_id: str, qtd: int, mercado: dict[str, float]) -> int:
    if qtd <= 0:
        raise RegraNegocioError("Quantidade para venda deve ser positiva")

    itens = load_catalog("itens")
    if item_id not in itens:
        raise RegraNegocioError(f"Item inválido para venda: {item_id}")

    remover_item(inventario, item_id, qtd)
    base = itens[item_id]["valor"]
    multiplicador = mercado.get(item_id, 1.0)
    ganho = int(base * multiplicador) * qtd
    return cidade_ouro + ganho


def produzir_liga_metal(inventario: dict[str, int]) -> dict[str, int]:
    if inventario.get("barra_metal", 0) < 2:
        raise RegraNegocioError("Barras de metal insuficientes para produzir liga")

    remover_item(inventario, "barra_metal", 2)
    adicionar_item(inventario, "liga_metal", 1)
    return inventario
