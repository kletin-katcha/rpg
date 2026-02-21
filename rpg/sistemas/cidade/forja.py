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
            "tipo": "pergunta",
            "prompt": "Deseja forjar uma Machadinha Reciclada? (s/n)",
            "acao": "forjar_machadinha",
            "log": logs,
        }

    return {"tipo": "feedback", "log": logs}


def executar_forja_machadinha(jogador):
    logs_forja = metalurgia.forjar_machadinha_reciclada(jogador)
    if "machadinha_reciclada" in jogador.inventario and jogador.equipamentos.get("arma_principal") is None:
        jogador.equipar_item("machadinha_reciclada")
        logs_forja.append("A nova machadinha foi equipada automaticamente.")

    return {"tipo": "feedback", "log": logs_forja}
