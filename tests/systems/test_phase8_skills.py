import unittest

from rpg.game import Game
from rpg.systems.skills import habilidades_disponiveis, desbloquear_habilidade


class TestPhase8Skills(unittest.TestCase):
    def test_fluxo_basico_desbloqueio(self):
        g = Game()
        jogador = g.criar_jogador("Arin", "humano", "guerreiro")

        self.assertEqual(habilidades_disponiveis(jogador), ["postura_ofensiva"])
        desbloquear_habilidade(jogador, "postura_ofensiva")
        self.assertIn("postura_ofensiva", jogador.habilidades_desbloqueadas)
        self.assertIn("golpe_reforcado", habilidades_disponiveis(jogador))

    def test_integracao_acoes_game(self):
        g = Game()
        g.criar_jogador("Lia", "elfo", "mago")
        msg_arvore = g.executar_acao_cidade("ver_arvore")
        self.assertIn("Combate Base", msg_arvore)

        msg_unlock = g.executar_acao_cidade("desbloquear_postura_ofensiva")
        self.assertIn("Habilidade desbloqueada", msg_unlock)


if __name__ == "__main__":
    unittest.main()
