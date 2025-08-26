# rpg_legacy/io/console_ui.py

from . import criacao_personagem as cc_api
from ..entidades.personagem import Personagem

def limpar_tela():
    """Função auxiliar para limpar o console."""
    # Simplesmente imprime várias linhas novas para "limpar" a tela.
    # Em um sistema real, usaríamos os.system('cls') ou os.system('clear').
    print("\n" * 100)

def esperar_enter():
    """Pausa a execução até que o usuário pressione Enter."""
    input("\nPressione Enter para continuar...")

def iniciar_criacao_personagem_console() -> Personagem:
    """
    Orquestra o fluxo de criação de personagem através do console.
    Esta função é responsável por toda a interação com o usuário.
    """
    limpar_tela()
    print("=========================================")
    print("||      CRIAÇÃO DE PERSONAGEM      ||")
    print("=========================================")
    print("\nBem-vindo, aventureiro! Vamos criar seu herói.")

    # 1. Obter o nome do personagem
    nome = ""
    while not nome:
        nome = input("\nQual é o nome do seu personagem? ")
        if not nome:
            print("O nome não pode ficar em branco.")

    personagem = cc_api.criar_personagem_base(nome)
    print(f"\nUm herói chamado {personagem.nome} se prepara para a jornada!")
    esperar_enter()

    # 2. Seleção de Raça
    personagem = _selecionar_raca_ui(personagem)

    # 3. Seleção de Classe
    personagem = _selecionar_classe_ui(personagem)

    # 4. Distribuição de Pontos
    personagem = _distribuir_pontos_ui(personagem)

    # Finalização
    personagem = cc_api.finalizar_criacao(personagem)

    limpar_tela()
    print("=========================================")
    print("||       PERSONAGEM CONCLUÍDO       ||")
    print("=========================================")
    print("\nSeu herói está pronto para a aventura!")
    print(personagem)
    esperar_enter()

    return personagem

def _selecionar_raca_ui(personagem: Personagem) -> Personagem:
    """
    Função de UI para o fluxo de seleção de raça.
    Retorna o personagem com a raça aplicada.
    """
    racas_dict = cc_api.get_dados_racas()
    racas_lista = list(racas_dict.items())
    pagina_atual = 0
    itens_por_pagina = 5

    while True:
        limpar_tela()
        print("=========================================")
        print("||         SELEÇÃO DE RAÇA         ||")
        print("=========================================")
        print("\nEscolha a raça do seu personagem. Cada raça oferece bônus e habilidades únicas.\n")

        inicio = pagina_atual * itens_por_pagina
        fim = inicio + itens_por_pagina

        for i, (id_raca, raca_data) in enumerate(racas_lista[inicio:fim], start=inicio):
            print(f"{i + 1}. {raca_data['nome']} - {raca_data['descricao']}")

        print("\n-----------------------------------------")
        print("Comandos:")
        print("  'p' para próxima página, 'a' para página anterior")
        print("  Digite o número da raça para ver detalhes")

        escolha = input("\nSua escolha: ").lower()

        if escolha == 'p':
            if fim < len(racas_lista):
                pagina_atual += 1
            else:
                print("\nVocê já está na última página.")
                esperar_enter()
        elif escolha == 'a':
            if pagina_atual > 0:
                pagina_atual -= 1
            else:
                print("\nVocê já está na primeira página.")
                esperar_enter()
        elif escolha.isdigit() and 1 <= int(escolha) <= len(racas_lista):
            indice = int(escolha) - 1
            id_raca_selecionada, raca_info = racas_lista[indice]

            limpar_tela()
            print(f"---------- DETALHES: {raca_info['nome']} ----------")
            print(f"\n{raca_info['lore']}\n")
            print("Modificadores de Atributos:")
            for stat, mod in raca_info['modificadores_stats'].items():
                print(f"  - {stat.capitalize()}: {mod:+} ")
            print("\nHabilidades Raciais:")
            for hab in raca_info['habilidades_raciais']:
                print(f"  - {hab.replace('_', ' ').capitalize()}")

            confirmar = input(f"\nVocê deseja confirmar {raca_info['nome']} como sua raça? (s/n): ").lower()
            if confirmar == 's':
                cc_api.aplicar_raca(personagem, id_raca_selecionada)
                print(f"\nVocê agora é um {raca_info['nome']}!")
                esperar_enter()
                return personagem
        else:
            print("\nComando inválido.")
            esperar_enter()

