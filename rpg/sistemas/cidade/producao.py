"""Configuração de produção automática e validações de plano."""
from ...dados.cidade.producao import PLANOS_PRODUCAO


def preparar_configuracao_producao(jogador):
    if "automacao_coleta" not in jogador.estruturas_construidas:
        return {"tipo": "feedback", "log": ["Ative a Automação de Coleta antes de configurar a produção."]}

    estruturas = getattr(jogador, "estruturas_construidas", set())
    opcoes_disponiveis = []
    for id_plano, dados in PLANOS_PRODUCAO.items():
        estrutura_necessaria = dados.get("estrutura_necessaria")
        if not estrutura_necessaria or estrutura_necessaria in estruturas:
            opcoes_disponiveis.append(id_plano)

    return {
        "tipo": "selecao",
        "prompt": "Escolha o plano de produção automática:",
        "opcoes": opcoes_disponiveis,
    return {
        "tipo": "selecao",
        "prompt": "Escolha o plano de produção automática:",
        "opcoes": list(PLANOS_PRODUCAO.keys()),
        "acao_prefixo": "definir_plano_producao",
        "log": [],
    }


def definir_plano_producao(jogador, id_plano: str):
    if id_plano not in PLANOS_PRODUCAO:
        return {"tipo": "feedback", "log": ["Plano de produção desconhecido."]}

    jogador.plano_producao_ativo = id_plano
    return {"tipo": "feedback", "log": [f"Plano de produção definido para '{id_plano}'."]}
