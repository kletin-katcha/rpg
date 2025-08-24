import unittest
from unittest.mock import patch
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem

class TestInventorySystem(unittest.TestCase):
    """
    Testes focados nos sistemas de inventário e itens.
    """

    def setUp(self):
        """Prepara um jogador padrão para os testes."""
        self.jogador = Personagem(nome="Testador de Itens", nivel=1)

    def test_adicionar_e_remover_item(self):
        """Testa se os itens são adicionados e removidos corretamente."""
        # Adiciona um item que não se empilha
        self.jogador.adicionar_item("espada_curta_ferro")
        self.assertIn("espada_curta_ferro", self.jogador.inventario)
        self.assertEqual(self.jogador.inventario["espada_curta_ferro"]["quantidade"], 1)

        # Adiciona um item que se empilha
        self.jogador.adicionar_item("pocao_cura_fraca", 3)
        self.assertIn("pocao_cura_fraca", self.jogador.inventario)
        self.assertEqual(self.jogador.inventario["pocao_cura_fraca"]["quantidade"], 3)

        # Adiciona mais do mesmo item para testar o empilhamento
        self.jogador.adicionar_item("pocao_cura_fraca", 2)
        self.assertEqual(self.jogador.inventario["pocao_cura_fraca"]["quantidade"], 5)

        # Remove alguns itens
        self.jogador.remover_item("pocao_cura_fraca", 4)
        self.assertEqual(self.jogador.inventario["pocao_cura_fraca"]["quantidade"], 1)

        # Remove o último item
        self.jogador.remover_item("pocao_cura_fraca", 1)
        self.assertNotIn("pocao_cura_fraca", self.jogador.inventario)

    def test_usar_pocao_de_cura(self):
        """
        Testa se usar uma poção de cura aumenta o HP do jogador e consome o item.
        """
        # Define o HP do jogador para um valor baixo
        self.jogador.hp_atual = 10
        hp_inicial = self.jogador.hp_atual

        # Adiciona uma poção ao inventário
        id_pocao = "pocao_cura_fraca"
        self.jogador.adicionar_item(id_pocao, 1)
        self.assertIn(id_pocao, self.jogador.inventario)

        # Usa a poção
        # Mocka o print para não poluir o output do teste
        with patch('builtins.print'):
            self.jogador.usar_item(id_pocao)

        # Verifica se o HP aumentou
        self.assertGreater(self.jogador.hp_atual, hp_inicial, "O HP deveria ter aumentado após usar a poção.")
        # Poção cura 50, então HP deve ser 10 + 50 = 60
        self.assertEqual(self.jogador.hp_atual, 60)

        # Verifica se a poção foi removida do inventário
        self.assertNotIn(id_pocao, self.jogador.inventario, "A poção deveria ter sido removida do inventário.")


if __name__ == '__main__':
    unittest.main()
