import unittest
from pathlib import Path

from rpg.game import Game
from rpg.systems.persistence import save_game, load_game


class TestPhase6Persistence(unittest.TestCase):
    def test_save_e_load_preservam_estado(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.executar_acao_cidade("coletar_item_inicial")
        game.executar_acao_cidade("desbloquear_postura_ofensiva")
        game.executar_acao_cidade("contrato_aleatorio")
        game.executar_acao_cidade("avancar_dia")

        path = "test_savegame.json"
        save_game(game, path)
        loaded = load_game(path)

        self.assertEqual(loaded.state.jogador.nome, "Arin")
        self.assertEqual(loaded.state.inventario.get("pocao_cura"), 1)
        self.assertIn("postura_ofensiva", loaded.state.jogador.habilidades_desbloqueadas)
        self.assertIsNotNone(loaded.state.contrato_ativo)
        self.assertGreaterEqual(loaded.state.dia_economico, 1)
        self.assertTrue(isinstance(loaded.state.codex, set))

        Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
