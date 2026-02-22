import unittest

from rpg.core.errors import RegraNegocioError
from rpg.systems.character.service import criar_personagem, conceder_xp


class TestCharacterSystem(unittest.TestCase):
    def test_criar_personagem_com_bonus_racial(self):
        p = criar_personagem("Arin", "elfo", "mago")
        self.assertEqual(p.nome, "Arin")
        self.assertEqual(p.atributos["destreza"], 6)
        self.assertEqual(p.atributos["inteligencia"], 6)

    def test_criar_personagem_nome_vazio(self):
        with self.assertRaises(RegraNegocioError):
            criar_personagem("  ", "humano", "guerreiro")

    def test_conceder_xp_sobe_nivel(self):
        p = criar_personagem("Brom", "humano", "guerreiro")
        conceder_xp(p, 120)
        self.assertEqual(p.nivel, 2)
        self.assertEqual(p.xp, 20)
        self.assertEqual(p.hp_atual, p.hp_max)


if __name__ == "__main__":
    unittest.main()
