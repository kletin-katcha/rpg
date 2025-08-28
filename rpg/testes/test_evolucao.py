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
        """Configura personagens para cada teste."""
        self.guerreiro = Personagem(nome="Guerreiro de Teste")
        cc_api.aplicar_classe(self.guerreiro, "guerreiro")

        self.ladino = Personagem(nome="Ladino de Teste")
        cc_api.aplicar_classe(self.ladino, "ladino")

        self.clerigo = Personagem(nome="Clerigo de Teste")
        cc_api.aplicar_classe(self.clerigo, "clerigo")

    def test_evolucao_disponivel_guerreiro(self):
        """Testa se as evoluções são listadas corretamente para um Guerreiro de nível alto."""
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

    def test_evolucao_sucesso_guerreiro_para_mestre(self):
        """Testa se a evolução de Guerreiro para Mestre de Armas funciona."""
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

    def test_evolucao_sucesso_ladino_para_assassino(self):
        """Testa se a evolução de Ladino para Assassino funciona."""
        self.ladino.nivel = 15
        destreza_antes = self.ladino.base_destreza
        inteligencia_antes = self.ladino.base_inteligencia

        logs = sistema_evolucao.evoluir_classe(self.ladino, "assassino")

        self.assertIn("Você evoluiu para Assassino!", logs)
        self.assertEqual(self.ladino.classe, "assassino")
        self.assertEqual(self.ladino.base_destreza, destreza_antes + 3)
        self.assertEqual(self.ladino.base_inteligencia, inteligencia_antes + 1)
        self.assertIn("ataque_exposto", self.ladino.habilidades)
        self.assertIn("veneno_debilitante", self.ladino.habilidades)

    def test_evolucao_sucesso_clerigo_para_sacerdote(self):
        """Testa se a evolução de Clérigo para Sacerdote funciona."""
        self.clerigo.nivel = 16
        sabedoria_antes = self.clerigo.base_sabedoria
        inteligencia_antes = self.clerigo.base_inteligencia

        logs = sistema_evolucao.evoluir_classe(self.clerigo, "sacerdote")

        self.assertIn("Você evoluiu para Sacerdote!", logs)
        self.assertEqual(self.clerigo.classe, "sacerdote")
        self.assertEqual(self.clerigo.base_sabedoria, sabedoria_antes + 3)
        self.assertEqual(self.clerigo.base_inteligencia, inteligencia_antes + 1)
        self.assertIn("cura_em_area", self.clerigo.habilidades)
        self.assertIn("palavra_sagrada_punicao", self.clerigo.habilidades)

    def test_evolucao_falha_requisitos(self):
        """Testa se um jogador não pode evoluir se não cumprir os requisitos."""
        self.guerreiro.nivel = 10 # Nível baixo
        logs = sistema_evolucao.evoluir_classe(self.guerreiro, "mestre_de_armas")
        self.assertIn("Você não cumpre os requisitos para esta evolução.", logs)
        self.assertEqual(self.guerreiro.classe, "guerreiro") # Classe não deve mudar

if __name__ == '__main__':
    unittest.main()
