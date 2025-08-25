from typing import TYPE_CHECKING
from ..utilitarios import funcoes_gerais, narrador

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def exibir_inventario(jogador: 'Personagem'):
    """
    Exibe o inventário do jogador e permite a interação com os itens.
    """
    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("Inventário", nivel=1)

        if not jogador.inventario:
            print("Seu inventário está vazio.")
        else:
            print("Seus itens:")
            # Gera uma lista numerada de itens para seleção
            itens_listados = list(jogador.inventario.values())
            for i, entrada in enumerate(itens_listados, 1):
                item = entrada['item']
                quantidade = entrada['quantidade']
                print(f"{i}. {item.nome} (x{quantidade})")

        print("\n" + "="*40)
        print("Digite o número de um item para ver detalhes, ou 'voltar' para sair.")

        escolha = input("> ").lower().strip()

        if escolha == 'voltar':
            break

        elif escolha.isdigit():
            try:
                idx_escolhido = int(escolha) - 1
                if 0 <= idx_escolhido < len(itens_listados):
                    item_selecionado = itens_listados[idx_escolhido]['item']
                    # Mostra os detalhes e as opções para o item
                    menu_item_selecionado(jogador, item_selecionado)
                else:
                    print("Número de item inválido.")
                    funcoes_gerais.pausar()
            except (ValueError, IndexError):
                print("Entrada inválida.")
                funcoes_gerais.pausar()
        else:
            print("Comando inválido.")
            funcoes_gerais.pausar()


def menu_item_selecionado(jogador: 'Personagem', item):
    """
    Exibe um menu de ações para um item selecionado.
    """
    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho(f"Item: {item.nome}", nivel=2)
        print(item.info_detalhada())

        print("\n--- Ações ---")
        opcoes = []
        if item.é_consumivel():
            opcoes.append("Usar")
        if item.é_equipavel():
            opcoes.append("Equipar")

        opcoes.append("Descartar")
        opcoes.append("Voltar")

        for i, opcao in enumerate(opcoes, 1):
            print(f"{i}. {opcao}")

        escolha = input("> ").lower().strip()

        if not escolha.isdigit():
            print("Comando inválido.")
            funcoes_gerais.pausar()
            continue

        idx_escolhido = int(escolha) - 1
        if not 0 <= idx_escolhido < len(opcoes):
            print("Opção inválida.")
            funcoes_gerais.pausar()
            continue

        acao_selecionada = opcoes[idx_escolhido].lower()

        if acao_selecionada == 'voltar':
            break

        # --- Lógica das Ações (a ser implementada) ---
        elif acao_selecionada == 'usar':
            jogador.usar_item(item.id_item)
            funcoes_gerais.pausar()
            break # Volta para a lista de inventário após usar

        elif acao_selecionada == 'equipar':
            jogador.equipar_item(item.id_item)
            funcoes_gerais.pausar()
            break

        elif acao_selecionada == 'descartar':
            print(f"Você descarta {item.nome}.")
            # TODO: Implementar a lógica de descarte.
            # jogador.remover_item(item.id_item, 1)
            funcoes_gerais.pausar()
            break

def exibir_inventario_combate(jogador: 'Personagem') -> bool:
    """
    Exibe o inventário durante o combate. Retorna True se um item foi usado (um turno foi gasto).
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("Inventário de Combate", nivel=2)

    # Filtra para mostrar apenas itens consumíveis
    consumiveis = {k: v for k, v in jogador.inventario.items() if v['item'].é_consumivel()}

    if not consumiveis:
        narrador.narrar("Você não tem itens consumíveis para usar em combate.")
        funcoes_gerais.pausar()
        return False # Nenhum turno foi gasto

    narrador.narrar("Qual item você quer usar?")
    itens_listados = list(consumiveis.values())
    for i, entrada in enumerate(itens_listados, 1):
        item = entrada['item']
        quantidade = entrada['quantidade']
        print(f"{i}. {item.nome} (x{quantidade})")

    print("0. Voltar")

    escolha = input("> ").lower().strip()

    if escolha == '0' or not escolha.isdigit():
        print("Ação cancelada.")
        return False # Nenhum turno foi gasto

    try:
        idx_escolhido = int(escolha) - 1
        if 0 <= idx_escolhido < len(itens_listados):
            item_selecionado = itens_listados[idx_escolhido]['item']
            jogador.usar_item(item_selecionado.id_item)
            funcoes_gerais.pausar()
            return True # Um turno foi gasto
        else:
            print("Número de item inválido.")
            funcoes_gerais.pausar()
            return False
    except (ValueError, IndexError):
        print("Entrada inválida.")
        funcoes_gerais.pausar()
        return False
