"""Sistema de metalurgia e forja com trilhas base e avançada."""
from typing import TYPE_CHECKING, List
from ..dados.metalurgia import (
    RECEITA_BARRA_RECICLADA,
    RECEITA_LAMINA_RECICLADA,
    RECEITA_MACHADINHA_RECICLADA,
    RECEITA_MACHADO_BATALHA_FERRO,
    RECEITAS_AVANCADAS_BLOQUEADAS,
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


def forjar_machado_batalha_ferro(jogador: 'Personagem') -> List[str]:
    """Forja um machado de batalha superior para o meio do jogo inicial."""
    if not _tem_itens_suficientes(jogador, RECEITA_MACHADO_BATALHA_FERRO["entrada"]):
        return ["Você precisa de 3x barra_metal_reciclado e 1x ferrao_de_vespa para forjar o machado de batalha."]

    _consumir_itens(jogador, RECEITA_MACHADO_BATALHA_FERRO["entrada"])
    for id_item, quantidade in RECEITA_MACHADO_BATALHA_FERRO["saida"].items():
        jogador.adicionar_item(id_item, quantidade)

    return ["Marteladas precisas! Você criou 1x machado_de_batalha_ferro."]


def forjar_receita_avancada(jogador: 'Personagem', id_receita: str) -> List[str]:
    """Forja uma receita avançada validando custos e nível mínimo de forja."""
    receita = RECEITAS_AVANCADAS_BLOQUEADAS.get(id_receita)
    if not receita:
        return ["Receita avançada inexistente."]

    nivel_forja = jogador.niveis_estruturas.get("oficina_basica", 1)
    if nivel_forja < receita.get("requisito_nivel_forja", 99):
        return [f"Oficina insuficiente. Requer nível {receita.get('requisito_nivel_forja')}." ]

    if not _tem_itens_suficientes(jogador, receita["entrada"]):
        return ["Materiais insuficientes para a receita avançada."]

    _consumir_itens(jogador, receita["entrada"])
    for id_item, quantidade in receita["saida"].items():
        jogador.adicionar_item(id_item, quantidade)

    return [f"Forja avançada concluída: {id_receita}."]
