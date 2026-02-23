import unittest
from unittest.mock import patch

from rpg.main import _normalizar_escolha, _escolher_opcao


class TestMainCliResilience(unittest.TestCase):
    def test_normalizar_escolha(self):
        self.assertEqual(_normalizar_escolha("  Guerreiro  "), "guerreiro")
        self.assertEqual(_normalizar_escolha("Elfo Negro"), "elfo_negro")

    def test_escolher_opcao_repite_ate_valida(self):
        with patch("builtins.input", side_effect=["inválida", "humano"]):
            out = _escolher_opcao("Escolha raça: ", ["humano", "elfo"])
        self.assertEqual(out, "humano")

    def test_escolher_opcao_eof_retorna_none(self):
        with patch("builtins.input", side_effect=EOFError):
            out = _escolher_opcao("Escolha classe: ", ["guerreiro", "mago"])
        self.assertIsNone(out)


if __name__ == "__main__":
    unittest.main()
