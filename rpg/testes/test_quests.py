import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem
from rpg.sistemas import quests

class TestQuestSystem(unittest.TestCase):
    """
    Testes focados exclusivamente no sistema de quests.
    """

    def setUp(self):
        """Prepara um jogador padrão para os testes."""
        self.jogador = Personagem(nome="Caçador de Quests", nivel=1)
        self.jogador.ouro = 0
        self.jogador.xp_atual = 0

    def test_quest_start_and_completion(self):
        """
        Testa o ciclo de vida completo de uma quest: iniciar, progredir e concluir.
        Usa a quest "mq02_ameaca_local" que requer matar 5 monstros.
        """
        id_quest = "mq02_ameaca_local"
        id_alvo_quest = "goblin_batedor"

        # Adiciona o pré-requisito para a quest poder ser iniciada
        self.jogador.quests_concluidas.append("mq01_despertar")

        # 1. Iniciar a quest
        with patch('rpg.utilitarios.narrador.narrar', MagicMock()):
            quests.iniciar_quest(self.jogador, id_quest)

        self.assertEqual(len(self.jogador.quests_ativas), 1)
        self.assertEqual(self.jogador.quests_ativas[0].id_quest, id_quest)
        self.assertFalse(self.jogador.quests_ativas[0].esta_completa())

        # 2. Progredir na quest
        with patch('rpg.utilitarios.narrador.narrar', MagicMock()):
            # Simula a morte de 5 goblins
            for _ in range(5):
                quests.atualizar_progresso_quests(self.jogador, "matar", id_alvo_quest)
            # Simula o retorno ao NPC
            quests.atualizar_progresso_quests(self.jogador, "retornar_para", "elara_curandeira")

        # Verifica se a quest está pronta para ser entregue
        self.assertTrue(self.jogador.quests_ativas[0].esta_completa())

        # 3. Concluir a quest
        quest_original = self.jogador.quests_ativas[0]
        xp_recompensa = quest_original.recompensas.get("xp", 0)
        ouro_recompensa = quest_original.recompensas.get("ouro", 0)

        with patch('rpg.utilitarios.narrador.narrar', MagicMock()):
             quests.concluir_quest(self.jogador, quest_original)

        # 4. Verificar o resultado
        self.assertEqual(len(self.jogador.quests_ativas), 0)
        self.assertIn(id_quest, self.jogador.quests_concluidas)
        # O jogador sobe de nível (precisa de 100 XP), então o XP atual será o resto.
        xp_esperado = xp_recompensa - 100
        self.assertEqual(self.jogador.xp_atual, xp_esperado)
        self.assertEqual(self.jogador.ouro, ouro_recompensa)


if __name__ == '__main__':
    unittest.main()
