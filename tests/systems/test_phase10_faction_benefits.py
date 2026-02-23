import unittest

from rpg.game import Game
from rpg.systems.meta_world import resgatar_beneficio_faccao


class TestPhase10FactionBenefits(unittest.TestCase):
    def test_beneficio_guilda_ferreiros_adiciona_item(self):
        reputacoes = {"guilda_ferreiros": 10}
        inventario = {}
        out = resgatar_beneficio_faccao(reputacoes, inventario, 100, "guilda_ferreiros")
        self.assertEqual(out["beneficio"], "item")
        self.assertEqual(inventario.get("sucata_metal"), 2)

    def test_integracao_game_resgate(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.state.reputacoes["guilda_ferreiros"] = 12
        msg = game.executar_acao_cidade("resgatar_beneficio_faccao")
        self.assertIn("Benefício de facção", msg)


if __name__ == "__main__":
    unittest.main()
