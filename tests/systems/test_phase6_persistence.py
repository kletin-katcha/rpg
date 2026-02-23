import unittest
from pathlib import Path

from rpg.game import Game
from rpg.systems.persistence import SAVE_VERSION, load_game, save_game


class TestPhase6Persistence(unittest.TestCase):
    def test_save_e_load_preservam_estado(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        game.executar_acao_cidade("coletar_item_inicial")
        game.executar_acao_cidade("desbloquear_postura_ofensiva")
        game.executar_acao_cidade("contrato_aleatorio")
        game.executar_acao_cidade("avancar_dia")
        game.executar_acao_cidade("iniciar_cadeia_contratos")
        game.executar_acao_cidade("gerar_tensao_faccoes")
        game.executar_acao_cidade("gerar_crise_urbana")
        game.executar_acao_cidade("viajar_fronteira_norte")
        game.executar_acao_cidade("gerar_dungeon")
        game.executar_acao_cidade("rodar_agenda_faccoes")
        game.executar_acao_cidade("iniciar_arco_longo")
        game.executar_acao_cidade("cacar_lobo")

        path = "test_savegame.json"
        save_game(game, path)
        loaded = load_game(path)

        self.assertEqual(loaded.state.jogador.nome, "Arin")
        self.assertGreaterEqual(loaded.state.inventario.get("pocao_cura", 0), 1)
        self.assertIn("postura_ofensiva", loaded.state.jogador.habilidades_desbloqueadas)
        self.assertIsNotNone(loaded.state.contrato_ativo)
        self.assertGreaterEqual(loaded.state.dia_economico, 1)
        self.assertTrue(isinstance(loaded.state.codex, set))
        self.assertTrue(isinstance(loaded.state.memoria_faccoes, dict))
        self.assertTrue(isinstance(loaded.state.regioes_descobertas, set))
        self.assertEqual(loaded.state.regiao_atual, "fronteira_norte")
        self.assertIsNotNone(loaded.state.dungeon_ativa)
        self.assertGreaterEqual(len(loaded.state.agenda_faccoes), 1)
        self.assertIsNotNone(loaded.state.arco_longo)
        self.assertTrue(isinstance(loaded.state.cadeia_contratos, list))
        self.assertTrue(isinstance(loaded.state.tensao_faccoes, dict))
        self.assertTrue(isinstance(loaded.state.crise_urbana, dict))
        self.assertEqual(loaded.state.metricas_onboarding["comandos_invalidos"], 0)
        self.assertTrue(isinstance(loaded.state.ultimo_log_combate, list))
        self.assertTrue(isinstance(loaded.state.checkpoint_criacao, dict))

        Path(path).unlink(missing_ok=True)
        Path(f"{path}.bak").unlink(missing_ok=True)

    def test_save_version_e_backup_de_recuperacao(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        path = "test_save_recovery.json"

        save_game(game, path)
        save_game(game, path)
        backup = Path(f"{path}.bak")
        self.assertTrue(backup.exists())

        Path(path).write_text("{invalido", encoding="utf-8")
        loaded = load_game(path)
        self.assertEqual(loaded.state.jogador.nome, "Lia")

        raw = backup.read_text(encoding="utf-8")
        self.assertIn(f'"save_version": {SAVE_VERSION}', raw)

        Path(path).unlink(missing_ok=True)
        backup.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
