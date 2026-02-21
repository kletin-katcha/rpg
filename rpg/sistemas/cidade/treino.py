from ...io import criacao_personagem as cc_api
from ...dados.cidade.treino_classes import CUSTO_TREINO_CLASSE_SECUNDARIA, NIVEL_MINIMO_CLASSE_SECUNDARIA
from ...dados.cidade import dialogos
from .validators import (
    tem_ouro_suficiente,
    tem_nivel_suficiente,
    ja_tem_classe_secundaria,
    tem_classe_principal,
)


def preparar_treino_classe_secundaria(jogador):
    if ja_tem_classe_secundaria(jogador):
        return {"tipo": "feedback", "log": [dialogos.MENSAGEM_CLASSE_SECUNDARIA_BLOQUEADA.format(classe=jogador.classe_secundaria)]}

    if not tem_classe_principal(jogador):
        return {"tipo": "feedback", "log": [dialogos.MENSAGEM_SEM_CLASSE_PRINCIPAL]}

    if not tem_nivel_suficiente(jogador, NIVEL_MINIMO_CLASSE_SECUNDARIA):
        return {"tipo": "feedback", "log": [dialogos.MENSAGEM_SEM_NIVEL.format(nivel=NIVEL_MINIMO_CLASSE_SECUNDARIA)]}

    if not tem_ouro_suficiente(jogador, CUSTO_TREINO_CLASSE_SECUNDARIA):
        return {"tipo": "feedback", "log": [dialogos.MENSAGEM_SEM_OURO.format(custo=CUSTO_TREINO_CLASSE_SECUNDARIA)]}

    classes_disponiveis = cc_api.get_classes_secundarias_disponiveis(jogador.classe)
    if not classes_disponiveis:
        return {"tipo": "feedback", "log": [dialogos.MENSAGEM_SEM_OPCOES]}

    return {
        "tipo": "selecao",
        "prompt": f"Escolha sua classe secundária (custo: {CUSTO_TREINO_CLASSE_SECUNDARIA} ouro):",
        "opcoes": classes_disponiveis,
        "acao_prefixo": "treinar_classe_secundaria",
        "log": [],
    }


def executar_treino_classe_secundaria(jogador, id_classe: str):
    if ja_tem_classe_secundaria(jogador):
        return {"tipo": "feedback", "log": ["Você já possui classe secundária."]}

    if not tem_ouro_suficiente(jogador, CUSTO_TREINO_CLASSE_SECUNDARIA):
        return {"tipo": "feedback", "log": ["Ouro insuficiente para o treinamento."]}

    try:
        cc_api.aplicar_classe_secundaria(jogador, id_classe)
    except ValueError as erro:
        return {"tipo": "feedback", "log": [f"Falha no treinamento: {erro}"]}

    jogador.ouro -= CUSTO_TREINO_CLASSE_SECUNDARIA
    return {"tipo": "feedback", "log": [dialogos.MENSAGEM_TREINO_SUCESSO.format(classe=id_classe)]}
