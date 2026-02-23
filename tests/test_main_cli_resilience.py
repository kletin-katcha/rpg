import unittest
from unittest.mock import patch

from rpg.main import _normalizar_escolha, _escolher_item_numerado


class TestMainCliResilience(unittest.TestCase):
    def test_normalizar_escolha(self):
        self.assertEqual(_normalizar_escolha("  Guerreiro  "), "guerreiro")
        self.assertEqual(_normalizar_escolha("Elfo Negro"), "elfo_negro")

    def test_escolher_item_numerado_repite_ate_valida(self):
        opcoes = [{"id": "humano", "nome": "Humano"}, {"id": "elfo", "nome": "Elfo"}]
        with patch("builtins.input", side_effect=["inválida", "2"]):
            out = _escolher_item_numerado("Escolha raça: ", opcoes)
        self.assertEqual(out["id"], "elfo")

    def test_escolher_item_numerado_eof_retorna_none(self):
        opcoes = [{"id": "guerreiro", "nome": "Guerreiro"}, {"id": "mago", "nome": "Mago"}]
        with patch("builtins.input", side_effect=EOFError):
            out = _escolher_item_numerado("Escolha classe: ", opcoes)
        self.assertIsNone(out)


if __name__ == "__main__":
    unittest.main()
