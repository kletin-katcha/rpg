import unittest

from rpg.game import Game
from rpg.systems.meta_world import avaliar_tensao_faccoes


class TestPhase19FactionTension(unittest.TestCase):
    def test_avaliar_tensao_conflito(self):
        reputacoes = {"guilda_ferreiros": 10, "circulo_arcano": 9}
        tensao = avaliar_tensao_faccoes(reputacoes)
        self.assertEqual(tensao["status"], "conflito")
        self.assertEqual(tensao["efeito_ouro"], -10)

    def test_game_gera_tensao_aplica_efeito(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.state.reputacoes = {"guilda_ferreiros": 12, "circulo_arcano": 11}
        ouro_antes = game.state.cidade.ouro

        msg = game.executar_acao_cidade("gerar_tensao_faccoes")

        self.assertIn("Tensão de facções atualizada", msg)
        self.assertEqual(game.state.cidade.ouro, ouro_antes - 10)

    def test_game_ver_tensao(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")

        msg = game.executar_acao_cidade("ver_tensao_faccoes")

        self.assertIn("Tensão de facções", msg)
        self.assertIn("status", msg)


if __name__ == "__main__":
    unittest.main()
