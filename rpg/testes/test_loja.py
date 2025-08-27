import unittest
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem
from rpg.sistemas import loja as sistema_loja
from rpg.dados.lojas import LOJAS

class TestLojaSistema(unittest.TestCase):
    """Testa o sistema de lógica de lojas (compra e venda)."""

    def setUp(self):
        """Configura um jogador e os dados da loja para cada teste."""
        self.jogador = Personagem(nome="Comprador")
        self.loja_data = LOJAS["ferreiro_vila"]

    def test_compra_sucesso(self):
        """Testa se um jogador pode comprar um item com ouro suficiente."""
        self.jogador.ouro = 500
        id_item = "espada_curta_ferro"
        preco_item = sistema_loja.get_preco_compra(id_item, self.loja_data)

        mensagem = sistema_loja.comprar_item(self.jogador, self.loja_data, id_item, 1)

        self.assertIn("Você comprou", mensagem)
        self.assertEqual(self.jogador.ouro, 500 - preco_item)
        self.assertIn(id_item, self.jogador.inventario)
        self.assertEqual(self.jogador.inventario[id_item]["quantidade"], 1)

    def test_compra_sem_ouro(self):
        """Testa se um jogador não pode comprar um item sem ouro suficiente."""
        self.jogador.ouro = 10
        id_item = "espada_curta_ferro"

        mensagem = sistema_loja.comprar_item(self.jogador, self.loja_data, id_item, 1)

        self.assertIn("Você não tem ouro suficiente", mensagem)
        self.assertEqual(self.jogador.ouro, 10)
        self.assertNotIn(id_item, self.jogador.inventario)

    def test_venda_sucesso(self):
        """Testa se um jogador pode vender um item que possui."""
        id_item = "adaga_de_ferro"
        self.jogador.adicionar_item(id_item, 1)
        self.jogador.ouro = 0
        preco_venda = sistema_loja.get_preco_venda(id_item, self.loja_data)

        mensagem = sistema_loja.vender_item(self.jogador, self.loja_data, id_item, 1)

        self.assertIn("Você vendeu", mensagem)
        self.assertEqual(self.jogador.ouro, preco_venda)
        self.assertNotIn(id_item, self.jogador.inventario)

    def test_venda_sem_item(self):
        """Testa se um jogador não pode vender um item que não possui."""
        id_item = "espada_longa"
        self.jogador.ouro = 0

        mensagem = sistema_loja.vender_item(self.jogador, self.loja_data, id_item, 1)

        self.assertIn("Você não possui este item para vender", mensagem)
        self.assertEqual(self.jogador.ouro, 0)

if __name__ == '__main__':
    unittest.main()
