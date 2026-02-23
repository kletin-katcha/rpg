import unittest

from rpg.main import _agrupar_acoes, _render_hud
from rpg.game import Game


class TestMainHudRender(unittest.TestCase):
    def test_agrupar_acoes(self):
        grupos = _agrupar_acoes([
            "cacar_lobo",
            "construir_oficina",
            "ver_status",
            "salvar",
        ])
        self.assertIn("Combate", grupos)
        self.assertIn("Economia/Cidade", grupos)
        self.assertIn("Mundo/Meta", grupos)
        self.assertIn("Sistema", grupos)

    def test_render_hud_contem_blocos(self):
        game = Game()
        game.criar_jogador("Nid", "elfo", "mago")
        hud = _render_hud(game)
        self.assertIn("RPG Surreal", hud)
        self.assertIn("Jogador: Nid", hud)
        self.assertIn("[Combate]", hud)
        self.assertIn("Atalhos:", hud)


if __name__ == "__main__":
    unittest.main()
