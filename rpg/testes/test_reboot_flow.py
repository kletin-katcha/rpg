import unittest

from rpg.game_manager import GameManager


class TestRebootFlow(unittest.TestCase):
    def test_fluxo_basico_criacao(self):
        gm = GameManager()
        gm.processar("Arin")
        gm.processar("humano")
        gm.processar("nordico")
        gm.processar("guerreiro")

        self.assertEqual(gm.estado.etapa, "fim")
        self.assertEqual(gm.jogador.nome, "Arin")
        self.assertEqual(gm.jogador.raca, "humano")
        self.assertEqual(gm.jogador.sub_raca, "nordico")
        self.assertEqual(gm.jogador.classe, "guerreiro")
        self.assertIn("ataque_poderoso", gm.jogador.habilidades)


if __name__ == "__main__":
    unittest.main()
