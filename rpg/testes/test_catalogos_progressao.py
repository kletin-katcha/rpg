import unittest

from rpg.io import criacao_personagem as cc_api


class TestCatalogosProgressao(unittest.TestCase):
    def test_catalogo_progressao_tem_blocos(self):
        catalogo = cc_api.get_catalogo_classes_progressao()
        self.assertIn("iniciais", catalogo)
        self.assertIn("evolucoes", catalogo)
        self.assertIn("secretas", catalogo)
        self.assertIn("side_quests_secretas", catalogo)

    def test_classes_secretas_referenciam_side_quests(self):
        catalogo = cc_api.get_catalogo_classes_progressao()
        side_quests = catalogo["side_quests_secretas"]
        for _id, dados in catalogo["secretas"].items():
            self.assertIn(dados["side_quest"], side_quests)


if __name__ == "__main__":
    unittest.main()
