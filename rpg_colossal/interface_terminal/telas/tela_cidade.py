# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: CIDADE
================================================================================================
Este módulo é responsável por renderizar e gerenciar a tela da cidade, o principal
hub para interações não-combativas como comércio, missões e socialização.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Menu Dinâmico:** A função `exibir_cidade` não tem um menu fixo. Ela lê os
  dados da cidade atual (passados através do `EstadoJogo`) e constrói dinamicamente
  uma lista de opções com base nos `servicos` disponíveis (lojas, taverna, etc.).
  Isso significa que cada cidade pode oferecer uma experiência única.

- **Loop de Interação Local:** A função opera em seu próprio loop `while`,
  permitindo que o jogador realize múltiplas ações dentro da cidade sem retornar
  imediatamente ao loop de exploração principal. O loop só termina quando o
  jogador escolhe a opção "Sair da cidade".

- **Delegação para Sub-Telas:** Assim como o `main.py` orquestra as telas principais,
  a `tela_cidade` orquestrará as "sub-telas" da cidade. Ao escolher "Visitar a
  taverna", por exemplo, esta função chamará a função `exibir_taverna` de outro
  módulo (a ser implementado). Por enquanto, apenas placeholders são exibidos.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

try:
    from rpg_colossal.motor_jogo.sistemas.gerenciador_save import EstadoJogo
    from rpg_colossal.motor_jogo.banco_de_dados.mundo.cidades import INDICE_CIDADES
    from rpg_colossal.motor_jogo.utilitarios import funcoes_gerais as geral
except ImportError:
    # Mocks para execução independente
    class EstadoJogo: pass
    class Personagem: pass
    INDICE_CIDADES = {"by_id": {}}
    class geral:
        def limpar_tela(): pass
        def criar_cabecalho(t): return f"== {t} =="
        def pausar_tela(): pass

# ==============================================================================================
# == SEÇÃO 2: FUNÇÃO PRINCIPAL DA TELA =========================================================
# ==============================================================================================
def exibir_cidade(estado_jogo: EstadoJogo, db_cidades=INDICE_CIDADES, ui_utils=geral):
    """
    Inicia e gerencia o loop interativo da tela da cidade.
    """
    id_cidade = estado_jogo.personagem.localizacao_atual
    dados_cidade = db_cidades["by_id"].get(id_cidade)

    if not dados_cidade:
        ui_utils.limpar_tela()
        print(f"Erro: Cidade '{id_cidade}' não encontrada.")
        ui_utils.pausar_tela()
        return

    while True:
        ui_utils.limpar_tela()

        # --- Renderização ---
        print(ui_utils.criar_cabecalho(dados_cidade["nome"]))
        print(dados_cidade["descricao"])

        # --- Construção do Menu de Ações Dinâmico ---
        acoes = []
        servicos = dados_cidade.get("servicos", {})

        for loja_id in servicos.get("lojas", []):
            acoes.append({"texto": f"Visitar a loja: {loja_id}", "acao": "visitar_loja", "id": loja_id})
        if servicos.get("taverna"):
            acoes.append({"texto": "Entrar na taverna", "acao": "visitar_taverna"})
        if servicos.get("templo"):
            acoes.append({"texto": "Visitar o templo", "acao": "visitar_templo"})

        acoes.append({"texto": "Sair da cidade", "acao": "sair"})

        print("\nO que você deseja fazer?")
        for i, item_acao in enumerate(acoes):
            print(f"[{i+1}] {item_acao['texto']}")

        # --- Obter e Processar Entrada ---
        try:
            escolha = int(input("> ")) - 1
            if 0 <= escolha < len(acoes):
                acao_escolhida = acoes[escolha]

                if acao_escolhida["acao"] == "sair":
                    # Define a nova localização do personagem para a área de onde ele veio
                    # (Lógica simplificada, assume que sempre volta para as planícies)
                    estado_jogo.personagem.localizacao_atual = "plains_de_havenwood"
                    print(f"\nVocê sai de {dados_cidade['nome']} e retorna para as planícies.")
                    ui_utils.pausar_tela()
                    break
                else:
                    # Placeholder para outras ações
                    print(f"\nExecutando ação: {acao_escolhida['acao']} (ID: {acao_escolhida.get('id', 'N/A')})")
                    print("(Funcionalidade a ser implementada)")
                    ui_utils.pausar_tela()
            else:
                print("Escolha inválida.")
                ui_utils.pausar_tela()
        except (ValueError, TypeError):
            print("Entrada inválida.")
            ui_utils.pausar_tela()


# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
import unittest
from unittest.mock import patch, MagicMock

class TestTelaCidade(unittest.TestCase):
    def setUp(self):
        # Mock do EstadoJogo e Personagem
        self.mock_personagem = MagicMock()
        self.mock_personagem.localizacao_atual = "cidade_teste"
        self.mock_estado_jogo = MagicMock()
        self.mock_estado_jogo.personagem = self.mock_personagem

        # Mock do Banco de Dados de Cidades
        self.mock_db_cidades = {
            "by_id": {
                "cidade_teste": {
                    "nome": "Cidade Teste",
                    "descricao": "Uma cidade para testes.",
                    "servicos": {
                        "lojas": ["ferreiro_teste"],
                        "taverna": True,
                        "templo": False
                    }
                }
            }
        }

    @patch('builtins.input', side_effect=['1', '3']) # 1 (Visitar loja), 3 (Sair)
    @patch('builtins.print')
    def test_fluxo_interativo_cidade(self, mock_print, mock_input):
        """Verifica se o menu da cidade é gerado e se as ações são processadas."""
        mock_ui_utils = MagicMock()

        exibir_cidade(
            estado_jogo=self.mock_estado_jogo,
            db_cidades=self.mock_db_cidades,
            ui_utils=mock_ui_utils
        )

        # Verifica se o menu foi impresso corretamente
        mock_print.assert_any_call("[1] Visitar a loja: ferreiro_teste")
        mock_print.assert_any_call("[2] Entrar na taverna")
        mock_print.assert_any_call("[3] Sair da cidade")

        # Verifica se o placeholder da ação foi chamado
        mock_print.assert_any_call("\nExecutando ação: visitar_loja (ID: ferreiro_teste)")

        # Verifica se a localização do personagem foi alterada ao sair
        self.assertEqual(self.mock_personagem.localizacao_atual, "plains_de_havenwood")

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    unittest.main(verbosity=2)
