import unittest

from rpg.game import Game
from rpg.systems.expansion import viajar_para_regiao, gerar_dungeon, gerar_pacote_expansao, simular_balance_headless


class TestPhase21To25ExpansionSuite(unittest.TestCase):
    def test_phase21_viagem(self):
        out = viajar_para_regiao("vila_aurora", "fronteira_norte", 6)
        self.assertTrue(out["ok"])
        self.assertEqual(out["regiao"], "fronteira_norte")

    def test_phase22_dungeon(self):
        d = gerar_dungeon(3, "fronteira_norte")
        self.assertIn("salas", d)
        self.assertGreaterEqual(d["salas"], 3)
        self.assertIn("recompensa_base", d)

    def test_phase23_agenda_game(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        msg = g.executar_acao_cidade("rodar_agenda_faccoes")
        self.assertIn("Agenda de facções executada", msg)
        self.assertIn("tensão=", msg)
        self.assertTrue(isinstance(g.state.tensao_faccoes, dict))

    def test_phase24_arco_longo(self):
        g = Game()
        g.criar_jogador("Lia", "elfo", "mago")
        g.executar_acao_cidade("iniciar_arco_longo")
        ouro_antes = g.state.cidade.ouro
        msg = g.executar_acao_cidade("avancar_arco_longo")
        self.assertIn("Arco longo atualizado", msg)
        g.executar_acao_cidade("avancar_arco_longo")
        self.assertGreaterEqual(g.state.cidade.ouro, ouro_antes)

    def test_phase25_tools(self):
        pacote = gerar_pacote_expansao("x", 3)
        sim = simular_balance_headless(10)
        self.assertEqual(len(pacote["itens"]), 3)
        self.assertEqual(sim["rodadas"], 10)
        self.assertIn("hp_final_medio", sim)

    def test_explorar_dungeon_concede_xp_no_game(self):
        g = Game()
        g.criar_jogador("Noah", "humano", "guerreiro")
        xp_antes = g.state.jogador.xp
        g.executar_acao_cidade("gerar_dungeon")
        g.executar_acao_cidade("explorar_dungeon")
        self.assertGreater(g.state.jogador.xp, xp_antes)


if __name__ == "__main__":
    unittest.main()
