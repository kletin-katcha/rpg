import unittest

from rpg.core.errors import RegraNegocioError
from rpg.systems.city import (
    CityState,
    ativar_plano_automacao,
    construir_estrutura,
    melhorar_estrutura,
    processar_automacao,
)
from rpg.systems.crafting import forjar_receita


class TestPhase3CityCrafting(unittest.TestCase):
    def test_forja_receita(self):
        inv = {"sucata_metal": 3}
        forjar_receita(inv, "refino_barra_metal")
        self.assertEqual(inv.get("sucata_metal", 0), 0)
        self.assertEqual(inv.get("barra_metal", 0), 1)

    def test_construir_e_melhorar_estrutura(self):
        state = CityState(ouro=500)
        nivel = construir_estrutura(state, "oficina")
        self.assertEqual(nivel, 1)
        nivel2 = melhorar_estrutura(state, "oficina")
        self.assertEqual(nivel2, 2)

    def test_automacao_requer_estrutura(self):
        state = CityState()
        with self.assertRaises(RegraNegocioError):
            ativar_plano_automacao(state, "coleta_sucata")

    def test_automacao_gera_recurso_e_refino(self):
        state = CityState(ouro=1000)
        construir_estrutura(state, "nucleo_automacao")
        construir_estrutura(state, "oficina")
        ativar_plano_automacao(state, "coleta_sucata")

        inv = {}
        processar_automacao(state, inv)
        processar_automacao(state, inv)

        self.assertGreaterEqual(inv.get("barra_metal", 0), 1)


if __name__ == "__main__":
    unittest.main()
