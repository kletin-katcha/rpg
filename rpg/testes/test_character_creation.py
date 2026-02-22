import unittest

from rpg.game import Game

    def test_sub_raca_api_aplica_modificador(self):
        """Valida leitura e aplicação de sub-raças (variações)."""
        jogador = cc_api.criar_personagem_base("Eirik")
        cc_api.aplicar_raca(jogador, "humano")

        sub_racas = cc_api.get_dados_sub_racas("humano")
        self.assertIn("nordico", sub_racas)

        constituicao_antes = jogador.base_constituicao
        cc_api.aplicar_sub_raca(jogador, "nordico")

        self.assertEqual(jogador.sub_raca, "nordico")
        self.assertEqual(jogador.base_constituicao, constituicao_antes + 1)

    def test_sub_raca_padrao_para_raca_sem_variacao_explicita(self):
        jogador = cc_api.criar_personagem_base("Krag")
        cc_api.aplicar_raca(jogador, "goliath")

        sub_racas = cc_api.get_dados_sub_racas("goliath")
        self.assertIn("goliath_tradicional", sub_racas)

        constituicao_antes = jogador.base_constituicao
        cc_api.aplicar_sub_raca(jogador, "goliath_tradicional")

        self.assertEqual(jogador.sub_raca, "goliath_tradicional")
        self.assertEqual(jogador.base_constituicao, constituicao_antes + 1)

    def test_sub_raca_sem_raca_lanca_erro(self):
        jogador = cc_api.criar_personagem_base("SemRaca")
        with self.assertRaises(ValueError):
            cc_api.aplicar_sub_raca(jogador, "nordico")

    def test_classe_secundaria_api(self):
        jogador = cc_api.criar_personagem_base("Kael")
        cc_api.aplicar_raca(jogador, "humano")
        cc_api.aplicar_classe(jogador, "guerreiro")

        total_habilidades_antes = len(jogador.habilidades)
        cc_api.aplicar_classe_secundaria(jogador, "ladino")

        self.assertEqual(jogador.classe_secundaria, "ladino")
        self.assertGreaterEqual(len(jogador.habilidades), total_habilidades_antes)

    def test_classe_secundaria_igual_principal_lanca_erro(self):
        jogador = cc_api.criar_personagem_base("Rurik")
        cc_api.aplicar_raca(jogador, "anao")
        cc_api.aplicar_classe(jogador, "guerreiro")

        with self.assertRaises(ValueError):
            cc_api.aplicar_classe_secundaria(jogador, "guerreiro")

    def test_classes_secundarias_disponiveis_filtra_classe_principal(self):
        disponiveis = cc_api.get_classes_secundarias_disponiveis("guerreiro")
        self.assertNotIn("guerreiro", disponiveis)
        self.assertIn("ladino", disponiveis)


class TestLegacyCharacterCreation(unittest.TestCase):
    def test_criacao_legada(self):
        g = Game()
        p = g.criar_jogador("Arin", "humano", "guerreiro")
        self.assertEqual(p.nome, "Arin")


if __name__ == "__main__":
    unittest.main()
