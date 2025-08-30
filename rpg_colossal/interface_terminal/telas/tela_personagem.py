# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: STATUS DO PERSONAGEM
================================================================================================
Este módulo é responsável por renderizar a "Ficha de Personagem", uma tela detalhada
que exibe todas as informações relevantes sobre o protagonista do jogador.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Leitura de Dados:** A função principal, `exibir_tela_personagem`, recebe uma
  instância completa do objeto `Personagem` e é responsável por ler seus atributos,
  equipamentos, habilidades, etc.

- **Apresentação Formatada:** A principal tarefa deste módulo é a formatação. Ele
  pega dados brutos do objeto `Personagem` e os apresenta em seções lógicas e
  claras (Informações Básicas, Atributos, Equipamento, etc.), utilizando
  utilitários de UI para criar uma apresentação visualmente agradável no terminal.

- **Interface Estática:** Esta tela é, em sua maioria, apenas para leitura. Sua única
  interação é esperar que o jogador pressione uma tecla para fechá-la e retornar à
  tela anterior (geralmente, a tela de exploração).
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
        pass
    class geral:
        def limpar_tela(): pass
        def desenhar_caixa(t, c): return f"== {t} ==\n" + "\n".join(c)
        def pausar_tela(): pass

# ==============================================================================================
# == SEÇÃO 2: FUNÇÃO PRINCIPAL DA TELA =========================================================
# ==============================================================================================
def exibir_tela_personagem(personagem: Personagem):
    """
    Renderiza a ficha de personagem completa e detalhada.

    Args:
        personagem (Personagem): A instância do personagem do jogador.
    """
    geral.limpar_tela()

    # --- Seção 1: Informações Básicas ---
    info_basica = [
        f"Nome: {personagem.nome}",
        f"Raça: {personagem.raca.get('nome', 'N/A')}",
        f"Classe: {personagem.classe.get('nome', 'N/A')}",
        f"Nível: {personagem.nivel}",
        f"XP: {personagem.xp_atual} / {personagem.xp_para_proximo_nivel}",
        f"Alinhamento: {personagem.alinhamento}"
    ]
    print(geral.desenhar_caixa("FICHA DE PERSONAGEM", info_basica))

    # --- Seção 2: Atributos e Status ---
    coluna_atributos = [f"{chave.capitalize():<12}: {valor}" for chave, valor in personagem.atributos.items()]
    coluna_status = [
        f"{'HP':<12}: {personagem.hp_atual}/{personagem.hp_max}",
        f"{'Mana':<12}: {personagem.mana_atual}/{personagem.mana_max}",
    ]
    # Lógica para imprimir em duas colunas (simplificada)
    print("\n-- Atributos & Status --")
    max_linhas = max(len(coluna_atributos), len(coluna_status))
    for i in range(max_linhas):
        str_atr = coluna_atributos[i] if i < len(coluna_atributos) else ""
        str_stat = coluna_status[i] if i < len(coluna_status) else ""
        print(f"{str_atr:<30} | {str_stat}")

    # --- Seção 3: Equipamento ---
    print("\n-- Equipamento --")
    for slot, item in personagem.equipamento.items():
        nome_item = item['nome'] if item else "Vazio"
        print(f"  - {slot.replace('_', ' ').capitalize():<15}: {nome_item}")

    # --- Seção 4: Reputação ---
    if personagem.reputacao:
        print("\n-- Reputação --")
        for faccao, valor in personagem.reputacao.items():
            print(f"  - {faccao.replace('_', ' ').capitalize()}: {valor}")

    print("\nPressione ENTER para voltar...")
    geral.pausar_tela()

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
import unittest
from unittest.mock import patch, MagicMock

class TestTelaPersonagem(unittest.TestCase):
    def setUp(self):
        """Prepara um objeto Personagem mock rico em detalhes para o teste."""
        mock_raca_data = {"nome": "Humano", "atributos_base": {"constituicao": 10}}
        mock_classe_data = {"nome": "Cavaleiro", "habilidades_iniciais": []}

        self.mock_personagem = Personagem(
            id_entidade="sir_kael_01",
            nome="Sir Kael",
            dados_raca=mock_raca_data,
            dados_classe=mock_classe_data
        )
        self.mock_personagem.nivel = 10
        self.mock_personagem.xp_atual = 500
        self.mock_personagem.xp_para_proximo_nivel = 1200
        self.mock_personagem.alinhamento = "Leal e Bom"
        self.mock_personagem.atributos = {"forca": 20, "destreza": 15, "constituicao": 10}
        self.mock_personagem.hp_atual = 95
        self.mock_personagem.hp_max = 100
        self.mock_personagem.mana_atual = 45
        self.mock_personagem.mana_max = 50
        self.mock_personagem.equipamento = {
            "mao_principal": {"nome": "Espada Longa de Aço"},
            "peito": {"nome": "Peitoral de Placas"},
            "cabeca": None, "mao_secundaria": None, "pernas": None, "pes": None, "amuleto": None, "anel_1": None, "anel_2": None
        }
        self.mock_personagem.reputacao = {"guilda_dos_guerreiros": 550}

    @patch('builtins.print')
    @patch(__name__ + '.geral')
    def test_exibicao_de_todos_os_dados(self, mock_geral, mock_print):
        """Verifica se todas as seções e dados chave são impressos na tela."""
        mock_geral.desenhar_caixa.return_value = "CAIXA_FICHA"

        exibir_tela_personagem(self.mock_personagem)

        # Verifica se a caixa principal foi impressa
        mock_print.assert_any_call("CAIXA_FICHA")

        # Verifica se um dado de cada seção foi impresso (não precisa checar tudo)
        # O teste real é a chamada para desenhar_caixa, que recebe os dados.
        # Aqui verificamos as impressões diretas.

        # Atributos
        self.assertTrue(any("Forca" in call.args[0] and "20" in call.args[0] for call in mock_print.call_args_list))
        # Equipamento
        self.assertTrue(any("Espada Longa de Aço" in call.args[0] for call in mock_print.call_args_list))
        # Reputação
        self.assertTrue(any("Guilda dos guerreiros: 550" in call.args[0] for call in mock_print.call_args_list))

        # Verifica se a pausa foi chamada no final
        mock_geral.pausar_tela.assert_called_once()


if __name__ == "__main__":
    # Adiciona o path aqui para garantir que o test runner encontre os módulos
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    unittest.main(verbosity=2)
