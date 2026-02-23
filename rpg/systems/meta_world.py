from random import choice

from rpg.content.loader import load_catalog
from rpg.systems.character.service import conceder_xp


TIER_PESO = {"bronze": 1, "prata": 2, "ouro": 3, "lendario": 4}


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


def gerar_contrato_aleatorio(tier_maximo: str = "ouro") -> dict:
    contratos = list(load_catalog("contratos").values())
    peso_maximo = TIER_PESO.get(tier_maximo, 3)
    elegiveis = [c for c in contratos if TIER_PESO.get(c.get("tier", "bronze"), 1) <= peso_maximo]
    return choice(elegiveis or contratos)


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


def falhar_contrato(reputacoes: dict[str, int], contrato: dict) -> dict:
    faccao_id = contrato["faccao_id"]
    perda = contrato.get("reputacao_perda", 1)
    reputacoes[faccao_id] = reputacoes.get(faccao_id, 0) - perda
    return {"faccao_id": faccao_id, "reputacao": reputacoes[faccao_id], "perda": perda}


def resgatar_beneficio_faccao(reputacoes: dict[str, int], inventario: dict[str, int], ouro_atual: int, faccao_id: str) -> dict:
    reputacao = reputacoes.get(faccao_id, 0)
    if reputacao < 10:
        return {"ouro": ouro_atual, "beneficio": "nenhum", "detalhe": "Reputação insuficiente"}

    if faccao_id == "guilda_ferreiros":
        if reputacao >= 20:
            inventario["sucata_metal"] = inventario.get("sucata_metal", 0) + 4
            return {"ouro": ouro_atual, "beneficio": "item_tier2", "detalhe": "+4 sucata_metal (tier 2)"}
        inventario["sucata_metal"] = inventario.get("sucata_metal", 0) + 2
        return {"ouro": ouro_atual, "beneficio": "item", "detalhe": "+2 sucata_metal (tier 1)"}

    if faccao_id == "circulo_arcano":
        if reputacao >= 20:
            novo_ouro = ouro_atual + 80
            return {"ouro": novo_ouro, "beneficio": "ouro_tier2", "detalhe": "+80 ouro (tier 2)"}
        novo_ouro = ouro_atual + 40
        return {"ouro": novo_ouro, "beneficio": "ouro", "detalhe": "+40 ouro (tier 1)"}

    return {"ouro": ouro_atual, "beneficio": "nenhum", "detalhe": "Facção sem benefício configurado"}



def gerar_cadeia_contratos(tier_maximo: str = "ouro", tamanho: int = 3) -> list[dict]:
    """Gera uma sequência curta de contratos para criar mini-arcos de progressão."""
    cadeia: list[dict] = []
    for _ in range(max(1, tamanho)):
        cadeia.append(gerar_contrato_aleatorio(tier_maximo))
    return cadeia


def progresso_cadeia(resolvidos: int, tamanho_total: int) -> str:
    if tamanho_total <= 0:
        return "Sem cadeia ativa."
    if resolvidos >= tamanho_total:
        return "Cadeia concluída."
    return f"Etapa {resolvidos + 1}/{tamanho_total}"



def avaliar_tensao_faccoes(reputacoes: dict[str, int]) -> dict:
    """Calcula tensão entre as duas facções mais influentes no momento."""
    if len(reputacoes) < 2:
        return {"status": "neutro", "rivalidade": [], "efeito_ouro": 0}

    ranking = sorted(reputacoes.items(), key=lambda kv: kv[1], reverse=True)
    (f1, r1), (f2, r2) = ranking[0], ranking[1]
    delta = abs(r1 - r2)

    if delta <= 2:
        return {"status": "conflito", "rivalidade": [f1, f2], "efeito_ouro": -10}
    if delta <= 6:
        return {"status": "competicao", "rivalidade": [f1, f2], "efeito_ouro": 0}
    return {"status": "hegemonia", "rivalidade": [f1, f2], "efeito_ouro": 10}



def gerar_crise_urbana(tensao: dict, clima: str) -> dict:
    """Gera uma crise urbana simples baseada em tensão política e clima."""
    status = tensao.get("status", "competicao")

    if status == "conflito":
        if clima == "tempestade_arcana":
            return {"tipo": "saques_arcanos", "gravidade": "alta", "impacto_ouro": -20}
        return {"tipo": "motim_local", "gravidade": "media", "impacto_ouro": -12}

    if status == "hegemonia":
        return {"tipo": "reforma_civica", "gravidade": "baixa", "impacto_ouro": 8}

    if clima == "chuvoso":
        return {"tipo": "alagamento_comercial", "gravidade": "media", "impacto_ouro": -6}

    return {"tipo": "estabilidade_vigiada", "gravidade": "baixa", "impacto_ouro": 0}
