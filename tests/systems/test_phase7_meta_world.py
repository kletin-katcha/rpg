import unittest

from rpg.game import Game
from rpg.systems.meta_world import gerar_contrato_aleatorio, iniciar_reputacoes, aplicar_evento_mundo


class TestPhase7MetaWorld(unittest.TestCase):
    def test_reputacoes_iniciais(self):
        reps = iniciar_reputacoes()
        self.assertIn("guilda_ferreiros", reps)

    def test_evento_mundo_retorna_payload(self):
        out = aplicar_evento_mundo(100)
        self.assertIn("evento", out)
        self.assertIn("ouro", out)

    def test_contrato_aleatorio(self):
        c = gerar_contrato_aleatorio()
        self.assertIn("xp", c)
        self.assertIn("ouro", c)

    def test_integracao_game_acoes_meta(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        msg = g.executar_acao_cidade("faccao_status")
        self.assertIn("Reputações", msg)


if __name__ == "__main__":
    unittest.main()
