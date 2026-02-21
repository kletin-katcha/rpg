import unittest

from rpg.dados.metalurgia import RECEITA_BARRA_RECICLADA, RECEITA_LAMINA_RECICLADA, RECEITA_MACHADINHA_RECICLADA


class TestDadosMetalurgia(unittest.TestCase):
    def test_receitas_basicas_possuem_entrada_e_saida(self):
        for receita in (RECEITA_BARRA_RECICLADA, RECEITA_LAMINA_RECICLADA, RECEITA_MACHADINHA_RECICLADA):
            self.assertIn("entrada", receita)
            self.assertIn("saida", receita)
            self.assertGreater(len(receita["entrada"]), 0)
            self.assertGreater(len(receita["saida"]), 0)


if __name__ == "__main__":
    unittest.main()
