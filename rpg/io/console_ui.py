from . import criacao_personagem as cc_api
from ..utilitarios import funcoes_gerais
from ..entidades.personagem import Personagem

def criar_novo_personagem_ui() -> Personagem:
    """
    Conduz o processo completo de criação de personagem através da interface do console.
    """
    funcoes_gerais.imprimir_cabecalho("CRIAÇÃO DE PERSONAGEM")
    print("Bem-vindo, aventureiro! Vamos criar seu herói.\n")

    nome = input("Primeiro, qual é o seu nome? ").strip()
    while not nome:
        print("O nome não pode estar em branco.")
        nome = input("Qual é o seu nome? ").strip()

    personagem = cc_api.criar_personagem_base(nome)
    print(f"\nUm herói chamado {nome}, o Valente se prepara para a jornada!")
    funcoes_gerais.pausar()

    # Seleção de Raça
    selecionar_raca_ui(personagem)

    # Seleção de Classe
    selecionar_classe_ui(personagem)

    # Distribuição de Atributos
    distribuir_pontos_ui(personagem)

    # Finalização
    personagem_final = cc_api.finalizar_criacao(personagem)
    funcoes_gerais.imprimir_cabecalho("PERSONAGEM CONCLUÍDO")
    print("Seu herói está pronto para a aventura!")
    print(personagem_final)
    funcoes_gerais.pausar()

    return personagem_final

def selecionar_raca_ui(personagem: Personagem):
    """Interface para o jogador selecionar uma raça."""
    racas = cc_api.get_racas_disponiveis()
    pagina_atual = 0
    racas_por_pagina = 5

    while True:
        funcoes_gerais.imprimir_cabecalho("SELEÇÃO DE RAÇA")
        print("Escolha a raça do seu personagem. Cada raça oferece bônus e habilidades únicas.\n")

        inicio = pagina_atual * racas_por_pagina
        fim = inicio + racas_por_pagina
        racas_pagina = list(racas.items())[inicio:fim]

        for i, (id_raca, raca_data) in enumerate(racas_pagina, 1):
            print(f"{i}. {raca_data['nome']} - {raca_data['short_desc']}")

        print("\n" + "-" * 41)
        print("Comandos:")
        if fim < len(racas): print("  'p' para próxima página, ", end="")
        if pagina_atual > 0: print("'a' para página anterior, ", end="")
        print("\n  Digite o número da raça para ver detalhes")

        escolha = input("> ").lower().strip()

        if escolha == 'p' and fim < len(racas):
            pagina_atual += 1
        elif escolha == 'a' and pagina_atual > 0:
            pagina_atual -= 1
        elif escolha.isdigit():
            idx_escolha = int(escolha) - 1
            if 0 <= idx_escolha < len(racas_pagina):
                id_raca_selecionada, raca_data = racas_pagina[idx_escolha]
                funcoes_gerais.limpar_tela()
                print(f"---------- DETALHES: {raca_data['nome']} ----------\n")
                print(raca_data['long_desc'])
                print("\nModificadores de Atributos:")
                for stat, mod in raca_data.get('modificadores_stats', {}).items():
                    print(f"  - {stat.capitalize()}: {mod:+} ")
                print("\nHabilidades Raciais:")
                for hab in raca_data.get('habilidades_raciais', []):
                    print(f"  - {hab.replace('_', ' ').capitalize()}")

                confirmar = input(f"\nVocê quer ser um {raca_data['nome']}? (s/n) ").lower()
                if confirmar == 's':
                    cc_api.aplicar_raca(personagem, id_raca_selecionada)
                    print(f"\nVocê agora é um {raca_data['nome']}!")
                    funcoes_gerais.pausar()
                    return
            else:
                print("Número inválido.")
                funcoes_gerais.pausar()
        else:
            print("Comando inválido.")
            funcoes_gerais.pausar()

