import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.treino import preparar_treino_classe_secundaria, executar_treino_classe_secundaria


class TestCidadeTreino(unittest.TestCase):
    def test_preparar_treino_valido(self):
        jogador = Personagem("Aluno")
        jogador.nivel = 4
        jogador.ouro = 100
        jogador.classe = "guerreiro"

        resultado = preparar_treino_classe_secundaria(jogador)
        self.assertEqual(resultado.get("tipo"), "selecao")

    def test_executar_treino_valido(self):
        jogador = Personagem("Aluno")
        jogador.nivel = 4
        jogador.ouro = 100
        jogador.classe = "guerreiro"

        resultado = executar_treino_classe_secundaria(jogador, "ladino")
        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertEqual(jogador.classe_secundaria, "ladino")
        self.assertEqual(jogador.ouro, 50)


if __name__ == "__main__":
    unittest.main()
