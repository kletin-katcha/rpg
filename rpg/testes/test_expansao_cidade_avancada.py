import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.dispatcher import executar_opcao_especial_cidade


class TestExpansaoCidadeAvancada(unittest.TestCase):
    def test_construir_novas_estruturas(self):
        jogador = Personagem("Construtor")
        jogador.ouro = 1000
        jogador.adicionar_item("caco_de_arma_enferrujada", 30)
        jogador.adicionar_item("barra_metal_reciclado", 15)
        jogador.adicionar_item("gosma_de_slime", 15)
        jogador.adicionar_item("ferrao_de_vespa", 10)

        executar_opcao_especial_cidade(jogador, "Construir Oficina (Protótipo)")
        executar_opcao_especial_cidade(jogador, "Construir Laboratório Alquímico (Protótipo)")
        executar_opcao_especial_cidade(jogador, "Ativar Automação de Refino (Protótipo)")

        self.assertIn("laboratorio_alquimico", jogador.estruturas_construidas)
        self.assertIn("automacao_refino", jogador.estruturas_construidas)


if __name__ == "__main__":
    unittest.main()
