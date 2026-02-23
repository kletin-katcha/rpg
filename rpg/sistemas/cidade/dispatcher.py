"""Dispatcher das ações especiais de cidade e respostas contextuais."""
from .treino import preparar_treino_classe_secundaria, executar_treino_classe_secundaria
from .forja import executar_forja_prototipo, executar_forja_machadinha, executar_forja_machado_batalha, executar_forja_receita_avancada
from .construcao import construir_estrutura
from .melhorias import melhorar_estrutura
from .producao import preparar_configuracao_producao, definir_plano_producao
from .viagem import preparar_viagem_cidade, viajar_para_cidade, resumo_cidades_reinos
from .treino import preparar_treino_classe_secundaria, executar_treino_classe_secundaria
from .forja import executar_forja_prototipo, executar_forja_machadinha
from .construcao import construir_estrutura
from .melhorias import melhorar_estrutura
from .producao import preparar_configuracao_producao, definir_plano_producao
from ...sistemas.automacao import processar_ciclo_automatizado


def executar_opcao_especial_cidade(jogador, opcao: str):
    if opcao == "Treinar Classe Secundária (Protótipo)":
        return preparar_treino_classe_secundaria(jogador)
    if opcao == "Usar Forja (Protótipo)":
        return executar_forja_prototipo(jogador)
    if opcao == "Construir Oficina (Protótipo)":
        return construir_estrutura(jogador, "oficina_basica")
    if opcao == "Melhorar Oficina (Protótipo)":
        return melhorar_estrutura(jogador, "oficina_basica")
    if opcao == "Ativar Automação de Coleta (Protótipo)":
        return construir_estrutura(jogador, "automacao_coleta")
    if opcao == "Construir Laboratório Alquímico (Protótipo)":
        return construir_estrutura(jogador, "laboratorio_alquimico")
    if opcao == "Ativar Automação de Refino (Protótipo)":
        return construir_estrutura(jogador, "automacao_refino")
    if opcao == "Configurar Produção Automática (Protótipo)":
        return preparar_configuracao_producao(jogador)
    if opcao == "Forjar Machado de Batalha (Protótipo)":
        return executar_forja_machado_batalha(jogador)
    if opcao == "Ver mapa de cidades/reinos":
        return {"tipo": "feedback", "log": resumo_cidades_reinos()}
    if opcao == "Viajar para outra cidade (Protótipo)":
        return preparar_viagem_cidade(jogador)
    if opcao == "Configurar Produção Automática (Protótipo)":
        return preparar_configuracao_producao(jogador)
    if opcao == "Avançar 1 dia (Protótipo)":
        return {"tipo": "feedback", "log": processar_ciclo_automatizado(jogador)}
    return None


def executar_acao_contextual_cidade(jogador, acao: str):
    if acao == "forjar_machadinha":
        return executar_forja_machadinha(jogador)
    if acao == "forjar_machado_batalha":
        return executar_forja_machado_batalha(jogador)

    if acao.startswith("acao_forja:"):
        forja_acao = acao.split(":", 1)[1]
        if forja_acao == "forjar_machadinha":
            return executar_forja_machadinha(jogador)
        if forja_acao == "forjar_machado_batalha":
            return executar_forja_machado_batalha(jogador)
        if forja_acao == "forjar_espada_longa_avancada":
            return executar_forja_receita_avancada(jogador, "espada_longa_reciclada")
        if forja_acao == "forjar_peitoral_avancado":
            return executar_forja_receita_avancada(jogador, "peitoral_reciclado")

    if acao.startswith("treinar_classe_secundaria:"):
        id_classe = acao.split(":", 1)[1]
        return executar_treino_classe_secundaria(jogador, id_classe)

    if acao.startswith("definir_plano_producao:"):
        id_plano = acao.split(":", 1)[1]
        return definir_plano_producao(jogador, id_plano)

    if acao.startswith("viajar_cidade:"):
        id_cidade = acao.split(":", 1)[1]
        return viajar_para_cidade(jogador, id_cidade)

    return None
