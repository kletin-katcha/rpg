import unittest

from rpg.core.types import CombatContext
from rpg.game import Game
from rpg.systems.character.service import criar_personagem
from rpg.systems.combat.service import criar_inimigo
from rpg.systems.combat.rules import resolver_turno


class TestPhase17CombatConditions(unittest.TestCase):
    def test_contexto_aplica_bonus_e_reducao(self):
        personagem = criar_personagem("Arin", "humano", "guerreiro")
        inimigo = criar_inimigo("lobo_cinzento")

        hp_inimigo_antes = inimigo.hp_atual
        hp_personagem_antes = personagem.hp_atual

        resolver_turno(
            CombatContext(
                personagem=personagem,
                inimigo=inimigo,
                bonus_dano_personagem=2,
                reducao_dano_personagem=1,
                bonus_dano_inimigo=1,
            )
        )

        self.assertLess(inimigo.hp_atual, hp_inimigo_antes)
        self.assertLess(personagem.hp_atual, hp_personagem_antes)

    def test_mutadores_refletem_clima_periodo_e_mutador_global(self):
        jogo = Game()
        jogo.state.hora = 20
        jogo.state.clima = "tempestade_arcana"
        jogo.state.mutador_ativo = "escassez"

        mutadores = jogo.mutadores_combate_atuais()

        self.assertEqual(mutadores["bonus_dano_personagem"], 0)
        self.assertEqual(mutadores["reducao_dano_personagem"], 0)
        self.assertEqual(mutadores["bonus_dano_inimigo"], 3)

    def test_acao_ver_condicoes_combate(self):
        jogo = Game()
        jogo.criar_jogador("Noah", "humano", "guerreiro")

        msg = jogo.executar_acao_cidade("ver_condicoes_combate")

        self.assertIn("Condições de combate atuais", msg)
        self.assertIn("bonus_dano_personagem", msg)


if __name__ == "__main__":
    unittest.main()
