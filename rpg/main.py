import random
from typing import TYPE_CHECKING

# Importação dos módulos do projeto
from .entidades.personagem import Personagem
from .entidades.monstro import Monstro
from .io import menu, criacao_personagem, salvar_carregar
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
        loot_table=loot_table,
        comportamento_ia=dados_monstro.get("comportamento_ia", "agressivo")
    )


# --- Loops de Jogo ---

def jogar(jogador: 'Personagem'):
    """O loop principal de gameplay para um personagem ativo."""
    # Inicia a primeira quest automaticamente para dar um ponto de partida ao jogador
    quests.iniciar_quest(jogador, "mq01_despertar")

    while jogador.esta_vivo():
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("Vila de Valesereno", nivel=2)
        print("Você está no centro da pequena e tranquila vila de Valesereno.")
        print("\nO que você faz?")
        print("1. Falar com Elara (Curandeira da Vila)")
        print("2. Explorar a Floresta dos Sussurros")
        print("3. Ver Diário de Missões")
        print("4. Ver status do personagem")
        print("5. Salvar Jogo")
        print("6. Sair para o Menu Principal")

        escolha = input("\nSua escolha: ")

        if escolha == '1': # Falar com Elara
            narrador.narrar("Você se aproxima de Elara, a curandeira local. Ela sorri calorosamente.")

            # Lógica para a quest mq01: Falar com Elara para completá-la
            quest_despertar = next((q for q in jogador.quests_ativas if q.id_quest == "mq01_despertar"), None)
            if quest_despertar:
                quests.atualizar_progresso_quests(jogador, "falar_com", "elara_curandeira")
                if quest_despertar.esta_completa():
                    quests.concluir_quest(jogador, quest_despertar)

            # Lógica para a quest mq02: Pegar e entregar
            if "mq01_despertar" in jogador.quests_concluidas:
                quests.iniciar_quest(jogador, "mq02_ameaca_local")

            quest_ameaca = next((q for q in jogador.quests_ativas if q.id_quest == "mq02_ameaca_local"), None)
            if quest_ameaca and quest_ameaca.esta_completa():
                quests.concluir_quest(jogador, quest_ameaca)
                quests.iniciar_quest(jogador, "mq03_primeira_sombra")

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

        elif escolha == '3': # Diário de Missões
            quests.exibir_journal(jogador)

        elif escolha == '4': # Status
            funcoes_gerais.limpar_tela()
            funcoes_gerais.imprimir_cabecalho("Status do Personagem", nivel=2)
            print(jogador)
            funcoes_gerais.pausar()

        elif escolha == '5': # Salvar
            nome_save = input("Digite o nome para o seu save: ").strip()
            if nome_save:
                salvar_carregar.salvar_jogo(jogador, nome_save)
            else:
                print("Nome de save inválido.")
            funcoes_gerais.pausar()

        elif escolha == '6': # Sair
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
