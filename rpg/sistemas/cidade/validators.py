def tem_ouro_suficiente(jogador, custo: int) -> bool:
    return jogador.ouro >= custo


def tem_nivel_suficiente(jogador, nivel_minimo: int) -> bool:
    return jogador.nivel >= nivel_minimo


def ja_tem_classe_secundaria(jogador) -> bool:
    return bool(jogador.classe_secundaria)


def tem_classe_principal(jogador) -> bool:
    return bool(jogador.classe)