def selecionar_classe_ui(personagem: Personagem):
    """Interface para o jogador selecionar uma classe."""
    classes = cc_api.get_classes_disponiveis_para_raca(personagem.raca)
    pagina_atual = 0
    classes_por_pagina = 10

    while True:
        funcoes_gerais.imprimir_cabecalho("SELEÇÃO DE CLASSE")
        print(f"Como um {personagem.raca.capitalize()}, qual caminho você seguirá?\n")

        inicio = pagina_atual * classes_por_pagina
        fim = inicio + classes_por_pagina
        classes_pagina = list(classes.items())[inicio:fim]

        for i, (id_classe, classe_data) in enumerate(classes_pagina, 1):
            print(f"{i}. {classe_data['nome']} - {classe_data['short_desc']}")

        print("\n" + "-" * 41)
        print("Comandos:")
        if fim < len(classes): print("  'p' para próxima página, ", end="")
        if pagina_atual > 0: print("'a' para página anterior, ", end="")
        print("\n  Digite o número da classe para ver detalhes")

        escolha = input("> ").lower().strip()

        if escolha == 'p' and fim < len(classes):
            pagina_atual += 1
        elif escolha == 'a' and pagina_atual > 0:
            pagina_atual -= 1
        elif escolha.isdigit():
            idx_escolha = int(escolha) - 1
            if 0 <= idx_escolha < len(classes_pagina):
                id_classe_selecionada, classe_data = classes_pagina[idx_escolha]
                funcoes_gerais.limpar_tela()
                print(f"---------- DETALHES: {classe_data['nome']} ----------\n")
                print(classe_data['long_desc'])
                print(f"\nAtributos Primários:")
                print(f"  - {', '.join(classe_data.get('stats_primarios', []))}")
                print("\nHabilidades Iniciais:")
                for hab in classe_data.get('habilidades_iniciais', []):
                    print(f"  - {hab.replace('_', ' ').capitalize()}")

                confirmar = input(f"\nVocê quer ser um {classe_data['nome']}? (s/n) ").lower()
                if confirmar == 's':
                    cc_api.aplicar_classe(personagem, id_classe_selecionada)
                    print(f"\nVocê agora é um {classe_data['nome']}!")
                    funcoes_gerais.pausar()
                    return
            else:
                print("Número inválido.")
                funcoes_gerais.pausar()
        else:
            print("Comando inválido.")
            funcoes_gerais.pausar()

def distribuir_pontos_ui(personagem: Personagem):
    """Interface para o jogador distribuir os pontos de atributo."""
    pontos = personagem.pontos_de_atributo_para_distribuir
    distribuicao = {
        "forca": 0, "destreza": 0, "constituicao": 0,
        "inteligencia": 0, "sabedoria": 0, "carisma": 0, "sorte": 0
    }

    while True:
        funcoes_gerais.imprimir_cabecalho("DISTRIBUIÇÃO DE PONTOS DE ATRIBUTO")
        print(f"Você tem {pontos} pontos para distribuir.\n")

        # Exibe os atributos
        for attr, valor in distribuicao.items():
            base_attr = getattr(personagem, f"base_{attr}")
            print(f"  - {attr.capitalize():<12}: {base_attr + valor} ({base_attr} +{valor})")

        print("\n" + "-" * 41)
        print("Comandos:")
        print("  Use 'atributo+' para adicionar um ponto (ex: forca+)")
        print("  Use 'atributo-' para remover um ponto (ex: forca-)")
        print("  Digite 'pronto' quando terminar.")

        cmd = input("> ").lower().strip()

        if cmd == 'pronto':
            if pontos > 0:
                print(f"Você ainda tem {pontos} para distribuir. Tem certeza? (s/n)")
                if input("> ").lower() != 's':
                    continue
            break

        if len(cmd) < 2:
            print("Comando inválido.")
            funcoes_gerais.pausar()
            continue

        operacao = cmd[-1]
        atributo = cmd[:-1]

        if atributo not in distribuicao:
            print(f"Atributo '{atributo}' desconhecido.")
            funcoes_gerais.pausar()
            continue

        if operacao == '+':
            if pontos > 0:
                distribuicao[atributo] += 1
                pontos -= 1
            else:
                print("Você não tem mais pontos para distribuir.")
                funcoes_gerais.pausar()
        elif operacao == '-':
            if distribuicao[atributo] > 0:
                distribuicao[atributo] -= 1
                pontos += 1
            else:
                print(f"Você não pode remover mais pontos de {atributo}.")
                funcoes_gerais.pausar()
        else:
            print("Operação inválida. Use '+' ou '-'.")
            funcoes_gerais.pausar()

    cc_api.aplicar_atributos(personagem, distribuicao)
    print("\nPontos de atributo distribuídos com sucesso!")
    funcoes_gerais.pausar()