def _selecionar_classe_ui(personagem: Personagem) -> Personagem:
    """
    Função de UI para o fluxo de seleção de classe.
    Retorna o personagem com a classe aplicada.
    """
    classes_dict = cc_api.get_dados_classes()
    classes_lista = list(classes_dict.items())
    pagina_atual = 0
    itens_por_pagina = 10 # Mais itens por página para classes

    while True:
        limpar_tela()
        print("=========================================")
        print("||        SELEÇÃO DE CLASSE        ||")
        print("=========================================")
        print(f"\nComo um {personagem.raca}, qual caminho você seguirá?\n")

        inicio = pagina_atual * itens_por_pagina
        fim = inicio + itens_por_pagina

        for i, (id_classe, classe_data) in enumerate(classes_lista[inicio:fim], start=inicio):
            print(f"{i + 1}. {classe_data['nome']} - {classe_data['descricao']}")

        print("\n-----------------------------------------")
        print("Comandos:")
        print("  'p' para próxima página, 'a' para página anterior")
        print("  Digite o número da classe para ver detalhes")

        escolha = input("\nSua escolha: ").lower()

        if escolha == 'p':
            if fim < len(classes_lista):
                pagina_atual += 1
            else:
                print("\nVocê já está na última página.")
                esperar_enter()
        elif escolha == 'a':
            if pagina_atual > 0:
                pagina_atual -= 1
            else:
                print("\nVocê já está na primeira página.")
                esperar_enter()
        elif escolha.isdigit() and 1 <= int(escolha) <= len(classes_lista):
            indice = int(escolha) - 1
            id_classe_selecionada, classe_info = classes_lista[indice]

            limpar_tela()
            print(f"---------- DETALHES: {classe_info['nome']} ----------")
            print(f"\n{classe_info['lore']}\n")
            print("Atributos Primários:")
            print(f"  - {', '.join(stat.capitalize() for stat in classe_info['stats_primarios'])}")
            print("\nHabilidades Iniciais:")
            for hab in classe_info['habilidades_iniciais']:
                print(f"  - {hab.replace('_', ' ').capitalize()}")

            confirmar = input(f"\nVocê deseja confirmar {classe_info['nome']} como sua classe? (s/n): ").lower()
            if confirmar == 's':
                cc_api.aplicar_classe(personagem, id_classe_selecionada)
                print(f"\nVocê agora é um {classe_info['nome']}!")
                esperar_enter()
                return personagem
        else:
            print("\nComando inválido.")
            esperar_enter()

def _distribuir_pontos_ui(personagem: Personagem) -> Personagem:
    """
    Função de UI para o fluxo de distribuição de pontos de atributo.
    """
    pontos_restantes = personagem.pontos_de_atributo_para_distribuir
    distribuicao_atual = {
        "forca": 0, "destreza": 0, "constituicao": 0,
        "inteligencia": 0, "sabedoria": 0, "carisma": 0, "sorte": 0
    }
    atributos = list(distribuicao_atual.keys())

    while True:
        limpar_tela()
        print("=========================================")
        print("||   DISTRIBUIÇÃO DE PONTOS DE ATRIBUTO   ||")
        print("=========================================")
        print(f"\nVocê tem {pontos_restantes} pontos para distribuir.\n")

        # Exibe os atributos base + pontos alocados
        for stat in atributos:
            base_stat = getattr(personagem, 'base_' + stat)
            alocado = distribuicao_atual[stat]
            print(f"  - {stat.capitalize():<12}: {base_stat + alocado} ({base_stat} +{alocado})")

        print("\n-----------------------------------------")
        print("Comandos:")
        print("  Use 'atributo+' para adicionar um ponto (ex: forca+)")
        print("  Use 'atributo-' para remover um ponto (ex: forca-)")
        print("  Digite 'pronto' quando terminar.")

        escolha = input("\nComando: ").lower()

        if escolha == 'pronto':
            if pontos_restantes > 0:
                confirmar = input(f"\nVocê ainda tem {pontos_restantes} pontos não distribuídos. Deseja continuar mesmo assim? (s/n): ").lower()
                if confirmar != 's':
                    continue

            # Aplica os pontos usando a API
            # A API agora usa o método do personagem, que valida os pontos.
            sucesso = cc_api.aplicar_atributos(personagem, distribuicao_atual)
            if sucesso:
                print("\nAtributos definidos!")
                esperar_enter()
                return personagem
            else:
                # Isso não deveria acontecer se a lógica da UI estiver correta, mas é uma segurança.
                print("\nErro ao aplicar atributos. Verifique se você tem pontos suficientes.")
                esperar_enter()

        elif escolha.endswith('+') or escolha.endswith('-'):
            operacao = escolha[-1]
            atributo = escolha[:-1]

            if atributo not in atributos:
                print("\nAtributo inválido.")
                esperar_enter()
                continue

            if operacao == '+':
                if pontos_restantes > 0:
                    distribuicao_atual[atributo] += 1
                    pontos_restantes -= 1
                else:
                    print("\nVocê não tem mais pontos para distribuir.")
                    esperar_enter()
            else: # Operação é '-'
                if distribuicao_atual[atributo] > 0:
                    distribuicao_atual[atributo] -= 1
                    pontos_restantes += 1
                else:
                    print(f"\nVocê não pode remover mais pontos de {atributo.capitalize()}.")
                    esperar_enter()
        else:
            print("\nComando inválido.")
            esperar_enter()

if __name__ == '__main__':
    # Para testar o fluxo de forma isolada
    novo_heroi = iniciar_criacao_personagem_console()
    print("\n--- PERSONAGEM CRIADO ---")
    print(novo_heroi)
