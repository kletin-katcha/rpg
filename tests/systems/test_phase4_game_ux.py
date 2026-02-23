import unittest

from rpg.core.errors import RegraNegocioError
from rpg.game import Game


class TestPhase4GameUx(unittest.TestCase):
    def test_aliases_de_acao(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        out = game.executar_acao_cidade("lobo")
        self.assertIn("Combate concluído", out)

    def test_help_e_historico(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        ajuda = game.executar_acao_cidade("help")
        self.assertIn("Ajuda contextual", ajuda)
        self.assertIn("combate:", ajuda)
        hist = game.executar_acao_cidade("historico")
        self.assertTrue(len(hist) > 0)

    def test_metrica_comando_invalido(self):
        game = Game()
        game.criar_jogador("Teo", "humano", "guerreiro")
        with self.assertRaises(RegraNegocioError):
            game.executar_acao_cidade("acao_que_nao_existe")
        self.assertEqual(game.state.metricas_onboarding["comandos_invalidos"], 1)

    def test_busca_de_acoes(self):
        game = Game()
        game.criar_jogador("Iris", "humano", "guerreiro")
        out = game.executar_acao_cidade("buscar_acoes:cacar")
        self.assertIn("cacar_lobo", out)
        self.assertIn("cacar_goblin", out)

    def test_ver_log_combate(self):
        game = Game()
        game.criar_jogador("Ravi", "humano", "guerreiro")
        game.executar_acao_cidade("cacar_lobo")
        out = game.executar_acao_cidade("ver_log_combate")
        self.assertIn("Log combate", out)


if __name__ == "__main__":
    unittest.main()
