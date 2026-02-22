import unittest

from scripts.validar_referencias_content import validar_referencias


class TestPhase16ContentReferences(unittest.TestCase):
    def test_referencias_cruzadas_validas(self):
        validar_referencias()


if __name__ == "__main__":
    unittest.main()
