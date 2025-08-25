from rpg.game_manager import GameManager
from rpg.utilitarios import funcoes_gerais
from rpg.io import menu_inventario, menu_equipamento
from rpg.sistemas import quests

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
                opcao_escolhida = opcoes[int(escolha) - 1]

                # Lógica especial para menus que abrem telas inteiras
                if opcao_escolhida == "Abrir Inventário":
                    menu_inventario.exibir_inventario(gm.jogador)
                elif opcao_escolhida == "Ver Equipamento":
                    menu_equipamento.exibir_equipamento(gm.jogador)
                elif opcao_escolhida == "Ver Diário de Missões":
                    quests.exibir_journal(gm.jogador)
                elif opcao_escolhida == "Ver status do personagem":
                    print(gm.jogador) # Usa o __str__ do personagem
                    funcoes_gerais.pausar()
                else:
                    # Para outras ações, usa o GameManager e exibe o log
                    resultado = gm.executar_opcao_cidade(opcao_escolhida)
                    for log_entry in resultado.get("log", []):
                        print(log_entry)

                    if resultado.get("tipo") == "pergunta":
                        resposta = input(f"\n{resultado.get('prompt', '')} ").lower().strip()
                        if resposta == 's':
                            resultado_contexto = gm.executar_acao_contextual(resultado.get("acao"))
                            for log_contexto in resultado_contexto.get("log", []):
                                print(log_contexto)

                    funcoes_gerais.pausar()
            else:
                print("Opção inválida.")
                funcoes_gerais.pausar()

        elif gm.game_state == "character_creation":
            # (O código de criação de personagem permanece o mesmo)
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
                raca_selecionada = False
                while not raca_selecionada:
                    funcoes_gerais.limpar_tela()
                    funcoes_gerais.imprimir_cabecalho("Escolha de Raça", nivel=2)
                    print("Escolha sua raça:")
                    for i, (id_raca, raca_data) in enumerate(racas_list, 1):
                        print(f"{i}. {raca_data['nome']}")

                    print("\nDigite o número de uma raça para ver detalhes, ou 'fim' para confirmar.")
                    escolha = input("> ").lower().strip()

                    if escolha == 'fim':
                        if gm.jogador.raca:
                            raca_selecionada = True
                        else:
                            print("Você deve primeiro selecionar uma raça.")
                            funcoes_gerais.pausar()
                        continue

                    try:
                        index = int(escolha) - 1
                        if 0 <= index < len(racas_list):
                            id_raca_escolhida, raca_data = racas_list[index]
                            funcoes_gerais.limpar_tela()
                            funcoes_gerais.imprimir_cabecalho(raca_data['nome'], nivel=3)
                            print(f"Descrição: {raca_data['descricao']}")
                            print("\n--- Modificadores de Atributos ---")
                            for stat, mod in raca_data['modificadores_stats'].items():
                                print(f"{stat.capitalize()}: {'+' if mod >= 0 else ''}{mod}")
                            print("\n--- Habilidades Raciais ---")
                            for hab in raca_data['habilidades_raciais']:
                                print(f"- {hab.replace('_', ' ').capitalize()}")

                            confirmar = input(f"\nDeseja escolher a raça {raca_data['nome']}? (s/n): ").lower().strip()
                            if confirmar == 's':
                                gm.processar_acao_criacao({"id_raca": id_raca_escolhida})
                                print(f"Você escolheu ser um(a) {raca_data['nome']}!")
                                funcoes_gerais.pausar()
                        else:
                            print("Número inválido.")
                            funcoes_gerais.pausar()
                    except ValueError:
                        print("Entrada inválida.")
                        funcoes_gerais.pausar()

            elif step == "classe":
                classes = dados_criacao.get("opcoes", {})
                classes_list = list(classes.items())
                classe_selecionada = False
                while not classe_selecionada:
                    funcoes_gerais.limpar_tela()
                    funcoes_gerais.imprimir_cabecalho("Escolha de Classe", nivel=2)
                    print("Escolha sua classe inicial:")
                    for i, (id_classe, classe_data) in enumerate(classes_list, 1):
                        print(f"{i}. {classe_data['nome']}")

                    print("\nDigite o número de uma classe para ver detalhes, ou 'fim' para confirmar.")
                    escolha = input("> ").lower().strip()

                    if escolha == 'fim':
                        if gm.jogador.classe:
                            classe_selecionada = True
                        else:
                            print("Você deve primeiro selecionar uma classe.")
                            funcoes_gerais.pausar()
                        continue

                    try:
                        index = int(escolha) - 1
                        if 0 <= index < len(classes_list):
                            id_classe_escolhida, classe_data = classes_list[index]
                            funcoes_gerais.limpar_tela()
                            funcoes_gerais.imprimir_cabecalho(classe_data['nome'], nivel=3)
                            print(f"Descrição: {classe_data['descricao']}")
                            print(f"\nAtributos Primários: {', '.join(classe_data['stats_primarios'])}")
                            print("\n--- Habilidades Iniciais ---")
                            for hab in classe_data['habilidades_iniciais']:
                                print(f"- {hab.replace('_', ' ').capitalize()}")

                            confirmar = input(f"\nDeseja escolher a classe {classe_data['nome']}? (s/n): ").lower().strip()
                            if confirmar == 's':
                                gm.processar_acao_criacao({"id_classe": id_classe_escolhida})
                                print(f"Você escolheu ser um(a) {classe_data['nome']}!")
                                funcoes_gerais.pausar()
                        else:
                            print("Número inválido.")
                            funcoes_gerais.pausar()
                    except ValueError:
                        print("Entrada inválida.")
                        funcoes_gerais.pausar()

            elif step == "atributos":
                pontos_para_distribuir = dados_criacao.get("pontos", 0)
                personagem = dados_criacao.get("personagem")
                pontos_distribuidos = {"forca": 0, "destreza": 0, "constituicao": 0, "inteligencia": 0, "sabedoria": 0, "carisma": 0}

                atributos = {
                    "1": "forca", "2": "destreza", "3": "constituicao",
                    "4": "inteligencia", "5": "sabedoria", "6": "carisma"
                }

                while pontos_para_distribuir > 0:
                    funcoes_gerais.limpar_tela()
                    funcoes_gerais.imprimir_cabecalho(f"Pontos Restantes: {pontos_para_distribuir}", nivel=3)
                    print("--- Atributos Atuais ---")
                    for i, key in atributos.items():
                        base_stat = getattr(personagem, 'base_' + key)
                        pontos_ja_add = pontos_distribuidos[key]
                        print(f"{i}. {key.capitalize():<13}: {base_stat + pontos_ja_add} ({base_stat} + {pontos_ja_add})")
                    print("------------------------")

                    escolha_attr = input("Digite o número do atributo para aumentar: ").lower().strip()
                    if escolha_attr not in atributos:
                        print("Escolha inválida.")
                        funcoes_gerais.pausar()
                        continue

                    attr_nome = atributos[escolha_attr]
                    try:
                        pontos_add = int(input(f"Quantos pontos para {attr_nome.capitalize()}? "))
                        if pontos_add <= 0:
                            print("Deve ser um número positivo.")
                        elif pontos_add > pontos_para_distribuir:
                            print("Pontos insuficientes.")
                        else:
                            pontos_distribuidos[attr_nome] += pontos_add
                            pontos_para_distribuir -= pontos_add
                    except ValueError:
                        print("Entrada inválida.")
                    funcoes_gerais.pausar()

                gm.processar_acao_criacao({"pontos": pontos_distribuidos})
                print("Criação de personagem concluída!")
                funcoes_gerais.pausar()

        elif gm.game_state == "combat":
            # O loop de combate agora é gerenciado aqui no cliente
            while gm.game_state == "combat":
                funcoes_gerais.limpar_tela()
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

                # Exibir log de combate do turno anterior
                for log_entry in gm.game_log:
                    print(log_entry)
                gm.clear_log() # Limpa o log para o próximo turno

                # Obter e executar ação do jogador
                acao_jogador = loop_acao_jogador_console(gm)
                if acao_jogador:
                    resultado_turno = gm.executar_turno_combate(acao_jogador)
                    # Adiciona o novo log ao log principal do GameManager
                    gm.game_log.extend(resultado_turno.get("log", []))
                else:
                    # O jogador cancelou ou a ação foi inválida, continue o loop para obter nova ação
                    continue

            # Pausa para o jogador ver o resultado final do combate (vitória/derrota)
            funcoes_gerais.pausar()

