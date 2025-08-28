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

        self.barbaro = Personagem(nome="Barbaro de Teste")
        cc_api.aplicar_classe(self.barbaro, "barbaro")

        self.ranger = Personagem(nome="Ranger de Teste")
        cc_api.aplicar_classe(self.ranger, "ranger")

        self.bardo = Personagem(nome="Bardo de Teste")
        cc_api.aplicar_classe(self.bardo, "bardo")

    def test_evolucao_disponivel(self):
        """Testa se as evoluções são listadas corretamente para um personagem de nível alto."""
        self.guerreiro.nivel = 15
        evolucoes = sistema_evolucao.get_evolucoes_disponiveis(self.guerreiro)
        self.assertEqual(len(evolucoes), 2)

    def test_evolucao_indisponivel_nivel_baixo(self):
        """Testa se nenhuma evolução é listada para um personagem de nível baixo."""
        self.guerreiro.nivel = 10
        evolucoes = sistema_evolucao.get_evolucoes_disponiveis(self.guerreiro)
        self.assertEqual(len(evolucoes), 0)

    def test_evolucao_sucesso_guerreiro(self):
        """Testa se a evolução de Guerreiro para Mestre de Armas funciona."""
        self.guerreiro.nivel = 20
        logs = sistema_evolucao.evoluir_classe(self.guerreiro, "mestre_de_armas")
        self.assertIn("Você evoluiu para Mestre de Armas!", logs)
        self.assertEqual(self.guerreiro.classe, "mestre_de_armas")
        self.assertIn("postura_de_mestre", self.guerreiro.habilidades)

    def test_evolucao_sucesso_ladino(self):
        """Testa se a evolução de Ladino para Assassino funciona."""
        self.ladino.nivel = 15
        logs = sistema_evolucao.evoluir_classe(self.ladino, "assassino")
        self.assertIn("Você evoluiu para Assassino!", logs)
        self.assertEqual(self.ladino.classe, "assassino")
        self.assertIn("ataque_exposto", self.ladino.habilidades)

    def test_evolucao_sucesso_clerigo(self):
        """Testa se a evolução de Clérigo para Sacerdote funciona."""
        self.clerigo.nivel = 16
        logs = sistema_evolucao.evoluir_classe(self.clerigo, "sacerdote")
        self.assertIn("Você evoluiu para Sacerdote!", logs)
        self.assertEqual(self.clerigo.classe, "sacerdote")
        self.assertIn("cura_em_area", self.clerigo.habilidades)

    def test_evolucao_sucesso_barbaro(self):
        """Testa se a evolução de Bárbaro para Protetor Ancestral funciona."""
        self.barbaro.nivel = 15
        logs = sistema_evolucao.evoluir_classe(self.barbaro, "protetor_ancestral")
        self.assertIn("Você evoluiu para Protetor Ancestral!", logs)
        self.assertEqual(self.barbaro.classe, "protetor_ancestral")
        self.assertIn("totem_de_protecao", self.barbaro.habilidades)

    def test_evolucao_falha_requisitos(self):
        """Testa se um jogador não pode evoluir se não cumprir os requisitos."""
        self.guerreiro.nivel = 10
        logs = sistema_evolucao.evoluir_classe(self.guerreiro, "mestre_de_armas")
        self.assertIn("Você não cumpre os requisitos para esta evolução.", logs)
        self.assertEqual(self.guerreiro.classe, "guerreiro")

if __name__ == '__main__':
    unittest.main()
