import unittest

from rpg.game import Game


class TestGameFlow(unittest.TestCase):
    def test_criacao_de_personagem_altera_estado(self):
        game = Game()
        jogador = game.criar_jogador("Arin", "elfo", "mago")
        self.assertEqual(jogador.nome, "Arin")
        self.assertEqual(game.state.etapa, "cidade")
        self.assertIsNotNone(game.state.jogador)

    def test_acao_cidade_coletar_item(self):
        game = Game()
        game.criar_jogador("Brom", "humano", "guerreiro")
        out = game.executar_acao_cidade("coletar_item_inicial")
        self.assertIn("Poção de Cura", out)
        self.assertEqual(game.state.inventario.get("pocao_cura"), 1)

    def test_acao_cidade_caca_lobo(self):
        game = Game()
        game.criar_jogador("Noah", "humano", "guerreiro")
        out = game.executar_acao_cidade("cacar_lobo")
        self.assertIn("Combate concluído", out)

    def test_fluxo_automacao_fase3(self):
        game = Game()
        game.criar_jogador("Nia", "humano", "guerreiro")
        game.executar_acao_cidade("construir_nucleo_automacao")
        game.executar_acao_cidade("construir_oficina")
        game.executar_acao_cidade("ativar_automacao")
        game.executar_acao_cidade("avancar_dia")
        self.assertIn("sucata_metal", game.state.inventario)

    def test_acao_cidade_sair(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        out = game.executar_acao_cidade("sair")
        self.assertIn("Saindo", out)
        self.assertFalse(game.running)


if __name__ == "__main__":
    unittest.main()
