import unittest

from rpg.io import criacao_personagem as cc_api


class TestExpansaoCatalogos(unittest.TestCase):
    def test_racas_expandidas_disponiveis(self):
        racas = cc_api.get_dados_racas()
        self.assertIn("fae", racas)
        self.assertIn("draconato", racas)

    def test_classes_extras_disponiveis(self):
        classes = cc_api.get_dados_classes()
        self.assertIn("sentinela_runico", classes)
        self.assertIn("arcanista_de_campo", classes)

    def test_todas_racas_tem_sub_racas(self):
        racas = cc_api.get_dados_racas()

        for id_raca in racas:
            sub_racas = cc_api.get_dados_sub_racas(id_raca)
            self.assertGreaterEqual(len(sub_racas), 1, f"Raça sem sub-raça: {id_raca}")



if __name__ == "__main__":
    unittest.main()
