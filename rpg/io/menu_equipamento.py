from typing import TYPE_CHECKING
from ..utilitarios import funcoes_gerais

if TYPE_CHECKING:
    from ..entidades.personagem import Personagem

def exibir_equipamento(jogador: 'Personagem'):
    """
    Exibe os equipamentos atuais do jogador e permite a interação para desequipar.
    """
    while True:
        funcoes_gerais.limpar_tela()
        funcoes_gerais.imprimir_cabecalho("Equipamento", nivel=1)

        # Gera uma lista numerada de slots para seleção
        slots_listados = list(jogador.equipamentos.keys())
        for i, slot in enumerate(slots_listados, 1):
            item = jogador.equipamentos[slot]
            nome_slot = slot.replace('_', ' ').capitalize()
            nome_item = item.nome if item else "[Vazio]"
            print(f"{i}. {nome_slot:<15}: {nome_item}")

        print("\n" + "="*40)
        print("Digite o número de um slot para desequipar o item, ou 'voltar' para sair.")

        escolha = input("> ").lower().strip()

        if escolha == 'voltar':
            break

        elif escolha.isdigit():
            try:
                idx_escolhido = int(escolha) - 1
                if 0 <= idx_escolhido < len(slots_listados):
                    slot_selecionado = slots_listados[idx_escolhido]
                    # Verifica se há um item para desequipar
                    if jogador.equipamentos[slot_selecionado]:
                        jogador.desequipar_item(slot_selecionado)
                        funcoes_gerais.pausar()
                    else:
                        print("Este slot está vazio.")
                        funcoes_gerais.pausar()
                else:
                    print("Número de slot inválido.")
                    funcoes_gerais.pausar()
            except (ValueError, IndexError):
                print("Entrada inválida.")
                funcoes_gerais.pausar()
        else:
            print("Comando inválido.")
            funcoes_gerais.pausar()
