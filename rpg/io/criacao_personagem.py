from typing import TYPE_CHECKING
from ..entidades.personagem import Personagem
from ..utilitarios import funcoes_gerais
from ..dados.racas_base import RACAS
from ..dados.classes_iniciais import CLASSES_INICIAIS

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def distribuir_atributos(personagem: 'Personagem'):
    """
    Permite ao jogador distribuir um conjunto de pontos entre os atributos primários.
    """
    pontos_para_distribuir = 20
    atributos = {
        "forca": "Força", "destreza": "Destreza", "constituicao": "Constituição",
        "inteligencia": "Inteligência", "sabedoria": "Sabedoria", "carisma": "Carisma"
    }
    mapa_escolha = {
        "1": "forca", "2": "destreza", "3": "constituicao",
        "4": "inteligencia", "5": "sabedoria", "6": "carisma"
    }

    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Distribuição de Atributos", nivel=2)
    print("Sua raça e classe influenciaram seus atributos iniciais.")
    print(f"Agora, você tem {pontos_para_distribuir} pontos para distribuir livremente.")
    print("Cada atributo começa com um valor base de 5 mais os bônus raciais.")
    funcoes_gerais.pausar()

    while pontos_para_distribuir > 0:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho(f"Pontos Restantes: {pontos_para_distribuir}", nivel=3)

        print("--- Atributos Atuais ---")
        for i, (key, nome) in enumerate(atributos.items(), 1):
            print(f"{i}. {nome:<13}: {getattr(personagem, key)}")
        print("------------------------")

        escolha_attr = input("Digite o número do atributo para aumentar (ou 'ajuda'): ").lower().strip()

        if escolha_attr == 'ajuda':
            # ... (código de ajuda omitido para brevidade)
            continue

        if escolha_attr not in mapa_escolha:
            print("Escolha inválida. Por favor, digite um número de 1 a 6.")
            funcoes_gerais.pausar()
            continue

        attr_nome = mapa_escolha[escolha_attr]
        attr_display = atributos[attr_nome]

        try:
            pontos_add = int(input(f"Quantos pontos você quer adicionar a {attr_display}? "))
            if pontos_add <= 0:
                print("Você deve adicionar pelo menos 1 ponto.")
            elif pontos_add > pontos_para_distribuir:
                print(f"Você não tem pontos suficientes. Você só tem {pontos_para_distribuir} pontos restantes.")
            else:
                setattr(personagem, attr_nome, getattr(personagem, attr_nome) + pontos_add)
                pontos_para_distribuir -= pontos_add
                print(f"{attr_display} aumentado para {getattr(personagem, attr_nome)}!")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        funcoes_gerais.pausar()

    print("\nTodos os pontos foram distribuídos!")
    personagem.recalcular_stats_completos()
    funcoes_gerais.pausar()


