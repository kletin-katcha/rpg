from rpg.game_manager import GameManager
from rpg.utilitarios import funcoes_gerais

# Este arquivo é o novo ponto de entrada para a versão de texto do jogo.
# Ele atua como um "cliente" para o GameManager, que contém toda a lógica.

def exibir_menu_numerado(opcoes: list[str]):
    """Exibe uma lista de opções numeradas."""
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")

def main_loop():
    """O loop principal do cliente de console."""
    gm = GameManager()

    while gm.is_running:
        funcoes_gerais.limpar_tela()

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

        elif gm.game_state == "in_game":
            funcoes_gerais.imprimir_cabecalho("Vila de Valesereno")
            print("Você está no centro da pequena e tranquila vila de Valesereno.")

            # Exibe o log de eventos, se houver
            for log_entry in gm.game_log:
                print(log_entry)

            print("\nO que você faz?")
            opcoes = gm.get_opcoes_cidade()
            exibir_menu_numerado(opcoes)

            escolha = input("\nSua escolha: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                resultado = gm.executar_opcao_cidade(opcoes[int(escolha) - 1])
                # A UI gráfica usaria o `resultado` para decidir o que fazer.
                # Aqui, nós apenas pausamos para o jogador ver o log.
                funcoes_gerais.pausar()
            else:
                print("Opção inválida.")
                funcoes_gerais.pausar()

        # TODO: Adicionar elif para gm.game_state == "combat"
        elif gm.game_state == "character_creation":
            # Lida com o fluxo de criação de personagem
            dados_criacao = gm.get_dados_criacao_personagem()
            step = dados_criacao.get("step")

            funcoes_gerais.imprimir_cabecalho(f"Criação de Personagem: {step.capitalize()}", nivel=2)

            if step == "nome":
                nome = input(dados_criacao.get("prompt", "Digite o nome: "))
                gm.processar_acao_criacao({"nome": nome})

            elif step == "raca":
                racas = dados_criacao.get("opcoes", {})
                racas_list = list(racas.items())
                print("Escolha sua raça:")
                for i, (id_raca, raca_data) in enumerate(racas_list, 1):
                    print(f"{i}. {raca_data['nome']}")
                escolha = input("> ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(racas_list):
                    id_raca_escolhida = racas_list[int(escolha) - 1][0]
                    gm.processar_acao_criacao({"id_raca": id_raca_escolhida})
                else:
                    print("Seleção inválida.")
                    funcoes_gerais.pausar()

            elif step == "classe":
                classes = dados_criacao.get("opcoes", {})
                classes_list = list(classes.items())
                print("Escolha sua classe:")
                for i, (id_classe, classe_data) in enumerate(classes_list, 1):
                    print(f"{i}. {classe_data['nome']}")
                escolha = input("> ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(classes_list):
                    id_classe_escolhida = classes_list[int(escolha) - 1][0]
                    gm.processar_acao_criacao({"id_classe": id_classe_escolhida})
                else:
                    print("Seleção inválida.")
                    funcoes_gerais.pausar()

            elif step == "atributos":
                pontos_restantes = dados_criacao.get("pontos", 0)
                personagem = dados_criacao.get("personagem")
                print(f"Você tem {pontos_restantes} pontos para distribuir.")
                # Lógica simplificada para o cliente de console: distribui tudo em força
                print("Distribuindo 10 em Força e 10 em Constituição...")
                pontos_distribuidos = {"forca": 10, "constituicao": 10}
                gm.processar_acao_criacao({"pontos": pontos_distribuidos})
                print("Criação de personagem concluída!")
                funcoes_gerais.pausar()

        elif gm.game_state == "combat":
            funcoes_gerais.imprimir_cabecalho("Combate!", nivel=2)
            estado_combate = gm.get_estado_combate()
            jogador = estado_combate["jogador"]
            inimigos = estado_combate["inimigos"]

            # Exibir status
            print(f"{jogador.nome}: {jogador.hp_atual}/{jogador.hp_max} HP | {jogador.mp_atual}/{jogador.mp_max} MP | {jogador.stamina_atual}/{jogador.stamina_max} Vigor")
            for inimigo in inimigos:
                if inimigo.esta_vivo():
                    print(f"{inimigo.nome}: {inimigo.hp_atual}/{inimigo.hp_max} HP")
            print("-" * 20)

            # Exibir log de combate
            for log_entry in gm.game_log:
                print(log_entry)

            # Obter e executar ação do jogador
            print("\nO que você faz?")
            opcoes_combate = gm.get_opcoes_combate()
            exibir_menu_numerado(opcoes_combate)
            escolha = input("> ")

            # Lógica simplificada para o cliente de console: sempre ataca com o primeiro ataque básico
            from rpg.dados.ataques_base import ATAQUES_BASE
            acao_jogador = {"tipo": "ataque_basico", "ataque": ATAQUES_BASE["soco"], "alvo": inimigos[0]}

            print(f"Você escolheu atacar o {inimigos[0].nome}!")
            funcoes_gerais.pausar()

            gm.executar_turno_combate(acao_jogador)


    print("\nObrigado por jogar!")

if __name__ == "__main__":
    main_loop()
