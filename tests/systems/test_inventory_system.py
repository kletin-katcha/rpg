import unittest

from rpg.core.errors import RegraNegocioError, RecursoInsuficienteError
from rpg.systems.inventory.service import adicionar_item_catalogado, remover_item_catalogado


class TestInventorySystem(unittest.TestCase):
    def test_add_item_catalogado(self):
        inv = {}
        adicionar_item_catalogado(inv, "espada_curta", 2)
        self.assertEqual(inv["espada_curta"], 2)

    def test_add_item_inexistente(self):
        with self.assertRaises(RegraNegocioError):
            adicionar_item_catalogado({}, "item_inexistente", 1)

    def test_remocao_com_falta_recurso(self):
        with self.assertRaises(RecursoInsuficienteError):
            remover_item_catalogado({"pocao_cura": 1}, "pocao_cura", 2)


if __name__ == "__main__":
    unittest.main()
