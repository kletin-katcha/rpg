import unittest

from rpg.game import Game
from rpg.systems.expansion import validar_estado_expansao


class TestPhase21To25Diagnostics(unittest.TestCase):
    def test_validar_estado_expansao_ok(self):
        out = validar_estado_expansao(
            {
                "energia_viagem": 6,
                "regiao_atual": "vila_aurora",
                "regioes_descobertas": {"vila_aurora"},
                "dungeon_ativa": None,
                "arco_longo": None,
            }
        )
        self.assertTrue(out["ok"])

    def test_validar_estado_expansao_com_erros(self):
        out = validar_estado_expansao(
            {
                "energia_viagem": 99,
                "regiao_atual": "mapa_invalido",
                "regioes_descobertas": set(),
                "dungeon_ativa": {"regiao": "x", "salas": 0},
                "arco_longo": {"ato": 10, "max_atos": 3},
            }
        )
        self.assertFalse(out["ok"])
        self.assertGreaterEqual(len(out["erros"]), 3)

    def test_acao_diagnostico_fases_1_25(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        msg = g.executar_acao_cidade("diagnostico_fases_1_25")
        self.assertIn("Diagnóstico 1-25", msg)
        self.assertIn("fase25_expansao_ok", msg)


if __name__ == "__main__":
    unittest.main()
