import unittest

from rpg.game import Game
from rpg.systems.meta_world import gerar_contrato_aleatorio, falhar_contrato, resgatar_beneficio_faccao


class TestPhase11ContractTiersAndReputation(unittest.TestCase):
    def test_contrato_tem_tier(self):
        contrato = gerar_contrato_aleatorio("ouro")
        self.assertIn(contrato["tier"], {"bronze", "prata", "ouro", "lendario"})

    def test_falha_contrato_reduz_reputacao(self):
        game = Game()
        game.criar_jogador("Arin", "humano", "guerreiro")
        contrato = gerar_contrato_aleatorio("ouro")
        rep_antes = game.state.reputacoes[contrato["faccao_id"]]
        out = falhar_contrato(game.state.reputacoes, contrato)
        self.assertEqual(out["reputacao"], rep_antes - contrato["reputacao_perda"])

    def test_perk_tier2_por_reputacao(self):
        reputacoes = {"guilda_ferreiros": 21}
        inventario = {}
        out = resgatar_beneficio_faccao(reputacoes, inventario, 100, "guilda_ferreiros")
        self.assertIn("tier 2", out["detalhe"])
        self.assertEqual(inventario.get("sucata_metal"), 4)

    def test_integracao_game_falhar_contrato(self):
        game = Game()
        game.criar_jogador("Lia", "elfo", "mago")
        game.executar_acao_cidade("contrato_aleatorio")
        msg = game.executar_acao_cidade("falhar_contrato")
        self.assertIn("Contrato falhou", msg)


if __name__ == "__main__":
    unittest.main()
