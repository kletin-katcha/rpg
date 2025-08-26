import unittest
from unittest.mock import patch
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg_legacy.io import console_ui
from rpg_legacy.entidades.personagem import Personagem

class TestCharacterCreationFlow(unittest.TestCase):
    """
    Testa o fluxo completo de criação de personagem, da UI ao objeto final.
    """

    @patch('builtins.input')
    def test_full_creation_flow(self, mock_input):
        """
        Simula a entrada do usuário para criar um Humano Guerreiro e verifica o resultado.
        """
        # Simula uma sequência de entradas do usuário
        mock_input.side_effect = [
            "Jules, o Valente",  # Nome do personagem
            "",                  # Pressiona Enter
            "1",                 # Escolhe a primeira raça (Humano)
            "s",                 # Confirma a escolha
            "",                  # Pressiona Enter
            "1",                 # Escolhe a primeira classe (Guerreiro)
            "s",                 # Confirma a escolha
            "",                  # Pressiona Enter
            "forca+", "forca+", "forca+", "forca+", "forca+", # +5 Força
            "constituicao+", "constituicao+", "constituicao+", "constituicao+", "constituicao+", # +5 Constituição
            "destreza+", "destreza+", "destreza+", "destreza+", "destreza+", # +5 Destreza
            "inteligencia+", "inteligencia+", "inteligencia+", "inteligencia+", "inteligencia+", # +5 Inteligência
            "pronto",            # Finaliza a distribuição de pontos
            "",                  # Pressiona Enter após a distribuição
            ""                   # Pressiona Enter no final para concluir
        ]

        # Roda a função principal da UI de criação
        personagem_criado = console_ui.iniciar_criacao_personagem_console()

        # --- VERIFICAÇÕES ---
        self.assertIsInstance(personagem_criado, Personagem)

        # Verifica dados básicos
        self.assertEqual(personagem_criado.nome, "Jules, o Valente")
        self.assertEqual(personagem_criado.raca, "humano")
        self.assertEqual(personagem_criado.classe, "guerreiro")

        # Verifica atributos (Base 5 + Racial + Distribuídos)
        # Humano: +2 FOR, +1 DES, +1 CON, +1 INT, +1 SAB, +1 CAR, +0 SOR
        # Pontos: +5 FOR, +5 DES, +5 CON, +5 INT
        self.assertEqual(personagem_criado.base_forca, 5 + 2 + 5) # 12
        self.assertEqual(personagem_criado.base_destreza, 5 + 1 + 5) # 11
        self.assertEqual(personagem_criado.base_constituicao, 5 + 1 + 5) # 11
        self.assertEqual(personagem_criado.base_inteligencia, 5 + 1 + 5) # 11
        self.assertEqual(personagem_criado.base_sabedoria, 5 + 1) # 6
        self.assertEqual(personagem_criado.base_carisma, 5 + 1) # 6
        self.assertEqual(personagem_criado.base_sorte, 5) # 5

        # Verifica se os pontos foram gastos
        self.assertEqual(personagem_criado.pontos_de_atributo_para_distribuir, 0)

        # Verifica habilidades
        self.assertIn("esforco_heroico", personagem_criado.habilidades) # Racial Humano
        self.assertIn("ataque_poderoso", personagem_criado.habilidades) # Classe Guerreiro
        self.assertIn("grito_de_guerra", personagem_criado.habilidades) # Classe Guerreiro

        # Verifica equipamento
        self.assertIsNotNone(personagem_criado.equipamentos["arma_principal"])
        self.assertEqual(personagem_criado.equipamentos["arma_principal"].id_item, "espada_curta_ferro")
        self.assertIsNotNone(personagem_criado.equipamentos["peitoral"])
        self.assertEqual(personagem_criado.equipamentos["peitoral"].id_item, "peitoral_de_couro_batido")

if __name__ == '__main__':
    unittest.main()
