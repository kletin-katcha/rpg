import unittest

from rpg.game import Game
from rpg.systems.economy import iniciar_mercado, atualizar_mercado, vender_item, produzir_liga_metal


class TestPhase13Economy(unittest.TestCase):
    def test_mercado_dinamico_muda_com_dia(self):
        mercado = iniciar_mercado()
        original = dict(mercado)
        atualizar_mercado(mercado, 2)
        self.assertNotEqual(original, mercado)

    def test_venda_item_converte_em_ouro(self):
        mercado = iniciar_mercado()
        inventario = {"sucata_metal": 2}
        ouro = vender_item(inventario, 100, "sucata_metal", 1, mercado)
        self.assertGreater(ouro, 100)
        self.assertEqual(inventario.get("sucata_metal"), 1)

    def test_cadeia_producao_liga(self):
        inventario = {"barra_metal": 2}
        produzir_liga_metal(inventario)
        self.assertEqual(inventario.get("liga_metal"), 1)

    def test_integracao_game_acoes_economia(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        g.state.inventario["sucata_metal"] = 2
        msg_mercado = g.executar_acao_cidade("ver_mercado")
        self.assertIn("Mercado", msg_mercado)
        msg_venda = g.executar_acao_cidade("vender_sucata")
        self.assertIn("Venda concluída", msg_venda)


if __name__ == "__main__":
    unittest.main()
