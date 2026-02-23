import unittest

from rpg.systems.character.service import criar_personagem
from rpg.systems.combat.service import combater_ate_fim, criar_inimigo


class TestCombatSystem(unittest.TestCase):
    def test_criar_inimigo(self):
        e = criar_inimigo("lobo_cinzento")
        self.assertEqual(e.nivel, 1)
        self.assertGreater(e.hp_max, 0)

    def test_combate_gera_xp_e_loot(self):
        p = criar_personagem("Arin", "humano", "guerreiro")
        inv = {}
        out = combater_ate_fim(p, "lobo_cinzento", inv)
        self.assertTrue(out["vitoria"])
        self.assertGreater(out["xp_recebido"], 0)
        self.assertIn("pocao_cura", inv)
        self.assertTrue(len(out["log_turnos"]) >= 1)
        self.assertIn("dano_causado", out["log_turnos"][0])


if __name__ == "__main__":
    unittest.main()
