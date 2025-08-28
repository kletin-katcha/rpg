from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def pode_criar(jogador: 'Personagem', receita: Dict[str, Any]) -> bool:
    """Verifica se o jogador tem todos os ingredientes necessários para uma receita."""
    for ingrediente in receita["ingredientes"]:
        id_item = ingrediente["id_item"]
        quantidade_necessaria = ingrediente["quantidade"]

        if id_item not in jogador.inventario:
            return False
        if jogador.inventario[id_item]["quantidade"] < quantidade_necessaria:
            return False

    return True

def criar_item(jogador: 'Personagem', receita: Dict[str, Any]) -> str:
    """
    Tenta criar um item a partir de uma receita.
    Retorna uma mensagem de status.
    """
    if not pode_criar(jogador, receita):
        return "Você não tem os ingredientes necessários."

    # Consumir ingredientes
    for ingrediente in receita["ingredientes"]:
        id_item = ingrediente["id_item"]
        quantidade_necessaria = ingrediente["quantidade"]
        jogador.remover_item(id_item, quantidade_necessaria)

    # Adicionar item criado
    from ..dados.itens import TODOS_OS_ITENS
    id_item_criado = receita["id_item_criado"]
    nome_item_criado = TODOS_OS_ITENS.get(id_item_criado, {}).get("nome", id_item_criado)

    jogador.adicionar_item(id_item_criado, 1) # Assumindo que cada receita cria 1 item

    return f"Você criou {nome_item_criado} com sucesso!"
