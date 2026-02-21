import unittest

from rpg.dados.cidade.opcoes_cidade import OPCOES_CIDADE_BASE


class TestDadosCidade(unittest.TestCase):
    def test_opcoes_cidade_contam_treino_e_forja(self):
        self.assertIn("Treinar Classe Secundária (Protótipo)", OPCOES_CIDADE_BASE)
        self.assertIn("Usar Forja (Protótipo)", OPCOES_CIDADE_BASE)


if __name__ == "__main__":
    unittest.main()
