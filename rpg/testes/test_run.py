import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path para permitir importações relativas
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.main import main as game_main
from rpg.io import salvar_carregar

class TestGameFlow(unittest.TestCase):
    """
    Testa o fluxo principal do jogo de ponta a ponta.
    """

    SAVE_FILE_NAME = "test_save_run"
    SAVE_FILE_PATH = os.path.join(salvar_carregar.SAVE_DIR, f"{SAVE_FILE_NAME}.json")

    def setUp(self):
        """Garante que não há saves antigos antes de cada teste."""
        if os.path.exists(self.SAVE_FILE_PATH):
            os.remove(self.SAVE_FILE_PATH)

    def tearDown(self):
        """Limpa os arquivos de save criados durante o teste."""
        if os.path.exists(self.SAVE_FILE_PATH):
            os.remove(self.SAVE_FILE_PATH)

    @patch('rpg.main.random')
    def test_smoke_test_full_run(self, mock_random):
        """
        Teste de fumaça (smoke test) que simula uma execução completa e determinística do jogo.
        """
        # Configura o comportamento do random para ser determinístico
        mock_random.random.return_value = 0.1 # Sempre encontra um monstro
        mock_random.choice.return_value = 'goblin_batedor' # Sempre o alvo da quest

        # Sequência de inputs do usuário para simular uma jogada completa da quest
        user_inputs = [
            '1',  # 1. Menu: Novo Jogo
            'Jules', # 2. Nome do Personagem
            '1',  # 3. Falar com Elara (Pega quest 1 e 2)
        ]

        # Loop para matar 5 goblins
        for _ in range(5):
            user_inputs.append('2') # Explorar
            # Adiciona 15 ataques para garantir a vitória contra um goblin (220 HP / 15 de dano)
            user_inputs.extend(['1'] * 15)

        # Continua com o resto do fluxo do jogo
        user_inputs.extend([
            '1',  # Falar com Elara (Completar quest 2, pegar quest 3)
            '3',  # Ver Diário de Missões
            '5',  # Salvar Jogo
            self.SAVE_FILE_NAME, # Nome do save
            '6',  # Sair para o Menu Principal
            '2',  # Menu: Carregar Jogo
            '1',  # Escolher o primeiro save
            '6',  # Sair para o Menu Principal
            '3',  # Menu: Sair do jogo
        ])

        with patch('builtins.input', side_effect=user_inputs), \
             patch('rpg.utilitarios.funcoes_gerais.limpar_tela', MagicMock()), \
             patch('rpg.utilitarios.narrador.narrar', MagicMock()), \
             patch('rpg.utilitarios.funcoes_gerais.pausar', MagicMock()):
            try:
                game_main()
            except StopIteration:
                pass
            except Exception as e:
                self.fail(f"O jogo quebrou com a exceção inesperada: {e}")

        self.assertTrue(os.path.exists(self.SAVE_FILE_PATH), "O arquivo de save não foi criado.")


if __name__ == '__main__':
    unittest.main()
