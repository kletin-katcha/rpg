from random import choice

from rpg.content.loader import load_catalog
from rpg.systems.character.service import conceder_xp


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


def concluir_contrato(personagem, reputacoes: dict[str, int], ouro_atual: int, contrato: dict) -> dict:
    conceder_xp(personagem, contrato["xp"])
    novo_ouro = ouro_atual + contrato["ouro"]
    faccao_id = contrato["faccao_id"]
    reputacoes[faccao_id] = reputacoes.get(faccao_id, 0) + contrato["reputacao_ganho"]
    return {
        "ouro": novo_ouro,
        "faccao_id": faccao_id,
        "reputacao": reputacoes[faccao_id],
        "xp": contrato["xp"],
    }
