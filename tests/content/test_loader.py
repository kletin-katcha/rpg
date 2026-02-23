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
        self.assertIn("itens", all_data)

    def test_catalog_inexistente_lanca_erro(self):
        with self.assertRaises(ContentValidationError):
            load_catalog("nao_existe")


if __name__ == "__main__":
    unittest.main()
