import unittest

from rpg.content.loader import load_catalog


class TestPhase4CatalogExpansion(unittest.TestCase):
    def test_expansao_racas_classes(self):
        racas = load_catalog("racas")
        classes = load_catalog("classes")
        self.assertGreaterEqual(len(racas), 5)
        self.assertGreaterEqual(len(classes), 5)

    def test_arvores_habilidades_catalogo(self):
        arvores = load_catalog("arvores_habilidades")
        self.assertIn("combate_base", arvores)
        self.assertIn("magia_base", arvores)


if __name__ == "__main__":
    unittest.main()
