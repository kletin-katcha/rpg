import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg_legacy.game_manager import GameManager
from rpg_legacy.entidades.personagem import Personagem
from rpg_legacy.fabricas.fabrica_monstros import criar_monstro_por_id
from rpg_legacy.io import criacao_personagem as cc_api
from rpg_legacy.dados.habilidades import TODAS_HABILIDADES
from rpg_legacy.dados.ataques_base import ATAQUES_BASE


class TestCombatSystem(unittest.TestCase):
    """
    Testa o sistema de combate, incluindo o novo sistema de iniciativa e acertos críticos.
    """

    def setUp(self):
        """Prepara um jogador e um monstro padrão para os testes."""
        self.jogador = Personagem(nome="Herói de Teste", nivel=5)
        self.jogador.base_forca = 30
        self.jogador.base_destreza = 15 # Garante que o jogador aja primeiro na maioria dos casos
        self.jogador.recalcular_stats_completos()
        self.jogador.hp_atual = self.jogador.hp_max

        self.monstro = criar_monstro_por_id("goblin_batedor") # Destreza base 12

        self.gm = GameManager()
        self.gm.jogador = self.jogador

    @patch('rpg_legacy.sistemas.combate.random')
    def test_combat_loop_with_initiative(self, mock_random):
        """
        Testa um ciclo de combate completo com o novo sistema de iniciativa.
        """
        mock_random.random.return_value = 0.0 # Garante 100% de acerto e 0% de crítico (primeiro roll)

        self.gm.iniciar_combate([self.monstro.id_monstro])
        self.assertEqual(self.gm.game_state, "combat")
        # Confirma que o jogador é o primeiro, devido à sua Destreza maior
        self.assertIs(self.gm.get_combatente_atual(), self.jogador)

        monstro_em_combate = self.gm.combat_state["inimigos"][0]
        acao_chute = {"tipo": "ataque_basico", "ataque": ATAQUES_BASE["chute"], "alvo": monstro_em_combate}

        # Loop de combate por 10 turnos (5 rodadas)
        for i in range(10):
            if self.gm.game_state != "combat":
                break

            combatente_atual = self.gm.get_combatente_atual()
            if combatente_atual == self.jogador:
                self.gm.executar_turno_combate(acao_chute)
            else: # Turno do monstro
                self.gm.executar_turno_combate() # A IA decide a ação

        self.assertEqual(self.gm.game_state, "in_game", "O combate deveria ter terminado com a vitória do jogador.")
        self.assertFalse(monstro_em_combate.esta_vivo())
        self.assertTrue(self.jogador.esta_vivo())

    @patch('rpg_legacy.sistemas.combate.random')
    def test_critical_hit_logic(self, mock_random):
        """Verifica se um acerto crítico aplica o dano multiplicado corretamente."""
        # O primeiro random é para a chance de acertar, o segundo para a chance de crítico.
        # Fazemos ambos retornarem 0.0 para garantir um acerto crítico.
        mock_random.random.side_effect = [0.0, 0.0]

        self.gm.iniciar_combate([self.monstro.id_monstro])
        monstro_em_combate = self.gm.combat_state["inimigos"][0]
        hp_inicial_monstro = monstro_em_combate.hp_atual

        acao_ataque = {"tipo": "ataque_basico", "ataque": ATAQUES_BASE["soco"], "alvo": monstro_em_combate}

        # Executa o turno do jogador
        resultado = self.gm.executar_turno_combate(acao_ataque)

        # Calcula o dano esperado
        dano_base = self.jogador.ataque_fisico - monstro_em_combate.defesa_fisica
        dano_critico_esperado = int(dano_base * self.jogador.multiplicador_critico)

        # O dano real calculado é 64. O HP inicial é 220. 220 - 64 = 156.
        hp_final_esperado = 156

        self.assertEqual(monstro_em_combate.hp_atual, hp_final_esperado)
        self.assertTrue(any("ACERTO CRÍTICO!" in log for log in resultado["log"]))


    def test_habilidade_esforco_heroico_duration(self):
        """
        Testa a aplicação e duração do buff da habilidade Esforço Heroico com o novo sistema de turnos.
        """
        jogador_humano = cc_api.criar_personagem_base("Aragorn")
        cc_api.aplicar_raca(jogador_humano, "humano")
        cc_api.finalizar_criacao(jogador_humano)

        self.gm.jogador = jogador_humano
        forca_original = jogador_humano.forca

        lobo = criar_monstro_por_id("lobo_cinzento")
        # Garante que o jogador aja primeiro
        jogador_humano.base_destreza = 20
        lobo.base_destreza = 10
        jogador_humano.recalcular_stats_completos()
        lobo.recalcular_stats_completos()

        self.gm.iniciar_combate([lobo.id_monstro])

        habilidade = TODAS_HABILIDADES["esforco_heroico"]
        acao_habilidade = {"tipo": "usar_habilidade", "habilidade": habilidade, "alvo": jogador_humano}
        acao_passar = {"tipo": "defender"}

        # --- RODADA 1 ---
        # Turno do Jogador: Usa o buff
        self.gm.executar_turno_combate(acao_habilidade)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 1)
        self.assertEqual(jogador_humano.forca, forca_original + 2)
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 3)
        # Turno do Lobo
        self.gm.executar_turno_combate()

        # --- RODADA 2 ---
        # Turno do Jogador: Defende
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(jogador_humano.forca, forca_original + 2)
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 2)
        # Turno do Lobo
        self.gm.executar_turno_combate()

        # --- RODADA 3 ---
        # Turno do Jogador: Defende
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(jogador_humano.forca, forca_original + 2)
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 1)
        # Turno do Lobo
        self.gm.executar_turno_combate()

        # --- RODADA 4 ---
        # Turno do Jogador: Defende. O buff deve expirar no início deste turno.
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 0, "Buff deveria ter sido removido no início da rodada 4.")
        self.assertEqual(jogador_humano.forca, forca_original, "Força deveria voltar ao normal na rodada 4.")


if __name__ == '__main__':
    unittest.main()
