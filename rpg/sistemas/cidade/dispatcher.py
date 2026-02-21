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
    if opcao == "Configurar Produção Automática (Protótipo)":
        return preparar_configuracao_producao(jogador)
    if opcao == "Avançar 1 dia (Protótipo)":
        return {"tipo": "feedback", "log": processar_ciclo_automatizado(jogador)}
    return None


def executar_acao_contextual_cidade(jogador, acao: str):
    if acao == "forjar_machadinha":
        return executar_forja_machadinha(jogador)

    if acao.startswith("treinar_classe_secundaria:"):
        id_classe = acao.split(":", 1)[1]
        return executar_treino_classe_secundaria(jogador, id_classe)

    if acao.startswith("definir_plano_producao:"):
        id_plano = acao.split(":", 1)[1]
        return definir_plano_producao(jogador, id_plano)

    return None
