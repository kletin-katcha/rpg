from random import choice

from rpg.content.loader import load_catalog


def iniciar_reputacoes() -> dict[str, int]:
    faccoes = load_catalog("faccoes")
    return {fid: data["reputacao_inicial"] for fid, data in faccoes.items()}


def aplicar_evento_mundo(ouro_atual: int, xp_bonus: int = 0) -> dict:
    eventos = list(load_catalog("eventos_mundo").values())
    evento = choice(eventos)
    ouro = ouro_atual
    xp = xp_bonus
    if evento["efeito"] == "ouro_bonus":
        ouro += 25
    elif evento["efeito"] == "xp_bonus":
        xp += 20
    return {"evento": evento["nome"], "ouro": ouro, "xp_bonus": xp}


def gerar_contrato_aleatorio() -> dict:
    contratos = list(load_catalog("contratos").values())
    return choice(contratos)
