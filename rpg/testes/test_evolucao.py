import unittest
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem
from rpg.sistemas import evolucao as sistema_evolucao
from rpg.io import criacao_personagem as cc_api

class TestEvolucaoSistema(unittest.TestCase):
    """Testa o sistema de lógica de evolução de classes."""

    def setUp(self):
        """Configura um jogador para cada teste."""
        self.guerreiro = Personagem(nome="Guerreiro de Teste")
        cc_api.aplicar_classe(self.guerreiro, "guerreiro")

    def test_evolucao_disponivel_nivel_certo(self):
        """Testa se as evoluções são listadas corretamente para um personagem de nível alto."""
        self.guerreiro.nivel = 15
        evolucoes = sistema_evolucao.get_evolucoes_disponiveis(self.guerreiro)
        self.assertIn("mestre_de_armas", evolucoes)
        self.assertIn("berserker", evolucoes)
        self.assertEqual(len(evolucoes), 2)

    def test_evolucao_indisponivel_nivel_baixo(self):
        """Testa se nenhuma evolução é listada para um personagem de nível baixo."""
        self.guerreiro.nivel = 10
        evolucoes = sistema_evolucao.get_evolucoes_disponiveis(self.guerreiro)
        self.assertEqual(len(evolucoes), 0)

    def test_evolucao_sucesso(self):
        """Testa se a evolução de classe aplica corretamente os bônus e habilidades."""
        self.guerreiro.nivel = 20
        forca_antes = self.guerreiro.base_forca
        destreza_antes = self.guerreiro.base_destreza
        habilidades_antes = len(self.guerreiro.habilidades)

        logs = sistema_evolucao.evoluir_classe(self.guerreiro, "mestre_de_armas")

        self.assertIn("Você evoluiu para Mestre de Armas!", logs)
        self.assertEqual(self.guerreiro.classe, "mestre_de_armas")
        self.assertEqual(self.guerreiro.base_forca, forca_antes + 2)
        self.assertEqual(self.guerreiro.base_destreza, destreza_antes + 2)
        self.assertGreater(len(self.guerreiro.habilidades), habilidades_antes)
        self.assertIn("postura_de_mestre", self.guerreiro.habilidades)
        self.assertIn("golpe_mortal", self.guerreiro.habilidades)

    def test_evolucao_falha_requisitos(self):
        """Testa se um jogador não pode evoluir se não cumprir os requisitos."""
        self.guerreiro.nivel = 10 # Nível baixo
        logs = sistema_evolucao.evoluir_classe(self.guerreiro, "mestre_de_armas")
        self.assertIn("Você não cumpre os requisitos para esta evolução.", logs)
        self.assertEqual(self.guerreiro.classe, "guerreiro") # Classe não deve mudar

if __name__ == '__main__':
    unittest.main()
