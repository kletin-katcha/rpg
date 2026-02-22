import unittest

from rpg.game import Game


class TestPhase4GameUx(unittest.TestCase):
    def test_aliases_de_acao(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        out = game.executar_acao_cidade("lobo")
        self.assertIn("Combate concluído", out)

    def test_help_e_historico(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        ajuda = game.executar_acao_cidade("help")
        self.assertIn("Ações disponíveis", ajuda)
        hist = game.executar_acao_cidade("historico")
        self.assertTrue(len(hist) > 0)


if __name__ == "__main__":
    unittest.main()
