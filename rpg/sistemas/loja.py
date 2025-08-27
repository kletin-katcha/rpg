from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

from ..dados.itens import TODOS_OS_ITENS

def get_preco_compra(id_item: str, loja_data: Dict[str, Any]) -> int:
    """Calcula o preço que um jogador paga para comprar um item."""
    preco_base = TODOS_OS_ITENS.get(id_item, {}).get("valor", 0)
    multiplicador = loja_data.get("multiplicador_preco_compra", 1.0)
    return int(preco_base * multiplicador)

def get_preco_venda(id_item: str, loja_data: Dict[str, Any]) -> int:
    """Calcula o preço que um jogador recebe ao vender um item."""
    preco_base = TODOS_OS_ITENS.get(id_item, {}).get("valor", 0)
    multiplicador = loja_data.get("multiplicador_preco_venda", 1.0)
    return int(preco_base * multiplicador)

def comprar_item(jogador: 'Personagem', loja_data: Dict[str, Any], id_item: str, quantidade: int = 1) -> str:
    """
    Processa a compra de um item pelo jogador.
    Retorna uma mensagem de status.
    """
    if id_item not in loja_data["inventario"]:
        return "A loja não vende este item."

    preco_total = get_preco_compra(id_item, loja_data) * quantidade
    if jogador.ouro < preco_total:
        return f"Você não tem ouro suficiente. Custa {preco_total} de ouro."

    jogador.ouro -= preco_total
    jogador.adicionar_item(id_item, quantidade)

    nome_item = TODOS_OS_ITENS.get(id_item, {}).get("nome", id_item)
    return f"Você comprou {quantidade}x {nome_item} por {preco_total} de ouro."

def vender_item(jogador: 'Personagem', loja_data: Dict[str, Any], id_item: str, quantidade: int = 1) -> str:
    """
    Processa a venda de um item pelo jogador.
    Retorna uma mensagem de status.
    """
    if id_item not in jogador.inventario:
        return "Você não possui este item para vender."

    if jogador.inventario[id_item]["quantidade"] < quantidade:
        return f"Você não tem {quantidade} unidades deste item para vender."

    preco_total = get_preco_venda(id_item, loja_data) * quantidade

    sucesso = jogador.remover_item(id_item, quantidade)
    if sucesso:
        jogador.ouro += preco_total
        nome_item = TODOS_OS_ITENS.get(id_item, {}).get("nome", id_item)
        return f"Você vendeu {quantidade}x {nome_item} por {preco_total} de ouro."
    else:
        # Esta parte é uma segurança, mas a verificação de quantidade acima deve prevenir.
        return "Ocorreu um erro ao tentar vender o item."
