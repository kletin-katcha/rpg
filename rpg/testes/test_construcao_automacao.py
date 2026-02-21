import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.construcao import construir_estrutura
from rpg.sistemas.automacao import processar_ciclo_automatizado
from rpg.sistemas.cidade.dispatcher import executar_opcao_especial_cidade


class TestConstrucaoAutomacao(unittest.TestCase):
    def test_construir_oficina_consumindo_recursos(self):
        jogador = Personagem("Builder")
        jogador.ouro = 200
        jogador.adicionar_item("caco_de_arma_enferrujada", 10)

        resultado = construir_estrutura(jogador, "oficina_basica")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIn("oficina_basica", jogador.estruturas_construidas)
        self.assertEqual(jogador.ouro, 120)

    def test_construir_automacao_via_dispatcher(self):
        jogador = Personagem("Builder")
        jogador.ouro = 500
        jogador.adicionar_item("caco_de_arma_enferrujada", 10)
        jogador.adicionar_item("barra_metal_reciclado", 5)

        executar_opcao_especial_cidade(jogador, "Construir Oficina (Protótipo)")
        resultado = executar_opcao_especial_cidade(jogador, "Ativar Automação de Coleta (Protótipo)")

        self.assertEqual(resultado.get("tipo"), "feedback")
        self.assertIn("automacao_coleta", jogador.estruturas_construidas)

    def test_ciclo_automatizado_gera_itens(self):
        jogador = Personagem("Builder")
        jogador.estruturas_construidas.add("automacao_coleta")

        logs = processar_ciclo_automatizado(jogador)

        self.assertIn("autômatos", logs[0])
        self.assertIn("caco_de_arma_enferrujada", jogador.inventario)
        self.assertIn("gosma_de_slime", jogador.inventario)


if __name__ == "__main__":
    unittest.main()
