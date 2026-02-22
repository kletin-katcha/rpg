import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.dispatcher import executar_opcao_especial_cidade, executar_acao_contextual_cidade


class TestCidadeDispatcher(unittest.TestCase):
    def test_dispatcher_opcao_treino_retorna_selecao_quando_valido(self):
        jogador = Personagem("Tester")
        jogador.nivel = 5
        jogador.ouro = 999
        jogador.classe = "guerreiro"

        resultado = executar_opcao_especial_cidade(jogador, "Treinar Classe Secundária (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "selecao")
        self.assertGreater(len(resultado.get("opcoes", [])), 0)

    def test_dispatcher_acao_inexistente_retorna_none(self):
        jogador = Personagem("Tester")
        resultado = executar_acao_contextual_cidade(jogador, "acao_inexistente")
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
