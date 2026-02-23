import unittest

from rpg.game import Game


class TestPhase18ContractChains(unittest.TestCase):
    def test_iniciar_e_consultar_cadeia(self):
        jogo = Game()
        jogo.criar_jogador("Arin", "humano", "guerreiro")

        msg = jogo.executar_acao_cidade("iniciar_cadeia_contratos")
        self.assertIn("Cadeia iniciada", msg)
        self.assertEqual(len(jogo.state.cadeia_contratos), 3)

        progresso = jogo.executar_acao_cidade("ver_cadeia_contratos")
        self.assertIn("Etapa 1/3", progresso)

    def test_concluir_avanca_para_proxima_etapa(self):
        jogo = Game()
        jogo.criar_jogador("Lia", "elfo", "mago")
        jogo.executar_acao_cidade("iniciar_cadeia_contratos")

        jogo.executar_acao_cidade("concluir_contrato")

        self.assertEqual(jogo.state.cadeia_resolvidos, 1)
        self.assertIsNotNone(jogo.state.contrato_ativo)

    def test_falha_reseta_cadeia(self):
        jogo = Game()
        jogo.criar_jogador("Noah", "humano", "guerreiro")
        jogo.executar_acao_cidade("iniciar_cadeia_contratos")

        jogo.executar_acao_cidade("falhar_contrato")

        self.assertEqual(jogo.state.cadeia_contratos, [])
        self.assertEqual(jogo.state.cadeia_resolvidos, 0)


if __name__ == "__main__":
    unittest.main()
