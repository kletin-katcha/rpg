import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.construcao import construir_estrutura
from rpg.sistemas.cidade.melhorias import melhorar_estrutura


class TestCidadeMelhorias(unittest.TestCase):
    def test_melhorar_oficina_para_nivel_2(self):
        jogador = Personagem("Engenheiro")
        jogador.ouro = 500
        jogador.adicionar_item("caco_de_arma_enferrujada", 10)
        jogador.adicionar_item("barra_metal_reciclado", 10)

        construir_estrutura(jogador, "oficina_basica")
        resultado = melhorar_estrutura(jogador, "oficina_basica")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertEqual(jogador.niveis_estruturas.get("oficina_basica"), 2)


if __name__ == "__main__":
    unittest.main()
