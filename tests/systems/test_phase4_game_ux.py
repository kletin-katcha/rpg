import unittest
from unittest.mock import patch

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

    def test_explorar_fora_da_cidade_usa_area_atual(self):
        game = Game()
        game.criar_jogador("Mila", "humano", "guerreiro")
        with patch("rpg.game.random.choice", return_value="lobo_cinzento"):
            out = game.executar_acao_cidade("explorar_fora_cidade")
        self.assertIn("Exploração em vila_aurora", out)
        self.assertIn("lobo_cinzento", out)

    def test_viagem_dispara_evento(self):
        game = Game()
        game.criar_jogador("Theo", "humano", "guerreiro")
        with patch("rpg.game.random.random", side_effect=[0.1, 0.4]), patch("rpg.game.random.choice", return_value="goblin_batedor"):
            out = game.executar_acao_cidade("viajar_fronteira_norte")
        self.assertIn("Viagem concluída", out)
        self.assertIn("Evento de viagem", out)


if __name__ == "__main__":
    unittest.main()
