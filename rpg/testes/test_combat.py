import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.game_manager import GameManager
from rpg.entidades.personagem import Personagem
from rpg.entidades.monstro import Monstro
from rpg.sistemas import combate
from rpg.fabricas.fabrica_monstros import criar_monstro_por_id

class TestCombatAPI(unittest.TestCase):
    """
    Testa o sistema de combate através da nova API do GameManager.
    """

    def setUp(self):
        """Prepara um jogador e um monstro padrão para os testes."""
        self.jogador = Personagem(nome="Herói de Teste", nivel=5)
        self.jogador.base_forca = 30
        self.jogador.recalcular_stats_completos()
        self.jogador.hp_atual = self.jogador.hp_max

        self.monstro = criar_monstro_por_id("goblin_batedor")

        self.gm = GameManager()
        self.gm.jogador = self.jogador

    @patch('rpg.sistemas.combate.random')
    def test_combat_loop_via_manager(self, mock_random):
        """
        Testa um ciclo de combate completo através do GameManager.
        """
        mock_random.random.return_value = 0.0 # Garante 100% de acerto

        # Inicia o combate passando o ID do monstro
        id_monstro = self.monstro.id_monstro
        self.gm.iniciar_combate([id_monstro])
        self.assertEqual(self.gm.game_state, "combat")

        # O alvo da ação agora precisa ser o objeto monstro de dentro do estado de combate
        monstro_em_combate = self.gm.combat_state["inimigos"][0]

        from rpg.dados.ataques_base import ATAQUES_BASE
        acao_chute = {"tipo": "ataque_basico", "ataque": ATAQUES_BASE["chute"], "alvo": monstro_em_combate}

        # Executa turnos até o combate terminar
        resultado_final = {}
        for _ in range(5): # 5 ataques devem ser suficientes
            if self.gm.game_state != "combat":
                break
            resultado_final = self.gm.executar_turno_combate(acao_chute)

        # Verifica o resultado final
        self.assertEqual(resultado_final.get("resultado"), "vitoria")
        self.assertFalse(monstro_em_combate.esta_vivo())
        self.assertTrue(self.jogador.esta_vivo())
        self.assertEqual(self.gm.game_state, "in_game")


if __name__ == '__main__':
    unittest.main()
