import unittest

from rpg.game import Game


class TestLegacyCharacterCreation(unittest.TestCase):
    def test_criacao_legada(self):
        g = Game()
        p = g.criar_jogador("Arin", "humano", "guerreiro")
        self.assertEqual(p.nome, "Arin")


if __name__ == "__main__":
    unittest.main()
