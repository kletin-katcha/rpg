"""Fluxos de forja acionados no menu de cidade."""
from ...sistemas import metalurgia


def executar_forja_prototipo(jogador):
    logs_fundicao = []
    while (
        jogador.inventario.get("caco_de_arma_enferrujada", {}).get("quantidade", 0) >= 3
        and jogador.inventario.get("barra_metal_reciclado", {}).get("quantidade", 0) < 2
    ):
        logs_fundicao.extend(metalurgia.fundir_sucata_em_barra(jogador))

    if not logs_fundicao:
        logs_fundicao = metalurgia.fundir_sucata_em_barra(jogador)

    logs_forja = metalurgia.forjar_lamina_reciclada(jogador)
    logs = logs_fundicao + logs_forja

    if "lamina_reciclada" in jogador.inventario and jogador.equipamentos.get("arma_principal") is None:
        jogador.equipar_item("lamina_reciclada")
        logs.append("A lâmina reciclada foi equipada automaticamente.")

    if jogador.inventario.get("barra_metal_reciclado", {}).get("quantidade", 0) >= 2:
        return {
            "tipo": "selecao",
            "prompt": "Escolha uma forja adicional:",
            "opcoes": ["forjar_machadinha", "forjar_machado_batalha", "forjar_espada_longa_avancada", "forjar_peitoral_avancado"],
            "acao_prefixo": "acao_forja",
            "log": logs,
        }

    return {"tipo": "feedback", "log": logs}


def executar_forja_machadinha(jogador):
    logs_forja = metalurgia.forjar_machadinha_reciclada(jogador)
    if "machadinha_reciclada" in jogador.inventario and jogador.equipamentos.get("arma_principal") is None:
        jogador.equipar_item("machadinha_reciclada")
        logs_forja.append("A nova machadinha foi equipada automaticamente.")

    return {"tipo": "feedback", "log": logs_forja}


def executar_forja_machado_batalha(jogador):
    logs_forja = metalurgia.forjar_machado_batalha_ferro(jogador)
    if "machado_de_batalha_ferro" in jogador.inventario and jogador.equipamentos.get("arma_principal") is None:
        jogador.equipar_item("machado_de_batalha_ferro")
        logs_forja.append("O machado de batalha foi equipado automaticamente.")

    return {"tipo": "feedback", "log": logs_forja}


def executar_forja_receita_avancada(jogador, id_receita: str):
    logs = metalurgia.forjar_receita_avancada(jogador, id_receita)
    if id_receita == "espada_longa_reciclada" and "espada_longa_reciclada" in jogador.inventario and jogador.equipamentos.get("arma_principal") is None:
        jogador.equipar_item("espada_longa_reciclada")
        logs.append("A espada longa reciclada foi equipada automaticamente.")
    if id_receita == "peitoral_reciclado" and "peitoral_reciclado" in jogador.inventario and jogador.equipamentos.get("peitoral") is None:
        jogador.equipar_item("peitoral_reciclado")
        logs.append("O peitoral reciclado foi equipado automaticamente.")
    return {"tipo": "feedback", "log": logs}
