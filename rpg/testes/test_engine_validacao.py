import unittest

from rpg import engine


class TestEngineValidacao(unittest.TestCase):
    def test_nome_invalido(self):
        with self.assertRaises(ValueError):
            engine.criar_personagem("   ")

    def test_sub_raca_sem_raca(self):
        p = engine.criar_personagem("Lia")
        with self.assertRaises(ValueError):
            engine.aplicar_sub_raca(p, "nordico")


if __name__ == "__main__":
    unittest.main()
