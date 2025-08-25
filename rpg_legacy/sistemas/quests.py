from typing import TYPE_CHECKING, List, Dict, Any
from ..entidades.quest import Quest, EstadoQuest
from ..dados.quests_ato1 import QUESTS_ATO1 # Por enquanto, só do ato 1
from ..utilitarios import funcoes_gerais, narrador

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

# Um registro central de todas as quests para fácil acesso
TODAS_AS_QUESTS = {}
TODAS_AS_QUESTS.update(QUESTS_ATO1)

def iniciar_quest(jogador: 'Personagem', id_quest: str):
    """Inicia uma nova quest para o jogador, se ele cumprir os requisitos."""
    if id_quest in [q.id_quest for q in jogador.quests_ativas] or id_quest in jogador.quests_concluidas:
        # narrador.narrar("Você já iniciou esta jornada.")
        return

    dados_quest = TODAS_AS_QUESTS.get(id_quest)
    if not dados_quest:
        print(f"ALERTA: Quest com ID '{id_quest}' não encontrada.")
        return

    # Verificar pré-requisitos
    pre_requisitos = dados_quest.get("pre_requisitos", [])
    for pre_req_id in pre_requisitos:
        if pre_req_id not in jogador.quests_concluidas:
            # narrador.narrar("Você ainda não está pronto para esta tarefa.")
            return

    # Criar e iniciar a quest
    nova_quest = Quest(id_quest=id_quest, **dados_quest)
    nova_quest.iniciar()
    jogador.quests_ativas.append(nova_quest)

def concluir_quest(jogador: 'Personagem', quest: 'Quest'):
    """Finaliza uma quest, move para concluídas e entrega as recompensas."""
    if quest.concluir(jogador):
        jogador.quests_ativas.remove(quest)
        jogador.quests_concluidas.append(quest.id_quest)

        narrador.narrar(f"Missão '{quest.titulo}' concluída!")

        # Entregar recompensas
        recompensas = quest.recompensas
        if "xp" in recompensas:
            jogador.ganhar_xp(recompensas["xp"])
        if "ouro" in recompensas:
            jogador.ouro += recompensas["ouro"]
            narrador.narrar(f"Você recebeu {recompensas['ouro']} de ouro.")

        itens_recompensa = recompensas.get("itens", [])
        if itens_recompensa:
            narrador.narrar("Você recebeu os seguintes itens:")
            for item_info in itens_recompensa:
                jogador.adicionar_item(item_info["id_item"], item_info["quantidade"])
    else:
        narrador.narrar("Você ainda não completou todos os objetivos desta missão.")


def atualizar_progresso_quests(jogador: 'Personagem', tipo_evento: str, id_alvo: str):
    """
    Chamado sempre que um evento relevante para quests acontece (ex: matar monstro).
    """
    for quest in jogador.quests_ativas:
        quest.atualizar_progresso(tipo_evento, id_alvo)
        # Verificar se a quest pode ser concluída
        if quest.esta_completa():
            narrador.narrar(f"Você completou todos os objetivos da missão: '{quest.titulo}'!")
            # A conclusão real acontece ao falar com o NPC.

def exibir_journal(jogador: 'Personagem'):
    """Exibe o diário de missões do jogador."""
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Diário de Missões", nivel=1)

    print("\n--- Missões Ativas ---")
    if not jogador.quests_ativas:
        print("Nenhuma missão ativa.")
    else:
        for quest in jogador.quests_ativas:
            print(f"\n[{quest.tipo.value}] {quest.titulo}")
            for obj in quest.objetivos:
                print(f"  - {obj['descricao']} ({obj['progresso']}/{obj['total']})")

    print("\n--- Missões Concluídas ---")
    if not jogador.quests_concluidas:
        print("Nenhuma missão concluída.")
    else:
        for id_quest in jogador.quests_concluidas:
            quest = TODAS_AS_QUESTS.get(id_quest)
            if quest:
                print(f"- {quest['titulo']}")

    funcoes_gerais.pausar()
