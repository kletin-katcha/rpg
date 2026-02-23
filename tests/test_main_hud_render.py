import unittest

from rpg.main import _render_hud, _normalizar_escolha
from rpg.game import Game


class TestMainHudRender(unittest.TestCase):
    def test_normalizar_escolha(self):
        self.assertEqual(_normalizar_escolha("Humano"), "humano")
        self.assertEqual(_normalizar_escolha("Elfo da Floresta"), "elfo_da_floresta")

    def test_render_hud_contem_blocos(self):
        game = Game()
        game.criar_jogador("Nid", "elfo", "mago")
        hud = _render_hud(game)
        self.assertIn("RPG Surreal", hud)
        self.assertIn("Jogador: Nid", hud)
        self.assertIn("Sub-raça", hud)
        self.assertIn("ATRIBUTOS / STATUS", hud)
        self.assertIn("[Combate]", hud)
        self.assertIn("Atalhos:", hud)


if __name__ == "__main__":
    unittest.main()
