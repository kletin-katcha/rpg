# -*- coding: utf-8 -*-
"""
================================================================================================
TELA: MENU PRINCIPAL
================================================================================================
Este arquivo define a classe `MenuPrincipalTela`, que é responsável por gerenciar a
lógica e o fluxo de navegação do menu principal do jogo no modo terminal.

-------------------------
-- DESIGN DO SISTEMA --
-------------------------
- **Controlador de Fluxo:** Esta classe não é responsável pela renderização final
  (cores, formatação), mas sim pelo fluxo de controle. Ela exibe as opções,
  captura a entrada do usuário e orquestra as chamadas para os sistemas de back-end
  apropriados (como `GerenciadorSave` ou `CriadorPersonagem`).

- **Injeção de Dependência (Implícita):** A classe `MenuPrincipalTela` instancia os
  gerenciadores de sistema de que precisa (como `GerenciadorSave`). Em uma
  arquitetura mais complexa, essas dependências poderiam ser injetadas, mas para
  este estágio, a instanciação direta é suficiente.

- **Testabilidade com Mocks:** A lógica é projetada para ser facilmente testável.
  O bloco de teste (`if __name__ == "__main__"`) demonstra como usar `unittest.mock`
  para simular a entrada do usuário e para "espionar" as chamadas aos sistemas de
  back-end, garantindo que o fluxo está funcionando corretamente sem depender
  da execução real desses sistemas.
"""

# ==============================================================================================
# == SEÇÃO 1: IMPORTAÇÕES ======================================================================
# ==============================================================================================
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from datetime import datetime
try:
    # Importa as dependências chave dos sistemas do motor
    from rpg_colossal.motor_jogo.sistemas.gerenciador_save import GerenciadorSave, EstadoJogo
    from rpg_colossal.motor_jogo.sistemas.criador_personagem import CriadorPersonagem
    from rpg_colossal.motor_jogo.utilitarios import funcoes_gerais as geral
except ImportError:
    # Mocks para permitir a execução independente e testes
    class GerenciadorSave:
        def listar_saves(self): return []
        def carregar_jogo(self, slot): return None
    class CriadorPersonagem:
        def iniciar_criacao(self): return None
    class EstadoJogo:
        def __init__(self, personagem, estado_mundo, metadata): pass
    class geral:
        def limpar_tela(): pass
        def carregar_arte_ascii(caminho): return "ARTE ASCII"

