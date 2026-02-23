import unittest

from rpg.core.errors import RPGError, RegraNegocioError, RecursoInsuficienteError
from rpg.core.types import CharacterState, EnemyState, CombatContext, CombatResult


class TestCoreContracts(unittest.TestCase):
    def test_character_state_minimo(self):
        p = CharacterState(id="p1", nome="Arin")
        self.assertEqual(p.id, "p1")
        self.assertEqual(p.nivel, 1)
        self.assertEqual(p.hp_max, 100)

    def test_combat_payloads(self):
        p = CharacterState(id="p1", nome="Arin")
        e = EnemyState(id="e1", nome="Lobo")
        ctx = CombatContext(personagem=p, inimigo=e)
        out = CombatResult(10, 3, False, False)
        self.assertEqual(ctx.acao, "ataque_basico")
        self.assertEqual(out.dano_causado, 10)

    def test_hierarquia_erros(self):
        self.assertTrue(issubclass(RegraNegocioError, RPGError))
        self.assertTrue(issubclass(RecursoInsuficienteError, RegraNegocioError))


if __name__ == "__main__":
    unittest.main()
