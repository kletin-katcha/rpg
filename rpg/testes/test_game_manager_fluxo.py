import unittest
from unittest.mock import patch

from rpg.game_manager import GameManager
from rpg.entidades.personagem import Personagem


class TestGameManagerFluxoCidade(unittest.TestCase):
    def setUp(self):
        self.gm = GameManager()
        self.gm.jogador = Personagem("Aventureiro")
        self.gm.game_state = "in_game"

    @patch("rpg.game_manager.random.choice", return_value="goblin_batedor")
    @patch("rpg.game_manager.random.random", return_value=0.0)
    def test_explorar_floresta_transiciona_para_combate(self, _mock_random, _mock_choice):
        resultado = self.gm.executar_opcao_cidade("Explorar a Floresta dos Sussurros")

        self.assertEqual(resultado.get("tipo"), "transicao_estado")
        self.assertEqual(resultado.get("novo_estado"), "combat")
        self.assertEqual(self.gm.game_state, "combat")
        self.assertIsNotNone(self.gm.combat_state)
        self.assertGreater(len(self.gm.combat_state["inimigos"]), 0)


if __name__ == "__main__":
    unittest.main()


class TestGameManagerCriacaoComSubRaca(unittest.TestCase):
    def test_fluxo_criacao_inclui_sub_raca_quando_existir(self):
        gm = GameManager()
        gm.novo_jogo()

        gm.processar_acao_criacao({"nome": "Heron"})
        self.assertEqual(gm.creation_step, "raca")

        gm.processar_acao_criacao({"id_raca": "humano"})
        self.assertEqual(gm.creation_step, "sub_raca")

        dados = gm.get_dados_criacao_personagem()
        self.assertEqual(dados.get("step"), "sub_raca")
        self.assertIn("nordico", dados.get("opcoes", {}))

        gm.processar_acao_criacao({"id_sub_raca": "nordico"})
        self.assertEqual(gm.creation_step, "classe")
        self.assertEqual(gm.jogador.sub_raca, "nordico")


class TestGameManagerClasseSecundaria(unittest.TestCase):
    def test_treinar_classe_secundaria_sucesso(self):
        gm = GameManager()
        gm.jogador = Personagem("Veterano")
        gm.jogador.nivel = 3
        gm.jogador.ouro = 200
        gm.jogador.classe = "guerreiro"
        gm.game_state = "in_game"

        resultado = gm.executar_opcao_cidade("Treinar Classe Secundária (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "selecao")
        self.assertGreater(len(resultado.get("opcoes", [])), 0)

        classe_escolhida = resultado["opcoes"][0]
        resultado_treino = gm.executar_acao_contextual(f"treinar_classe_secundaria:{classe_escolhida}")

        self.assertEqual(resultado_treino.get("tipo"), "feedback")
        self.assertEqual(gm.jogador.classe_secundaria, classe_escolhida)
        self.assertNotEqual(gm.jogador.classe_secundaria, "guerreiro")
        self.assertEqual(gm.jogador.ouro, 150)

    def test_treinar_classe_secundaria_falha_por_nivel(self):
        gm = GameManager()
        gm.jogador = Personagem("Iniciante")
        gm.jogador.nivel = 2
        gm.jogador.ouro = 200
        gm.jogador.classe = "guerreiro"
        gm.game_state = "in_game"

        resultado = gm.executar_opcao_cidade("Treinar Classe Secundária (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIsNone(gm.jogador.classe_secundaria)

    def test_treinar_classe_secundaria_falha_sem_classe_principal(self):
        gm = GameManager()
        gm.jogador = Personagem("SemClasse")
        gm.jogador.nivel = 10
        gm.jogador.ouro = 999
        gm.game_state = "in_game"

        resultado = gm.executar_opcao_cidade("Treinar Classe Secundária (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIsNone(gm.jogador.classe_secundaria)

    def test_treinar_classe_secundaria_falha_por_ouro(self):
        gm = GameManager()
        gm.jogador = Personagem("SemOuro")
        gm.jogador.nivel = 10
        gm.jogador.ouro = 10
        gm.jogador.classe = "guerreiro"
        gm.game_state = "in_game"

        resultado = gm.executar_opcao_cidade("Treinar Classe Secundária (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIsNone(gm.jogador.classe_secundaria)


    def test_treinar_classe_secundaria_acao_contextual_invalida(self):
        gm = GameManager()
        gm.jogador = Personagem("SemTreino")
        gm.jogador.nivel = 10
        gm.jogador.ouro = 500
        gm.jogador.classe = "guerreiro"
        gm.game_state = "in_game"

        resultado = gm.executar_acao_contextual("treinar_classe_secundaria:guerreiro")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIn("Falha no treinamento", resultado.get("log", [""])[0])
