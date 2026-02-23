import unittest

from rpg.systems.balance import gerar_relatorio_balance, simular_rodada_combate


class TestPhase5Balance(unittest.TestCase):
    def test_simulacao_retorna_metricas(self):
        out = simular_rodada_combate("Bot", "humano", "guerreiro", ["lobo_cinzento"])
        self.assertIn("turno_medio", out)
        self.assertIn("xp_total", out)

    def test_relatorio_sanidade(self):
        r = gerar_relatorio_balance()
        self.assertIn("cenario_base", r)
        self.assertIn("sanidade", r)
        self.assertTrue(r["sanidade"]["ganhou_xp"])


if __name__ == "__main__":
    unittest.main()
