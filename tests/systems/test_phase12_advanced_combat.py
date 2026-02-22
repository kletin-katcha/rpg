import unittest

from rpg.game import Game
from rpg.systems.character.service import criar_personagem
from rpg.systems.combat.service import criar_inimigo, combater_ate_fim
from rpg.systems.combat.rules import resolver_turno
from rpg.core.types import CombatContext


class TestPhase12AdvancedCombat(unittest.TestCase):
    def test_inimigo_com_arquetipo_e_velocidade(self):
        inimigo = criar_inimigo("goblin_batedor")
        self.assertEqual(inimigo.arquetipo, "venenoso")
        self.assertGreater(inimigo.velocidade, 0)

    def test_turno_com_iniciativa(self):
        p = criar_personagem("Arin", "humano", "guerreiro")
        p.atributos["destreza"] = 1
        inimigo = criar_inimigo("goblin_batedor")
        hp_antes = p.hp_atual
        resolver_turno(CombatContext(personagem=p, inimigo=inimigo))
        self.assertLess(p.hp_atual, hp_antes)

    def test_boss_multi_fase(self):
        p = criar_personagem("Lia", "elfo", "mago")
        inv = {}
        out = combater_ate_fim(p, "ogro_alfa", inv)
        self.assertIn("fase_final_inimigo", out)
        self.assertGreaterEqual(out["fase_final_inimigo"], 1)

    def test_integracao_game_cacar_boss(self):
        g = Game()
        g.criar_jogador("Noah", "humano", "guerreiro")
        msg = g.executar_acao_cidade("cacar_boss")
        self.assertIn("Boss derrotado", msg)


if __name__ == "__main__":
    unittest.main()
