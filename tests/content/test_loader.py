import unittest

from rpg.content.loader import load_all_catalogs, load_catalog
from rpg.content.schemas.common import ContentValidationError


class TestContentLoader(unittest.TestCase):
    def test_load_catalog_racas(self):
        racas = load_catalog("racas")
        self.assertIn("humano", racas)
        self.assertEqual(racas["elfo"]["nome"], "Elfo")

    def test_load_all_catalogs(self):
        all_data = load_all_catalogs()
        self.assertIn("racas", all_data)
        self.assertIn("classes", all_data)
        self.assertIn("sub_racas", all_data)
        self.assertIn("itens", all_data)

    def test_sub_racas_por_raca(self):
        sub = load_catalog("sub_racas")
        self.assertIn("elfo_floresta", sub)
        self.assertEqual(sub["elfo_floresta"]["raca_id"], "elfo")

    def test_monstros_por_area_catalogados(self):
        monstros = load_catalog("monstros")
        self.assertIn("areas", monstros["lobo_cinzento"])
        self.assertIn("vila_aurora", monstros["lobo_cinzento"]["areas"])
        self.assertIn("ruinas_antigas", monstros["ogro_alfa"]["areas"])

    def test_catalog_inexistente_lanca_erro(self):
        with self.assertRaises(ContentValidationError):
            load_catalog("nao_existe")


if __name__ == "__main__":
    unittest.main()
