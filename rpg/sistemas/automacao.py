"""Automação diária de coleta/refino com escalonamento por estrutura."""
from typing import TYPE_CHECKING, List
from ..dados.cidade.producao import PLANOS_PRODUCAO

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem


def _processar_refino_automatico(jogador: 'Personagem', logs: List[str]):
    if "automacao_refino" not in jogador.estruturas_construidas:
        return

    nivel_refino = jogador.niveis_estruturas.get("automacao_refino", 1)
    ciclos = nivel_refino
    for _ in range(ciclos):
        qtd = jogador.inventario.get("caco_de_arma_enferrujada", {}).get("quantidade", 0)
        if qtd < 3:
            break
        jogador.remover_item("caco_de_arma_enferrujada", 3)
        jogador.adicionar_item("barra_metal_reciclado", 1)
    logs.append(f"Autômato de refino processou até {ciclos} ciclo(s).")


def processar_ciclo_automatizado(jogador: 'Personagem') -> List[str]:
    logs: List[str] = []
    estruturas = getattr(jogador, "estruturas_construidas", set())

    if "automacao_coleta" in estruturas:
        nivel_automacao = jogador.niveis_estruturas.get("automacao_coleta", 1)
        plano = jogador.plano_producao_ativo or "coleta_mista"
        dados_plano = PLANOS_PRODUCAO.get(plano, PLANOS_PRODUCAO["coleta_mista"])

        for id_item, quantidade_base in dados_plano.get("recompensas", {}).items():
            jogador.adicionar_item(id_item, quantidade_base * nivel_automacao)

        logs.append(f"Seus autômatos executaram o plano '{plano}' (nível {nivel_automacao}).")

    _processar_refino_automatico(jogador, logs)

    if not logs:
        logs.append("Nenhuma automação ativa para este ciclo.")

    return logs
