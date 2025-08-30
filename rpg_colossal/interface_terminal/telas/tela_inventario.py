# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: INVENTÁRIO
================================================================================================
Este módulo é responsável por renderizar e gerenciar a tela de inventário, uma
interface interativa onde o jogador pode visualizar e gerenciar os itens que possui.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Interface Interativa:** Diferente de telas estáticas como a de status, o
  inventário é um loop interativo. O jogador pode navegar, selecionar itens e
  executar ações sobre eles.

- **Fluxo em Duas Etapas:**
  1. **Visualização da Lista:** A tela principal mostra uma lista numerada de todos
     os itens no inventário do personagem. O jogador pode selecionar um item
     digitando seu número ou sair.
  2. **Menu de Ação do Item:** Ao selecionar um item, um novo menu de contexto
     aparece, mostrando os detalhes do item e as ações possíveis (usar, equipar,
     descartar, etc.).

- **Delegação de Lógica:** A tela do inventário não contém a lógica de "o que
  acontece quando um item é usado". Ela apenas captura a intenção do jogador e
  chama o método apropriado no objeto `Personagem` (ex: `personagem.equipar_item`).
  A lógica real do que significa equipar um item (mudar atributos, etc.) pertence
  à classe `Personagem` ou a um sistema de itens.

- **Testabilidade:** O loop interativo e as chamadas de método são testados
  usando `unittest.mock` para simular a entrada do usuário e para verificar se
  os métodos corretos no objeto `Personagem` são chamados.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

try:
    from rpg_colossal.motor_jogo.entidades.personagem import Personagem
    from rpg_colossal.motor_jogo.utilitarios import funcoes_gerais as geral
except ImportError:
    # Mocks para execução independente
    class Personagem:
        def equipar_item(self, item, slot): pass
    class geral:
        def limpar_tela(): pass
        def desenhar_caixa(t, c): return f"== {t} ==\n" + "\n".join(c)
        def pausar_tela(): pass

# ==============================================================================================
# == SEÇÃO 2: FUNÇÃO PRINCIPAL DA TELA =========================================================
# ==============================================================================================
def exibir_inventario(personagem: Personagem):
    """
    Inicia e gerencia o loop interativo da tela de inventário.
    """
    while True:
        geral.limpar_tela()
        print(geral.criar_cabecalho("Inventário"))

        if not personagem.inventario:
            print("Seu inventário está vazio.")
            print("\n[0] Voltar")
        else:
            print("Seus Itens:")
            for i, item in enumerate(personagem.inventario):
                print(f"  [{i+1}] {item.get('nome', 'Item Desconhecido')}")
            print("\n[0] Voltar")

        escolha_item = input("\nSelecione um item para inspecionar (ou 0 para voltar): ")

        if escolha_item == '0':
            break

        try:
            idx = int(escolha_item) - 1
            if 0 <= idx < len(personagem.inventario):
                item_selecionado = personagem.inventario[idx]
                # Entra no menu de ação para o item selecionado
                _menu_acao_item(personagem, item_selecionado)
            else:
                print("Seleção inválida.")
                geral.pausar_tela()
        except (ValueError, TypeError):
            print("Entrada inválida.")
            geral.pausar_tela()

def _menu_acao_item(personagem: Personagem, item: dict):
    """
    Exibe um menu de ações para um item específico.
    """
    while True:
        geral.limpar_tela()
        print(geral.desenhar_caixa(item.get('nome'), [item.get('descricao', 'Sem descrição.')]))

        print("\nAções:")
        print("[1] Equipar") # Assumindo que pode ser equipamento
        print("[2] Usar")    # Assumindo que pode ser consumível
        print("[3] Descartar")
        print("[0] Voltar")

        escolha_acao = input("\nO que fazer com este item? ")

        if escolha_acao == '1':
            # Lógica de equipar simplificada. Assume que o item tem um slot.
            slot = item.get("slot", "mao_principal")
            personagem.equipar_item(item, slot) # Delega a ação para o objeto personagem
            print(f"Você equipou {item.get('nome')}.")
            geral.pausar_tela()
            return # Retorna para a lista principal do inventário
        elif escolha_acao == '2':
            print("Você não pode usar este item agora.")
            geral.pausar_tela()
        elif escolha_acao == '3':
            print(f"{item.get('nome')} foi descartado.")
            personagem.inventario.remove(item)
            geral.pausar_tela()
            return # Retorna para a lista principal do inventário
        elif escolha_acao == '0':
            break # Volta para a lista de itens
        else:
            print("Ação inválida.")
            geral.pausar_tela()


# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
import unittest
from unittest.mock import patch

class TestTelaInventario(unittest.TestCase):
    def setUp(self):
        """Prepara um personagem mock com um inventário."""
        # A instanciação correta do Personagem é necessária mesmo para o mock
        mock_raca_data = {"id": "humano_t", "nome": "Humano de Teste", "atributos_base": {"constituicao": 10}}
        mock_classe_data = {"id_classe": "guerreiro_t", "nome": "Guerreiro", "habilidades_iniciais": []}
        self.mock_personagem = Personagem(
            id_entidade="player_test_inv", nome="Testador",
            dados_raca=mock_raca_data, dados_classe=mock_classe_data
        )

        self.mock_personagem.inventario = [
            {"nome": "Espada de Ferro", "descricao": "Uma espada básica.", "slot": "mao_principal"},
            {"nome": "Poção de Cura", "descricao": "Restaura HP."}
        ]
        # Adiciona um mock para o método que será chamado
        self.mock_personagem.equipar_item = unittest.mock.MagicMock()

    @patch('rpg_colossal.interface_terminal.telas.tela_inventario.geral')
    @patch('builtins.input', side_effect=['1', '1', '', '0']) # 1 (seleciona Espada), 1 (equipa), '' (pausa), 0 (sai)
    def test_fluxo_equipar_item(self, mock_input, mock_geral):
        """Verifica se a seleção e a ação de equipar chamam o método correto."""

        exibir_inventario(self.mock_personagem)

        # Verifica se o método equipar_item foi chamado corretamente
        self.mock_personagem.equipar_item.assert_called_once()
        # Verifica se foi chamado com o item correto
        item_esperado = self.mock_personagem.inventario[0]
        self.mock_personagem.equipar_item.assert_called_with(item_esperado, "mao_principal")

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    unittest.main(verbosity=2)