def loop_acao_jogador_console(gm: GameManager) -> dict:
    """
    Função auxiliar para obter a ação do jogador no console.
    Retorna o dicionário de ação ou None se o jogador cancelar.
    """
    print("\nO que você faz?")
    opcoes_combate = gm.get_opcoes_combate()
    exibir_menu_numerado(opcoes_combate)
    escolha_str = input("> ")

    if not escolha_str.isdigit() or not 1 <= int(escolha_str) <= len(opcoes_combate):
        print("Ação inválida ou cancelada.")
        funcoes_gerais.pausar()
        return None

    escolha_acao = opcoes_combate[int(escolha_str) - 1]

    if escolha_acao == 'Atacar':
        ataques = gm.jogador.ataques_base
        print("\nEscolha o ataque:")
        for i, ataque in enumerate(ataques, 1):
            print(f"{i}. {ataque['nome']}")
        print("0. Voltar")

        escolha_ataque_str = input("> ")
        if escolha_ataque_str.isdigit() and 1 <= int(escolha_ataque_str) <= len(ataques):
            ataque_escolhido = ataques[int(escolha_ataque_str) - 1]
            inimigos = [i for i in gm.combat_state["inimigos"] if i.esta_vivo()]
            print("\nEscolha o alvo:")
            for i, inimigo in enumerate(inimigos, 1):
                print(f"{i}. {inimigo.nome}")
            escolha_alvo_str = input("> ")
            if escolha_alvo_str.isdigit() and 1 <= int(escolha_alvo_str) <= len(inimigos):
                alvo_escolhido = inimigos[int(escolha_alvo_str) - 1]
                return {"tipo": "ataque_basico", "ataque": ataque_escolhido, "alvo": alvo_escolhido}

    elif escolha_acao == 'Habilidade':
        habilidades_disponiveis = gm.get_habilidades_ativas_jogador()

        if not habilidades_disponiveis:
            print("Você não tem nenhuma habilidade que possa usar.")
            funcoes_gerais.pausar()
            return None

        print("\nEscolha a habilidade:")
        for i, hab in enumerate(habilidades_disponiveis, 1):
            custo = hab.get('custo_valor', 0)
            tipo_custo = hab.get('custo_tipo', 'nenhum').upper()
            print(f"{i}. {hab['nome']} (Custo: {custo} {tipo_custo}) - {hab['descricao']}")
        print("0. Voltar")

        escolha_hab_str = input("> ")
        if escolha_hab_str.isdigit() and 1 <= int(escolha_hab_str) <= len(habilidades_disponiveis):
            habilidade_escolhida = habilidades_disponiveis[int(escolha_hab_str) - 1]

            alvo = None
            tipo_alvo_hab = habilidade_escolhida.get("tipo_alvo")

            if tipo_alvo_hab == "self":
                alvo = gm.jogador
            elif tipo_alvo_hab in ["inimigo_unico", "inimigos_area"]:
                inimigos = [i for i in gm.combat_state["inimigos"] if i.esta_vivo()]
                print("\nEscolha o alvo:")
                for i, inimigo in enumerate(inimigos, 1):
                    print(f"{i}. {inimigo.nome}")
                escolha_alvo_str = input("> ")
                if escolha_alvo_str.isdigit() and 1 <= int(escolha_alvo_str) <= len(inimigos):
                    alvo = inimigos[int(escolha_alvo_str) - 1]
            # TODO: Adicionar lógica para alvos aliados

            if alvo:
                return {"tipo": "usar_habilidade", "habilidade": habilidade_escolhida, "alvo": alvo}

    elif escolha_acao == 'Defender':
        return {"tipo": "defender"}

    elif escolha_acao == 'Item':
        from rpg.io.menu_inventario import exibir_inventario_combate
        if exibir_inventario_combate(gm.jogador):
            return {"tipo": "passar_turno"} # Ação já foi feita, apenas consuma o turno.
        else:
            return None # O jogador cancelou, então não consuma o turno.

    elif escolha_acao == 'Fugir':
        return {"tipo": "fugir"}

    print("Ação inválida ou cancelada.")
    funcoes_gerais.pausar()
    return None

if __name__ == "__main__":
    main_loop()
