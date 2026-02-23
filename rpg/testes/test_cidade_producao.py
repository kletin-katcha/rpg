import unittest

from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.producao import preparar_configuracao_producao, definir_plano_producao
from rpg.sistemas.automacao import processar_ciclo_automatizado


class TestCidadeProducao(unittest.TestCase):
    def test_preparar_configuracao_sem_automacao(self):
        jogador = Personagem("Produtor")
        resultado = preparar_configuracao_producao(jogador)
        self.assertEqual(resultado.get("tipo"), "feedback")

    def test_definir_plano_e_processar_ciclo(self):
        jogador = Personagem("Produtor")
        jogador.estruturas_construidas.add("automacao_coleta")
        jogador.niveis_estruturas["automacao_coleta"] = 2

        conf = preparar_configuracao_producao(jogador)
        self.assertEqual(conf.get("tipo"), "selecao")

        definir_plano_producao(jogador, "sucata")
        logs = processar_ciclo_automatizado(jogador)

        self.assertIn("sucata", logs[0])
        self.assertIn("caco_de_arma_enferrujada", jogador.inventario)
        self.assertEqual(jogador.inventario["caco_de_arma_enferrujada"]["quantidade"], 4)


if __name__ == "__main__":
    unittest.main()
