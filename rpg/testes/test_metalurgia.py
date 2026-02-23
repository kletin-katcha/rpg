import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas import metalurgia
from rpg.game_manager import GameManager


class TestMetalurgiaMVP(unittest.TestCase):
    def test_fundir_sucata_em_barra(self):
        jogador = Personagem("Ferreiro")
        jogador.adicionar_item("caco_de_arma_enferrujada", 3)

        logs = metalurgia.fundir_sucata_em_barra(jogador)

        self.assertIn("fundiu sucata", logs[0])
        self.assertNotIn("caco_de_arma_enferrujada", jogador.inventario)
        self.assertIn("barra_metal_reciclado", jogador.inventario)
        self.assertEqual(jogador.inventario["barra_metal_reciclado"]["quantidade"], 1)

    def test_forjar_lamina_requer_duas_barras(self):
        jogador = Personagem("Ferreiro")
        jogador.adicionar_item("barra_metal_reciclado", 1)

        logs = metalurgia.forjar_lamina_reciclada(jogador)

        self.assertIn("2x barra_metal_reciclado", logs[0])
        self.assertNotIn("lamina_reciclada", jogador.inventario)

    def test_opcao_forja_no_game_manager(self):
        gm = GameManager()
        gm.jogador = Personagem("Aventureiro")
        gm.game_state = "in_game"
        gm.jogador.adicionar_item("caco_de_arma_enferrujada", 6)

        resultado = gm.executar_opcao_cidade("Usar Forja (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "feedback")
        arma = gm.jogador.equipamentos.get("arma_principal")
        self.assertIsNotNone(arma)
        self.assertEqual(arma.id_item, "lamina_reciclada")

    def test_opcao_forja_equipe_arma_se_slot_vazio(self):
        gm = GameManager()
        gm.jogador = Personagem("Aventureiro")
        gm.game_state = "in_game"
        gm.jogador.adicionar_item("caco_de_arma_enferrujada", 6)

        gm.executar_opcao_cidade("Usar Forja (Protótipo)")

        arma = gm.jogador.equipamentos.get("arma_principal")
        self.assertIsNotNone(arma)
        self.assertEqual(arma.id_item, "lamina_reciclada")

    def test_acao_contextual_forjar_machadinha(self):
        gm = GameManager()
        gm.jogador = Personagem("Aventureiro")
        gm.game_state = "in_game"
        gm.jogador.adicionar_item("barra_metal_reciclado", 2)

        resultado = gm.executar_acao_contextual("forjar_machadinha")

        self.assertEqual(resultado.get("tipo"), "feedback")
        arma = gm.jogador.equipamentos.get("arma_principal")
        self.assertIsNotNone(arma)
        self.assertEqual(arma.id_item, "machadinha_reciclada")

    def test_forjar_machadinha_requer_duas_barras(self):
        jogador = Personagem("Ferreiro")
        jogador.adicionar_item("barra_metal_reciclado", 1)

        logs = metalurgia.forjar_machadinha_reciclada(jogador)

        self.assertIn("2x barra_metal_reciclado", logs[0])
        self.assertNotIn("machadinha_reciclada", jogador.inventario)


if __name__ == "__main__":
    unittest.main()