# ==============================================================================================
# == SEÇÃO 2: CLASSE DA TELA DO MENU PRINCIPAL =================================================
# ==============================================================================================
class MenuPrincipalTela:
    """
    Gerencia a lógica de interação do menu principal.
    """
    def __init__(self):
        self.gerenciador_save = GerenciadorSave()
        self.criador_personagem = CriadorPersonagem()
        # Define o caminho para a arte do título
        self.caminho_arte_titulo = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'ascii_art', 'titulo.txt')
        self.arte_titulo = geral.carregar_arte_ascii(self.caminho_arte_titulo)


    def exibir(self) -> EstadoJogo | str | None:
        """
        Exibe o menu principal e processa a entrada do usuário em um loop.
        Retorna um objeto EstadoJogo se um jogo for iniciado/carregado,
        ou uma string 'sair' se o usuário escolher sair.
        """
        opcoes_menu = {
            '1': 'Novo Jogo',
            '2': 'Carregar Jogo',
            '3': 'Opções',
            '4': 'Sair ⚔️',
        }

        while True:
            geral.limpar_tela()
            print("=" * 80)
            print(self.arte_titulo)
            print("=" * 80)
            print("\n" * 2)

            print(" " * 30 + "MENU PRINCIPAL")
            print(" " * 30 + "--------------")
            for key, value in opcoes_menu.items():
                print(f" " * 30 + f"[{key}] - {value}")
            print("\n" * 2)

            escolha = input(" " * 25 + "Escolha uma opção e pressione Enter: ")

            if escolha == '1':
                estado_jogo = self._novo_jogo()
                if estado_jogo:
                    return estado_jogo
            elif escolha == '2':
                estado_jogo = self._carregar_jogo()
                if estado_jogo:
                    return estado_jogo
            elif escolha == '3':
                print("\n" + " " * 25 + "Opção ainda não implementada.")
                geral.pausar_tela()
            elif escolha == '4':
                print("\n" + " " * 25 + "Obrigado por jogar Ecos da Aetheria!")
                return "sair"
            else:
                print("\n" + " " * 25 + "Opção inválida. Por favor, tente novamente.")
                geral.pausar_tela()

    def _novo_jogo(self) -> EstadoJogo | None:
        """
        Inicia o fluxo de criação de um novo personagem e o encapsula em um EstadoJogo.
        """
        print("\nIniciando um novo jogo...")
        novo_personagem = self.criador_personagem.iniciar_criacao()

        if novo_personagem:
            # Cria um estado de jogo inicial para o novo personagem
            estado_jogo = EstadoJogo(
                personagem=novo_personagem,
                estado_mundo={"chefes_derrotados": [], "eventos_concluidos": []},
                metadata={"timestamp": datetime.now(), "tempo_de_jogo_segundos": 0}
            )
            return estado_jogo
        return None

    def _carregar_jogo(self) -> EstadoJogo | None:
        """
        Gerencia o fluxo de carregamento de um jogo salvo.
        """
        print("\n--- Carregar Jogo ---")
        saves = self.gerenciador_save.listar_saves()

        if not saves:
            print("Nenhum jogo salvo encontrado.")
            return None

        print("Slots de save disponíveis:")
        for save in saves:
            # Tenta formatar o timestamp, mas usa um fallback se não for um datetime real (ex: em mocks)
            try:
                timestamp_str = datetime.fromisoformat(save.get('metadata', {}).get('timestamp')).strftime('%Y-%m-%d %H:%M:%S')
            except:
                timestamp_str = save.get('metadata', {}).get('timestamp', 'Data desconhecida')
            print(f"  Slot {save['slot']}: Salvo em {timestamp_str}")

        try:
            slot_escolhido = int(input("Digite o número do slot para carregar: "))

            if any(s['slot'] == slot_escolhido for s in saves):
                print(f"Carregando slot {slot_escolhido}...")
                estado_jogo = self.gerenciador_save.carregar_jogo(slot_escolhido)
                if estado_jogo:
                    print("Jogo carregado com sucesso!")
                    return estado_jogo
                else:
                    print("Falha ao carregar o jogo.")
            else:
                print("Slot inválido.")
        except (ValueError, TypeError):
            print("Entrada inválida. Por favor, digite um número.")

        return None

# ==============================================================================================
# == SEÇÃO 3: BLOCO DE TESTE E DEMONSTRAÇÃO ====================================================
# ==============================================================================================
if __name__ == "__main__":
    import unittest
    from unittest.mock import patch, MagicMock

    print("\n" + "="*80)
    print("== TESTES DO FLUXO DO MENU PRINCIPAL ==")
    print("="*80)

    class TestMenuPrincipal(unittest.TestCase):

        @patch('builtins.input', side_effect=['2', '1', '4']) # Simula: 2 (Carregar), 1 (Slot), 4 (Sair)
        @patch(__name__ + '.GerenciadorSave')
        def test_fluxo_carregar_jogo_sucesso(self, MockGerenciadorSave, mock_input):
            print("\n--- Testando o fluxo de carregar um jogo com sucesso ---")

            # Configura o mock do GerenciadorSave
            mock_instancia = MockGerenciadorSave.return_value
            mock_instancia.listar_saves.return_value = [
                {"slot": 1, "metadata": {"timestamp": "2025-01-01T12:00:00"}}
            ]
            mock_instancia.carregar_jogo.return_value = "Estado do Jogo Carregado"

            menu = MenuPrincipalTela()
            resultado = menu.exibir()

            # Verificações
            mock_instancia.listar_saves.assert_called_once()
            mock_instancia.carregar_jogo.assert_called_with(1)
            self.assertEqual(resultado, "sair")
            print("Teste de fluxo de carregamento bem-sucedido.")

        @patch('builtins.input', side_effect=['1', '4']) # Simula: 1 (Novo Jogo), 4 (Sair)
        def test_fluxo_novo_jogo(self, mock_input):
            print("\n--- Testando o fluxo de novo jogo (placeholder) ---")
            menu = MenuPrincipalTela()
            # O teste aqui apenas verifica se o loop termina corretamente
            # e se a função é chamada sem erros.
            resultado = menu.exibir()
            self.assertEqual(resultado, "sair")
            print("Teste de fluxo de novo jogo bem-sucedido.")

    # Executa os testes
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMenuPrincipal))
    runner = unittest.TextTestRunner()
    runner.run(suite)
