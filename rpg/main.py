import random
from typing import TYPE_CHECKING

# Importação dos módulos do projeto
from .entidades.personagem import Personagem
from .entidades.monstro import Monstro
from .io import menu, criacao_personagem, salvar_carregar, menu_inventario, menu_equipamento
from .sistemas import combate, quests
from .utilitarios import funcoes_gerais, narrador
from .dados.monstros_area1 import MONSTROS_AREA1

if TYPE_CHECKING:
    from .entidades.personagem import Personagem

# --- Fábricas de Entidades (Funções de Ajuda) ---

def criar_monstro_por_id(id_monstro: str) -> Monstro:
    """Cria uma instância de Monstro a partir dos dados do dicionário."""
    dados_monstro = MONSTROS_AREA1.get(id_monstro)
    if not dados_monstro:
        raise ValueError(f"Monstro com ID '{id_monstro}' não encontrado.")

    habilidades = dados_monstro.get("habilidades", [])
    ataques_base = dados_monstro.get("ataques_base_ids", [])
    loot_table = dados_monstro.get("loot_table", [])

    return Monstro(
        id_monstro=id_monstro,
        nome=dados_monstro["nome"],
        nivel=dados_monstro["nivel"],
        familia=dados_monstro["familia"],
        xp_recompensa=dados_monstro["xp_recompensa"],
        ouro_recompensa=dados_monstro["ouro_recompensa"],
        stats_base=dados_monstro["stats_base"],
        habilidades_ids=habilidades,
        ataques_base_ids=ataques_base,
        loot_table=loot_table,
        comportamento_ia=dados_monstro.get("comportamento_ia", "agressivo")
    )


# --- Loops de Jogo ---

