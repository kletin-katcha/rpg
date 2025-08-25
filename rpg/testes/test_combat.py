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
from rpg.io import criacao_personagem as cc_api
from rpg.dados.habilidades import TODAS_HABILIDADES


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

    def test_habilidade_esforco_heroico(self):
        """
        Testa a aplicação e duração do buff da habilidade Esforço Heroico.
        A lógica correta é: um buff de 3 turnos é ativo no turno 1, 2 e 3.
        No início do turno 4, ele expira.
        """
        # Cria um Humano para garantir que ele tenha a habilidade
        jogador_humano = cc_api.criar_personagem_base("Aragorn")
        cc_api.aplicar_raca(jogador_humano, "humano")
        cc_api.finalizar_criacao(jogador_humano)

        self.gm.jogador = jogador_humano
        forca_original = jogador_humano.forca

        self.gm.iniciar_combate(["lobo_cinzento"])

        # Ação: Usar Esforço Heroico
        habilidade = TODAS_HABILIDADES["esforco_heroico"]
        acao_habilidade = {"tipo": "usar_habilidade", "habilidade": habilidade, "alvo": jogador_humano}
        acao_passar = {"tipo": "defender"}

        # --- TURNO 1: Jogador usa o buff ---
        # Efeitos são processados no início do turno, mas não há nenhum ainda.
        # Jogador usa a skill. Buff é aplicado.
        self.gm.executar_turno_combate(acao_habilidade)

        self.assertEqual(len(jogador_humano.efeitos_ativos), 1, "Buff deveria ter sido aplicado.")
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria estar buffada após turno 1.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 3, "Duração deveria ser 3 após aplicação.")

        # --- TURNO 2: O buff continua ativo ---
        # No início deste turno, tick() é chamado. Duração vai para 2.
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria continuar buffada no turno 2.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 2, "Duração deveria ser 2 após turno 2.")

        # --- TURNO 3: O buff continua ativo ---
        # No início deste turno, tick() é chamado. Duração vai para 1.
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria continuar buffada no turno 3.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 1, "Duração deveria ser 1 após turno 3.")

        # --- TURNO 4: O buff deve expirar no início deste turno ---
        # No início deste turno, tick() é chamado. Duração vai para 0. Efeito é removido. Stats são recalculados.
        # A ação do jogador (defender) acontece com os stats normais.
        self.gm.executar_turno_combate(acao_passar)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 0, "Buff deveria ter sido removido no início do turno 4.")
        self.assertEqual(jogador_humano.forca, forca_original, "Força deveria voltar ao normal no turno 4.")


if __name__ == '__main__':
    unittest.main()
