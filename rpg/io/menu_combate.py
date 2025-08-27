from typing import TYPE_CHECKING, Optional
from ..utilitarios import funcoes_gerais

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def selecionar_item_combate_ui(personagem: 'Personagem') -> Optional[str]:
    """
    Exibe uma interface para o jogador selecionar um item consumível do inventário durante o combate.
    Retorna o id_item do item escolhido ou None se a ação for cancelada.
    """
    funcoes_gerais.limpar_tela()
    funcoes_gerais.imprimir_cabecalho("USAR ITEM")

    # Filtra o inventário para encontrar apenas itens consumíveis
    itens_consumiveis = [
        (id_item, dados["item"], dados["quantidade"])
        for id_item, dados in personagem.inventario.items()
        if dados["item"].é_consumivel()
    ]

    if not itens_consumiveis:
        print("Você não tem itens consumíveis para usar.")
        funcoes_gerais.pausar()
        return None

    print("Escolha um item para usar:\n")
    for i, (_, item, quantidade) in enumerate(itens_consumiveis, 1):
        print(f"{i}. {item.nome} (x{quantidade})")

    print(f"\n{len(itens_consumiveis) + 1}. Cancelar")

    while True:
        escolha_str = input("\n> ")
        if not escolha_str.isdigit():
            print("Por favor, insira um número.")
            continue

        escolha_idx = int(escolha_str) - 1

        if 0 <= escolha_idx < len(itens_consumiveis):
            id_item_selecionado, _, _ = itens_consumiveis[escolha_idx]
            # Confirmação
            confirmar = input(f"Usar {itens_consumiveis[escolha_idx][1].nome}? (s/n): ").lower()
            if confirmar == 's':
                return id_item_selecionado
            else:
                print("Ação cancelada.")
                funcoes_gerais.pausar()
                return None
        elif escolha_idx == len(itens_consumiveis): # Opção de cancelar
            print("Ação cancelada.")
            funcoes_gerais.pausar()
            return None
        else:
            print("Opção inválida.")