def escolher_raca(personagem: 'Personagem'):
    """
    Permite ao jogador escolher uma raça para seu personagem.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Escolha de Raça", nivel=2)

    racas_list = list(RACAS.items())

    while True:
        print("Escolha sua raça:")
        for i, (id_raca, raca_data) in enumerate(racas_list, 1):
            print(f"{i}. {raca_data['nome']}")

        print("\nDigite o número da raça para ver mais detalhes (ex: '1') ou 'fim' para confirmar sua escolha.")
        escolha = input("Sua escolha: ").lower().strip()

        if escolha == 'fim':
            if personagem.raca:
                break
            else:
                print("Você deve primeiro selecionar uma raça vendo seus detalhes.")
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
                    sinal = "+" if mod >= 0 else ""
                    print(f"{stat.capitalize()}: {sinal}{mod}")
                print("\n--- Habilidades Raciais ---")
                for hab in raca_data['habilidades_raciais']:
                    print(f"- {hab.replace('_', ' ').capitalize()}")

                confirmar = input(f"\nDeseja escolher a raça {raca_data['nome']}? (s/n): ").lower().strip()
                if confirmar == 's':
                    personagem.raca = id_raca_escolhida
                    print(f"Você escolheu ser um(a) {raca_data['nome']}!")
                    funcoes_gerais.pausar()
                    break

            else:
                print("Número inválido.")
                funcoes_gerais.pausar()
        except ValueError:
            print("Entrada inválida. Digite um número.")
            funcoes_gerais.pausar()

    raca_escolhida_data = RACAS[personagem.raca]
    for stat, mod in raca_escolhida_data['modificadores_stats'].items():
        setattr(personagem, stat, getattr(personagem, stat) + mod)

    for habilidade in raca_escolhida_data['habilidades_raciais']:
        personagem.habilidades.append(habilidade)

    personagem.recalcular_stats_completos()
    print(f"\nSeus atributos foram atualizados com base na sua raça.")
    funcoes_gerais.pausar()


def escolher_classe(personagem: 'Personagem'):
    """
    Permite ao jogador escolher uma classe para seu personagem.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Escolha de Classe", nivel=2)

    classes_list = list(CLASSES_INICIAIS.items())

    while True:
        print("Escolha sua classe inicial:")
        for i, (id_classe, classe_data) in enumerate(classes_list, 1):
            print(f"{i}. {classe_data['nome']}")

        print("\nDigite o número da classe para ver mais detalhes (ex: '1') ou 'fim' para confirmar sua escolha.")
        escolha = input("Sua escolha: ").lower().strip()

        if escolha == 'fim':
            if personagem.classe:
                break
            else:
                print("Você deve primeiro selecionar uma classe vendo seus detalhes.")
                funcoes_gerais.pausar()
                continue

        try:
            index = int(escolha) - 1
            if 0 <= index < len(classes_list):
                id_classe_escolhida, classe_data = classes_list[index]

                funcoes_gerais.limpar_tela()
                funcoes_gerais.imprimir_cabecalho(classe_data['nome'], nivel=3)
                print(f"Descrição: {classe_data['descricao']}")
                print(f"\nAtributos Primários: {', '.join(classe_data['stats_primarios']).capitalize()}")
                print("\n--- Habilidades Iniciais ---")
                for hab in classe_data['habilidades_iniciais']:
                    print(f"- {hab.replace('_', ' ').capitalize()}")

                confirmar = input(f"\nDeseja escolher a classe {classe_data['nome']}? (s/n): ").lower().strip()
                if confirmar == 's':
                    personagem.classe = id_classe_escolhida
                    print(f"Você escolheu ser um(a) {classe_data['nome']}!")
                    funcoes_gerais.pausar()
                    break

            else:
                print("Número inválido.")
                funcoes_gerais.pausar()
        except ValueError:
            print("Entrada inválida. Digite um número.")
            funcoes_gerais.pausar()

    classe_escolhida_data = CLASSES_INICIAIS[personagem.classe]
    for habilidade in classe_escolhida_data['habilidades_iniciais']:
        personagem.habilidades.append(habilidade)

    # TODO: Implementar sistema de itens e equipar o equipamento inicial
    # equipamento_inicial = classe_escolhida_data['equipamento_inicial']

    personagem.recalcular_stats_completos()
    print(f"\nSuas habilidades foram atualizadas com base na sua classe.")
    funcoes_gerais.pausar()


def iniciar_criacao_personagem() -> 'Personagem':
    """
    Guia o jogador através do processo de criação de personagem.
    Retorna um objeto Personagem totalmente inicializado.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Criação de Personagem", nivel=1)

    nome = ""
    while not nome:
        nome = input("Digite o nome do seu herói: ").strip()
        if not nome:
            print("O nome não pode estar em branco.")

    jogador = Personagem(nome=nome)

    print(f"\nBem-vindo, {nome}!")

    # Nova ordem de criação
    escolher_raca(jogador)
    escolher_classe(jogador)
    distribuir_atributos(jogador)

    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Personagem Criado", nivel=2)
    raca_nome = RACAS[jogador.raca]['nome']
    classe_nome = CLASSES_INICIAIS[jogador.classe]['nome']
    print(f"Raça: {raca_nome} | Classe: {classe_nome}")
    print(jogador)
    print(f"Habilidades: {', '.join(hab.replace('_', ' ').capitalize() for hab in jogador.habilidades)}")
    funcoes_gerais.pausar()

    return jogador
