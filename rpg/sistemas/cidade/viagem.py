"""Sistema de consulta e viagem entre cidades/reinos do mundo."""

from ...dados.cidades_reinos import CIDADES_REINOS


def preparar_viagem_cidade(jogador):
    """Retorna seleção de cidades disponíveis para viagem rápida."""
    return {
        "tipo": "selecao",
        "prompt": "Escolha seu destino:",
        "opcoes": list(CIDADES_REINOS.keys()),
        "acao_prefixo": "viajar_cidade",
        "log": [],
    }


def viajar_para_cidade(jogador, id_cidade: str):
    """Atualiza localização atual do personagem."""
    if id_cidade not in CIDADES_REINOS:
        return {"tipo": "feedback", "log": ["Destino inválido."]}

    dados = CIDADES_REINOS[id_cidade]
    jogador.cidade_atual = id_cidade
    jogador.reino_atual = dados.get("reino")
    return {"tipo": "feedback", "log": [f"Você viajou para {dados['nome']} ({dados['reino']})."]}


def resumo_cidades_reinos():
    """Resumo textual para UI/depuração do catálogo de locais."""
    return [f"{cid}: {dados['nome']} [{dados['reino']}]" for cid, dados in CIDADES_REINOS.items()]
