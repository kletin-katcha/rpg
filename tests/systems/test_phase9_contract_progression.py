import unittest

from rpg.game import Game
from rpg.systems.meta_world import concluir_contrato, gerar_contrato_aleatorio


class TestPhase9ContractProgression(unittest.TestCase):
    def test_concluir_contrato_aplica_recompensas(self):
        game = Game()
        jogador = game.criar_jogador("Arin", "humano", "guerreiro")
        contrato = gerar_contrato_aleatorio()

        reputacao_antes = game.state.reputacoes.get(contrato["faccao_id"], 0)
        ouro_antes = game.state.cidade.ouro

        out = concluir_contrato(jogador, game.state.reputacoes, ouro_antes, contrato)
        self.assertGreaterEqual(out["ouro"], ouro_antes + contrato["ouro"])
        self.assertEqual(out["reputacao"], reputacao_antes + contrato["reputacao_ganho"])
        self.assertGreaterEqual(jogador.xp, 0)

    def test_integracao_game_contrato_ativo(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        game.executar_acao_cidade("contrato_aleatorio")
        msg = game.executar_acao_cidade("concluir_contrato")
        self.assertIn("Contrato concluído", msg)


if __name__ == "__main__":
    unittest.main()
