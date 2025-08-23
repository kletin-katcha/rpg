import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path para permitir importações relativas
# Isso é necessário para rodar o teste diretamente, mas o ideal é usar `python -m unittest`
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
        O objetivo é garantir que o jogo não quebre em nenhum ponto do fluxo principal.
        """
        # Configura o comportamento do random para ser determinístico
        # Primeira exploração -> encontro. Demais -> sem encontro.
        mock_random.random.side_effect = [0.1, 0.9, 0.9, 0.9, 0.9, 0.9]
        # Sempre encontra o monstro mais fraco
        mock_random.choice.return_value = 'slime_verde'

        # Sequência de inputs do usuário para simular uma jogada determinística.
        user_inputs = [
            '1',  # 1. Menu: Novo Jogo
            'Jules', # 2. Nome do Personagem

            # Loop de jogo: A primeira exploração causa uma batalha com um Slime
            '1',  # 3. Explorar a floresta
        ]
        # Adiciona 26 ataques para garantir a vitória contra o Slime (280 HP / 11 de dano por golpe)
        user_inputs.extend(['1'] * 26)

        # Continua com o resto do fluxo do jogo
        user_inputs.extend([
            '1',  # Explorar novamente (sem encontro desta vez)
            '2',  # Ver status do personagem
            '3',  # Salvar Jogo
            self.SAVE_FILE_NAME, # Nome do save
            '4',  # Sair para o Menu Principal
            '2',  # Menu: Carregar Jogo
            '1',  # Escolher o primeiro save
            '4',  # Sair para o Menu Principal
            '3',  # Menu: Sair do jogo
        ])

        # Mockamos 'input', 'pausar', 'limpar_tela' e 'narrar'
        with patch('builtins.input', side_effect=user_inputs), \
             patch('rpg.utilitarios.funcoes_gerais.limpar_tela', MagicMock()), \
             patch('rpg.utilitarios.narrador.narrar', MagicMock()), \
             patch('rpg.utilitarios.funcoes_gerais.pausar', MagicMock()):
            try:
                # Executa a função principal do jogo
                game_main()
            except StopIteration:
                # É normal que o side_effect de input se esgote
                pass
            except Exception as e:
                self.fail(f"O jogo quebrou com a exceção inesperada: {e}")

        # Verificação final: o arquivo de save foi realmente criado?
        self.assertTrue(os.path.exists(self.SAVE_FILE_PATH), "O arquivo de save não foi criado.")


if __name__ == '__main__':
    unittest.main()
