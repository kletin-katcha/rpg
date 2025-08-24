import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.io import criacao_personagem
from rpg.entidades.personagem import Personagem

class TestCharacterCreation(unittest.TestCase):
    """
    Testes focados exclusivamente no processo de criação de personagem.
    """

    def test_full_character_creation_flow(self):
        """
        Testa o fluxo completo de criação de personagem, verificando se o
        personagem final tem os atributos, raça e classe esperados.
        """
        # Sequência de inputs para criar um Anão Guerreiro chamado "Durin"
        creation_inputs = [
            "Durin",  # Nome
            '3', 's', # Raça: Anão
            '1', 's', # Classe: Guerreiro
            '1', '10', # 10 pontos em Força
            '3', '10', # 10 pontos em Constituição
        ]

        with patch('builtins.input', side_effect=creation_inputs), \
             patch('rpg.utilitarios.narrador.narrar', MagicMock()), \
             patch('rpg.utilitarios.funcoes_gerais.pausar', MagicMock()):

            # Inicia o processo de criação
            jogador = criacao_personagem.iniciar_criacao_personagem()

            # Asserções para verificar o resultado
            self.assertIsInstance(jogador, Personagem)
            self.assertEqual(jogador.nome, "Durin")
            self.assertEqual(jogador.raca, "anao")
            self.assertEqual(jogador.classe, "guerreiro")

            # Verifica os atributos base + bônus racial + pontos distribuídos
            # Base(5) + Anão(3) + Pontos(10) = 18
            self.assertEqual(jogador.forca, 18)
            # Base(5) + Anão(4) + Pontos(10) = 19
            self.assertEqual(jogador.constituicao, 19)
            # Verifica se as habilidades foram adicionadas
            self.assertIn("resistencia_a_veneno", jogador.habilidades) # Habilidade de Anão
            self.assertIn("ataque_poderoso", jogador.habilidades) # Habilidade de Guerreiro

if __name__ == '__main__':
    unittest.main()
