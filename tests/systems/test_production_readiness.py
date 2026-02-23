import unittest

from rpg.game import Game
from scripts.gate_kpis import coletar_kpis, avaliar


class TestProductionReadiness(unittest.TestCase):
    def test_rollback_criacao_restabelece_estado_base(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.executar_acao_cidade("coletar_item_inicial")
        game.executar_acao_cidade("construir_oficina")

        out = game.executar_acao_cidade("rollback_criacao")
        self.assertIn("Rollback aplicado", out)
        self.assertEqual(game.state.inventario, {})
        self.assertEqual(game.state.cidade.estruturas, {})
        self.assertEqual(game.state.jogador.nome, "Arin")

    def test_kpi_gate_snapshot_nao_retorna_erros(self):
        kpis = coletar_kpis()
        erros = avaliar(kpis)
        self.assertEqual(erros, [])


if __name__ == "__main__":
    unittest.main()
