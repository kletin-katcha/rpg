from typing import TYPE_CHECKING, List
from ..dados.metalurgia import (
    RECEITA_BARRA_RECICLADA,
    RECEITA_LAMINA_RECICLADA,
    RECEITA_MACHADINHA_RECICLADA,
)

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem


def _tem_itens_suficientes(jogador: 'Personagem', custo: dict[str, int]) -> bool:
    for id_item, quantidade in custo.items():
        entrada = jogador.inventario.get(id_item)
        if not entrada or entrada["quantidade"] < quantidade:
            return False
    return True


def _consumir_itens(jogador: 'Personagem', custo: dict[str, int]):
    for id_item, quantidade in custo.items():
        jogador.remover_item(id_item, quantidade)


def fundir_sucata_em_barra(jogador: 'Personagem') -> List[str]:
    """Converte sucata (cacos) em barra reciclada para o MVP."""
    if not _tem_itens_suficientes(jogador, RECEITA_BARRA_RECICLADA["entrada"]):
        return ["Você não possui sucata suficiente. Precisa de 3x caco_de_arma_enferrujada."]

    _consumir_itens(jogador, RECEITA_BARRA_RECICLADA["entrada"])
    for id_item, quantidade in RECEITA_BARRA_RECICLADA["saida"].items():
        jogador.adicionar_item(id_item, quantidade)

    return ["Você fundiu sucata goblin e criou 1x barra_metal_reciclado."]


def forjar_lamina_reciclada(jogador: 'Personagem') -> List[str]:
    """Forja uma arma inicial simples a partir das barras recicladas."""
    if not _tem_itens_suficientes(jogador, RECEITA_LAMINA_RECICLADA["entrada"]):
        return ["Você precisa de 2x barra_metal_reciclado para forjar a lâmina."]

    _consumir_itens(jogador, RECEITA_LAMINA_RECICLADA["entrada"])
    for id_item, quantidade in RECEITA_LAMINA_RECICLADA["saida"].items():
        jogador.adicionar_item(id_item, quantidade)

    return ["A forja crepita! Você criou 1x lamina_reciclada."]


def forjar_machadinha_reciclada(jogador: 'Personagem') -> List[str]:
    """Forja uma alternativa de arma de impacto com a mesma base de barras."""
    if not _tem_itens_suficientes(jogador, RECEITA_MACHADINHA_RECICLADA["entrada"]):
        return ["Você precisa de 2x barra_metal_reciclado para forjar a machadinha."]

    _consumir_itens(jogador, RECEITA_MACHADINHA_RECICLADA["entrada"])
    for id_item, quantidade in RECEITA_MACHADINHA_RECICLADA["saida"].items():
        jogador.adicionar_item(id_item, quantidade)

    return ["Faíscas saltam da bigorna! Você criou 1x machadinha_reciclada."]
