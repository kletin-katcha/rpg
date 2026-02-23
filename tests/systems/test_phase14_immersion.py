import unittest

from rpg.game import Game
from rpg.systems.immersion import periodo_do_dia, avancar_tempo, atualizar_clima, registrar_jornal


class TestPhase14Immersion(unittest.TestCase):
    def test_periodo_do_dia(self):
        self.assertEqual(periodo_do_dia(8), "manha")
        self.assertEqual(periodo_do_dia(20), "noite")

    def test_avanco_tempo_e_clima(self):
        hora = avancar_tempo(20, 6)
        self.assertEqual(hora, 2)
        self.assertIn(atualizar_clima(3), {"ensolarado", "chuvoso", "neblina", "tempestade_arcana"})

    def test_jornal_limita_tamanho(self):
        j = []
        for i in range(25):
            registrar_jornal(j, f"evento-{i}", limite=20)
        self.assertEqual(len(j), 20)
        self.assertEqual(j[0], "evento-5")

    def test_integracao_game_imersao(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        g.executar_acao_cidade("avancar_dia")
        msg_clima = g.executar_acao_cidade("ver_clima")
        msg_jornal = g.executar_acao_cidade("ver_jornal")
        msg_codex = g.executar_acao_cidade("ver_codex")
        self.assertIn("Clima atual", msg_clima)
        self.assertTrue(len(msg_jornal) > 0)
        self.assertIn("Codex desbloqueado", msg_codex)


if __name__ == "__main__":
    unittest.main()
