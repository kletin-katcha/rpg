import unittest

from rpg.game import Game
from rpg.systems.meta_world import gerar_crise_urbana


class TestPhase20UrbanCrisis(unittest.TestCase):
    def test_gerar_crise_por_conflito_e_tempestade(self):
        crise = gerar_crise_urbana({"status": "conflito"}, "tempestade_arcana")
        self.assertEqual(crise["tipo"], "saques_arcanos")
        self.assertEqual(crise["impacto_ouro"], -20)

    def test_game_gera_crise_e_aplica_ouro(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.state.tensao_faccoes = {"status": "conflito"}
        game.state.clima = "tempestade_arcana"
        ouro_antes = game.state.cidade.ouro

        msg = game.executar_acao_cidade("gerar_crise_urbana")

        self.assertIn("Crise urbana gerada", msg)
        self.assertEqual(game.state.cidade.ouro, ouro_antes - 20)

    def test_game_ver_crise(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        msg = game.executar_acao_cidade("ver_crise_urbana")
        self.assertIn("Crise urbana atual", msg)


if __name__ == "__main__":
    unittest.main()
