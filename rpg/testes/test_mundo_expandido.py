"""Testes para expansão de mundo (cidades/reinos) e forja avançada."""

import unittest

from rpg.dados.cidades_reinos import CIDADES_REINOS, REINOS
from rpg.entidades.personagem import Personagem
from rpg.sistemas.cidade.viagem import preparar_viagem_cidade, viajar_para_cidade
from rpg.sistemas.metalurgia import forjar_receita_avancada


class TestMundoExpandido(unittest.TestCase):
    def test_catalogo_cidades_reinos(self):
        self.assertGreaterEqual(len(CIDADES_REINOS), 5)
        self.assertGreaterEqual(len(REINOS), 5)

    def test_preparar_e_viajar(self):
        jogador = Personagem("Viajante")
        selecao = preparar_viagem_cidade(jogador)
        self.assertEqual(selecao["tipo"], "selecao")

        res = viajar_para_cidade(jogador, "forte_ferreo")
        self.assertEqual(res["tipo"], "feedback")
        self.assertEqual(jogador.cidade_atual, "forte_ferreo")

    def test_forja_avancada_requer_nivel(self):
        jogador = Personagem("Ferreiro")
        jogador.niveis_estruturas["oficina_basica"] = 1
        jogador.adicionar_item("barra_metal_reciclado", 10)
        logs = forjar_receita_avancada(jogador, "espada_longa_reciclada")
        self.assertIn("Oficina insuficiente", logs[0])


if __name__ == "__main__":
    unittest.main()
