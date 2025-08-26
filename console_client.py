from rpg.game_manager import GameManager
from rpg.utilitarios import funcoes_gerais
from rpg.io import console_ui, menu_inventario, menu_equipamento
from rpg.sistemas import quests

def exibir_menu_numerado(opcoes: list[str]):
    """Exibe uma lista de opções numeradas."""
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")

def main_loop():
    """O loop principal do cliente de console."""
    gm = GameManager()

    while gm.is_running:
        funcoes_gerais.limpar_tela()

        # Exibe o log de eventos do turno/ação anterior
        for log_entry in gm.game_log:
            print(f">> {log_entry}")
        if gm.game_log: print("-" * 20)
        gm.clear_log()

        if gm.game_state == "main_menu":
            funcoes_gerais.imprimir_cabecalho("RPG TEXTUAL COLOSSAL")
            opcoes = gm.get_opcoes_menu_principal()
            exibir_menu_numerado(opcoes)
            escolha = input("\nEscolha uma opção: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                gm.executar_opcao_menu_principal(opcoes[int(escolha) - 1])
            else:
                print("Opção inválida.")
                funcoes_gerais.pausar()

        elif gm.game_state == "character_creation":
            gm.jogador = console_ui.criar_novo_personagem_ui()
            gm.game_state = "in_game" # Transição para o jogo principal

        elif gm.game_state == "in_game":
            funcoes_gerais.imprimir_cabecalho(f"Local: {gm.localizacao_atual.capitalize()}")
            opcoes = gm.get_opcoes_localizacao()
            exibir_menu_numerado(opcoes)

            escolha = input("\nSua escolha: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                opcao_escolhida = opcoes[int(escolha) - 1]

                # Lógica para menus que abrem telas inteiras e pausam o fluxo
                if opcao_escolhida == "Abrir Inventário":
                    menu_inventario.exibir_inventario(gm.jogador)
                elif opcao_escolhida == "Ver Equipamento":
                    menu_equipamento.exibir_equipamento(gm.jogador)
                elif opcao_escolhida == "Ver Diário de Missões":
                    # Supondo que exista uma função para exibir o diário
                    # quests.exibir_diario(gm.jogador)
                    print("Diário de missões ainda não implementado.")
                    funcoes_gerais.pausar()
                elif opcao_escolhida == "Ver status do personagem":
                    print(gm.jogador)
                    funcoes_gerais.pausar()
                elif "Distribuir Pontos de Atributo" in opcao_escolhida:
                    console_ui.distribuir_pontos_levelup_ui(gm.jogador)
                else:
                    gm.executar_opcao_localizacao(opcao_escolhida)
                    # Não pausa aqui para o log do GM ser exibido no topo do próximo loop
            else:
                print("Opção inválida.")
                funcoes_gerais.pausar()

        elif gm.game_state == "combat":
            funcoes_gerais.imprimir_cabecalho("Combate!")

            # Exibir status
            jogador = gm.combat_state["jogador"]
            inimigos = gm.combat_state["inimigos"]
            print(f"{jogador.nome}: {jogador.hp_atual}/{jogador.hp_max} HP")
            for inimigo in inimigos:
                if inimigo.esta_vivo():
                    print(f"{inimigo.nome}: {inimigo.hp_atual}/{inimigo.hp_max} HP")
            print("-" * 20)

            combatente_atual = gm.get_combatente_atual()
            print(f"É o turno de {combatente_atual.nome}.")

            if combatente_atual == gm.jogador:
                acao = loop_acao_jogador_console(gm)
                if acao:
                    gm.executar_turno_combate(acao)
                else:
                    continue # Permite que o jogador tente uma nova ação se cancelou
            else: # Turno do monstro
                funcoes_gerais.pausar() # Pausa para o jogador ver o que o monstro vai fazer
                gm.executar_turno_combate(None) # O GM vai chamar decidir_acao do monstro

def loop_acao_jogador_console(gm: GameManager) -> dict:
    """Função auxiliar para obter a ação do jogador no console durante o combate."""
    print("\nO que você faz?")
    opcoes = gm.get_opcoes_combate()
    exibir_menu_numerado(opcoes)
    escolha_str = input("> ")

    if not escolha_str.isdigit() or not 1 <= int(escolha_str) <= len(opcoes):
        print("Ação inválida.")
        return None

    escolha_acao = opcoes[int(escolha_str) - 1]

    if escolha_acao == 'Atacar':
        inimigos = [i for i in gm.combat_state["inimigos"] if i.esta_vivo()]
        print("\nEscolha o alvo:")
        for i, inimigo in enumerate(inimigos, 1):
            print(f"{i}. {inimigo.nome}")
        escolha_alvo_str = input("> ")
        if escolha_alvo_str.isdigit() and 1 <= int(escolha_alvo_str) <= len(inimigos):
            alvo = inimigos[int(escolha_alvo_str) - 1]
            # Usando o primeiro ataque base como padrão por simplicidade
            ataque_base = gm.jogador.ataques_base[0]
            return {"tipo": "ataque_basico", "ataque": ataque_base, "alvo": alvo}

    elif escolha_acao == 'Habilidade':
        habilidades = gm.get_habilidades_ativas_jogador()
        if not habilidades:
            print("Você não tem habilidades para usar.")
            return None

        print("\nEscolha a habilidade:")
        for i, hab in enumerate(habilidades, 1):
            print(f"{i}. {hab['nome']}")
        escolha_hab_str = input("> ")
        if escolha_hab_str.isdigit() and 1 <= int(escolha_hab_str) <= len(habilidades):
            habilidade = habilidades[int(escolha_hab_str) - 1]

            alvo = None
            if habilidade['tipo_alvo'] == 'inimigo_unico':
                inimigos = [i for i in gm.combat_state["inimigos"] if i.esta_vivo()]
                print("\nEscolha o alvo:")
                for i, inimigo in enumerate(inimigos, 1):
                    print(f"{i}. {inimigo.nome}")
                escolha_alvo_str = input("> ")
                if escolha_alvo_str.isdigit() and 1 <= int(escolha_alvo_str) <= len(inimigos):
                    alvo = inimigos[int(escolha_alvo_str) - 1]
            elif habilidade['tipo_alvo'] == 'self':
                alvo = gm.jogador

            if alvo:
                return {"tipo": "usar_habilidade", "habilidade": habilidade, "alvo": alvo}

    # Implementar outras ações como Item, Defender, Fugir
    return None

if __name__ == "__main__":
    main_loop()
