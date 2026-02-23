import unittest

from rpg.game import Game
from rpg.systems.world_director import (
    iniciar_memoria_faccoes,
    gerar_arco_mundo,
    escolher_mutador,
    aplicar_mutador_mercado,
    registrar_memoria,
)


class TestPhase15WorldDirector(unittest.TestCase):
    def test_gerar_arco_mundo(self):
        arco = gerar_arco_mundo({"guilda_ferreiros": 10, "circulo_arcano": 6}, "chuvoso", 14)
        self.assertIn("titulo", arco)
        self.assertIn("descricao", arco)

    def test_mutador_aplica_em_mercado(self):
        mercado = {"sucata_metal": 1.0, "espada_curta": 1.0}
        aplicar_mutador_mercado(mercado, "escassez_metal")
        self.assertGreater(mercado["sucata_metal"], 1.0)

    def test_memoria_faccoes(self):
        memoria = iniciar_memoria_faccoes({"guilda_ferreiros": 1})
        registrar_memoria(memoria, "guilda_ferreiros", "sucesso:caca_lobo")
        self.assertIn("sucesso:caca_lobo", memoria["guilda_ferreiros"])

    def test_integracao_game_diretor(self):
        g = Game()
        g.criar_jogador("Arin", "humano", "guerreiro")
        msg1 = g.executar_acao_cidade("gerar_arco_mundo")
        msg2 = g.executar_acao_cidade("aplicar_mutador")
        msg3 = g.executar_acao_cidade("ver_memoria_faccoes")
        self.assertIn("Arco gerado", msg1)
        self.assertIn("Mutador aplicado", msg2)
        self.assertIn("Memória de facções", msg3)


if __name__ == "__main__":
    unittest.main()
