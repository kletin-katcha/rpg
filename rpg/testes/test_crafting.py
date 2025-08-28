import unittest
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem
from rpg.sistemas import crafting as sistema_crafting
from rpg.dados.receitas import RECEITAS

class TestCraftingSistema(unittest.TestCase):
    """Testa o sistema de lógica de crafting."""

    def setUp(self):
        """Configura um jogador para cada teste."""
        self.jogador = Personagem(nome="Artesão")
        self.receita_adaga = RECEITAS["adaga_de_ferro_r"]
        self.receita_pocao = RECEITAS["pocao_cura_media_r"]

    def test_criacao_sucesso(self):
        """Testa se um jogador pode criar um item se tiver os ingredientes."""
        # Adiciona ingredientes para a adaga
        self.jogador.adicionar_item("caco_de_arma_enferrujada", 2)
        self.jogador.adicionar_item("pele_de_lobo", 1)

        self.assertTrue(sistema_crafting.pode_criar(self.jogador, self.receita_adaga))

        mensagem = sistema_crafting.criar_item(self.jogador, self.receita_adaga)

        self.assertIn("Você criou Adaga de Ferro com sucesso!", mensagem)
        self.assertNotIn("caco_de_arma_enferrujada", self.jogador.inventario)
        self.assertNotIn("pele_de_lobo", self.jogador.inventario)
        self.assertIn("adaga_de_ferro", self.jogador.inventario)
        self.assertEqual(self.jogador.inventario["adaga_de_ferro"]["quantidade"], 1)

    def test_criacao_sem_ingredientes(self):
        """Testa se um jogador não pode criar um item sem os ingredientes."""
        self.assertFalse(sistema_crafting.pode_criar(self.jogador, self.receita_pocao))

        mensagem = sistema_crafting.criar_item(self.jogador, self.receita_pocao)

        self.assertIn("Você não tem os ingredientes necessários.", mensagem)
        self.assertNotIn("pocao_cura_media", self.jogador.inventario)

    def test_criacao_com_ingredientes_insuficientes(self):
        """Testa se um jogador não pode criar um item com quantidade insuficiente de ingredientes."""
        # Adiciona apenas 1 dos 2 ingredientes necessários
        self.jogador.adicionar_item("pocao_cura_fraca", 1)
        self.jogador.adicionar_item("ervas_estranhas", 1)

        self.assertFalse(sistema_crafting.pode_criar(self.jogador, self.receita_pocao))

        mensagem = sistema_crafting.criar_item(self.jogador, self.receita_pocao)
        self.assertIn("Você não tem os ingredientes necessários.", mensagem)


if __name__ == '__main__':
    unittest.main()