def jogar(jogador: 'Personagem'):
    """O loop principal de gameplay para um personagem ativo."""
    while jogador.esta_vivo():
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("Vila de Valesereno", nivel=2)
        print("Você está no centro da pequena e tranquila vila de Valesereno.")
        print("\nO que você faz?")
        print("1. Falar com Elara (Curandeira da Vila)")
        print("2. Explorar a Floresta dos Sussurros")
        print("3. Viajar")
        print("4. Ver Diário de Missões")
        print("5. Abrir Inventário")
        print("6. Ver Equipamento")
        print("7. Ver status do personagem")
        print("8. Salvar Jogo")
        print("9. Sair para o Menu Principal")

        escolha = input("\nSua escolha: ")

        if escolha == '1': # Falar com Elara
            narrador.narrar("Você se aproxima de Elara, a curandeira local. Ela sorri calorosamente.")

            # --- Lógica de Diálogo com Elara baseada no estado das quests ---

            # Checa se a quest "despertar" está ativa
            quest_despertar = next((q for q in jogador.quests_ativas if q.id_quest == "mq01_despertar"), None)
            # Checa se a quest da ameaça está ativa
            quest_ameaca = next((q for q in jogador.quests_ativas if q.id_quest == "mq02_ameaca_local"), None)

            # Caso 1: Primeira interação, nenhuma quest principal foi iniciada.
            if not quest_despertar and "mq01_despertar" not in jogador.quests_concluidas:
                narrador.narrar("'Que bom que você acordou! Você estava desmaiado na floresta. Como se sente?'")
                quests.iniciar_quest(jogador, "mq01_despertar")

            # Caso 2: Jogador está na quest "despertar" e fala com ela para completar.
            elif quest_despertar and not quest_despertar.esta_completa():
                quests.atualizar_progresso_quests(jogador, "falar_com", "elara_curandeira")
                if quest_despertar.esta_completa():
                    quests.concluir_quest(jogador, quest_despertar)
                    # Imediatamente oferece a próxima quest
                    narrador.narrar("'Fico feliz que esteja se recuperando. Na verdade, preciso de um favor...'")
                    quests.iniciar_quest(jogador, "mq02_ameaca_local")

            # Caso 3: Jogador completou a quest dos goblins e retorna para Elara.
            elif quest_ameaca and quest_ameaca.esta_completa():
                quests.concluir_quest(jogador, quest_ameaca)
                # Imediatamente oferece a próxima quest
                narrador.narrar("'Não acredito que você conseguiu! A vila está em dívida com você. Mas ao derrotá-los, você encontrou algo estranho...'")
                quests.iniciar_quest(jogador, "mq03_primeira_sombra")

            # Caso 4: Diálogo padrão se nenhuma condição de quest for atendida.
            else:
                narrador.narrar("'É bom ver você bem. Cuidado lá fora.'")

            # Oferecer cura se o jogador não estiver com HP ou MP no máximo
            if jogador.hp_atual < jogador.hp_max or jogador.mp_atual < jogador.mp_max:
                narrador.narrar("\n'Você parece cansado. Deixe-me restaurar suas energias.'")
                confirmar_cura = input("Aceitar a cura? (s/n): ").lower().strip()
                if confirmar_cura == 's':
                    jogador.hp_atual = jogador.hp_max
                    jogador.mp_atual = jogador.mp_max
                    narrador.narrar("Você se sente revigorado! HP e MP totalmente restaurados.")

            funcoes_gerais.pausar()

        elif escolha == '2': # Explorar
            if random.random() < 0.75:
                id_monstro_encontrado = random.choice(list(MONSTROS_AREA1.keys()))
                monstro = criar_monstro_por_id(id_monstro_encontrado)
                vitoria = combate.iniciar_batalha(jogador, [monstro])
                if vitoria:
                    quests.atualizar_progresso_quests(jogador, "matar", id_monstro_encontrado)
            else:
                narrador.narrar("\nVocê explora a floresta, mas não encontra nada de interessante, apenas o som do vento nas árvores.")
            funcoes_gerais.pausar()

        elif escolha == '3': # Viajar
            narrador.narrar("Você olha para as estradas que saem de Valesereno, mas ainda não se sente pronto ou não sabe para onde ir. Melhor continuar explorando a área local por enquanto.")
            funcoes_gerais.pausar()

        elif escolha == '4': # Diário de Missões
            quests.exibir_journal(jogador)

        elif escolha == '5': # Inventário
            menu_inventario.exibir_inventario(jogador)

        elif escolha == '6': # Equipamento
            menu_equipamento.exibir_equipamento(jogador)

        elif escolha == '7': # Status
            funcoes_gerais.limpar_tela()
            funcoes_gerais.imprimir_cabecalho("Status do Personagem", nivel=2)
            print(jogador)
            funcoes_gerais.pausar()

        elif escolha == '8': # Salvar
            nome_save = input("Digite o nome para o seu save: ").strip()
            if nome_save:
                salvar_carregar.salvar_jogo(jogador, nome_save)
            else:
                print("Nome de save inválido.")
            funcoes_gerais.pausar()

        elif escolha == '9': # Sair
            print("\nVoltando ao menu principal...")
            funcoes_gerais.pausar()
            break

        else:
            print("\nEscolha inválida.")
            funcoes_gerais.pausar()

    if not jogador.esta_vivo():
        funcoes_gerais.imprimir_cabecalho("FIM DE JOGO", nivel=1)
        print("Sua jornada termina aqui, mas seu legado pode continuar...")
        funcoes_gerais.pausar()


def main():
    """O loop principal do jogo, que gerencia os menus."""
    while True:
        escolha_menu = menu.exibir_menu_principal()

        if escolha_menu == "novo_jogo":
            jogador_ativo = criacao_personagem.iniciar_criacao_personagem()
            jogar(jogador_ativo)

        elif escolha_menu == "carregar_jogo":
            nome_save = menu.menu_carregar_jogo()
            if nome_save:
                jogador_ativo = salvar_carregar.carregar_jogo(nome_save)
                if jogador_ativo:
                    jogar(jogador_ativo)

        elif escolha_menu == "sair":
            funcoes_gerais.limpar_tela()
            print("\nObrigado por jogar!\n")
            break

if __name__ == "__main__":
    main()
