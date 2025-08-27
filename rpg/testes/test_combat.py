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
        max_turnos = 20 # Safety break
        turnos_executados = 0
        while self.gm.game_state == "combat" and turnos_executados < max_turnos:
            # A ação do jogador só é relevante no turno dele.
            acao_turno = None
            if self.gm.get_combatente_atual() == self.jogador:
                acao_turno = acao_chute

            resultado_final = self.gm.executar_turno_combate(acao_turno)
            turnos_executados += 1

        # Verifica o resultado final
        self.assertEqual(resultado_final.get("resultado"), "vitoria", f"Combate não terminou em vitória após {turnos_executados} turnos.")
        self.assertFalse(monstro_em_combate.esta_vivo())
        self.assertTrue(self.jogador.esta_vivo())
        self.assertEqual(self.gm.game_state, "in_game")

    def test_habilidade_esforco_heroico(self):
        """
        Testa a aplicação e duração do buff da habilidade Esforço Heroico.
        A lógica correta é: um buff de 3 turnos é ativo no turno 1, 2 e 3.
        No início do turno 4, ele expira.
        """
        jogador_humano = cc_api.criar_personagem_base("Aragorn")
        cc_api.aplicar_raca(jogador_humano, "humano")
        cc_api.finalizar_criacao(jogador_humano)
        self.gm.jogador = jogador_humano
        forca_original = jogador_humano.forca
        self.gm.iniciar_combate(["lobo_cinzento"])

        habilidade = TODAS_HABILIDADES["esforco_heroico"]
        acao_habilidade = {"tipo": "usar_habilidade", "habilidade": habilidade, "alvo": jogador_humano}
        acao_passar = {"tipo": "passar_turno"}

        # Função auxiliar para garantir que a ação correta seja executada no turno do jogador
        def executar_turno_jogador(acao):
            max_tentativas = 10
            for _ in range(max_tentativas):
                if self.gm.get_combatente_atual() == self.gm.jogador:
                    self.gm.executar_turno_combate(acao)
                    return
                else:
                    self.gm.executar_turno_combate(None) # Turno do monstro
            self.fail("O turno do jogador não chegou no tempo esperado.")

        # --- TURNO 1: Jogador usa o buff ---
        executar_turno_jogador(acao_habilidade)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 1, "Buff deveria ter sido aplicado.")
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria estar buffada após turno 1.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].duracao_original, 3, "Duração inicial deveria ser 3.")

        # --- TURNO 2: O buff continua ativo ---
        executar_turno_jogador(acao_passar)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 1, "Buff deveria continuar ativo no turno 2.")
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria continuar buffada no turno 2.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 2, "Duração deveria ser 2 após turno 2.")

        # --- TURNO 3: O buff continua ativo ---
        executar_turno_jogador(acao_passar)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 1, "Buff deveria continuar ativo no turno 3.")
        self.assertEqual(jogador_humano.forca, forca_original + 2, "Força deveria continuar buffada no turno 3.")
        self.assertEqual(jogador_humano.efeitos_ativos[0].turnos_restantes, 1, "Duração deveria ser 1 após turno 3.")

        # --- TURNO 4: O buff deve expirar no início deste turno ---
        executar_turno_jogador(acao_passar)
        self.assertEqual(len(jogador_humano.efeitos_ativos), 0, "Buff deveria ter sido removido no início do turno 4.")
        self.assertEqual(jogador_humano.forca, forca_original, "Força deveria voltar ao normal no turno 4.")

    def test_usar_item_em_combate(self):
        """Testa se o jogador pode usar um item consumível durante o combate."""
        # Configuração inicial
        self.jogador.hp_atual = 100
        self.jogador.adicionar_item("pocao_cura_fraca", 1)
        self.assertTrue("pocao_cura_fraca" in self.jogador.inventario)
        hp_antes = self.jogador.hp_atual

        # Inicia o combate
        self.gm.iniciar_combate([self.monstro.id_monstro])
        self.assertEqual(self.gm.game_state, "combat")

        # Define a ação de usar o item
        acao_usar_item = {"tipo": "usar_item", "id_item": "pocao_cura_fraca"}

        # Garante que seja o turno do jogador antes de executar a ação
        if self.gm.get_combatente_atual() != self.jogador:
            self.gm.executar_turno_combate(None) # Passa o turno do monstro

        # Executa o turno do jogador com a ação de usar item
        self.gm.executar_turno_combate(acao_usar_item)

        # Verificações
        hp_depois = self.jogador.hp_atual
        self.assertGreater(hp_depois, hp_antes, "O HP do jogador deveria ter aumentado após usar a poção.")
        self.assertFalse("pocao_cura_fraca" in self.jogador.inventario, "A poção deveria ter sido removida do inventário.")

    @patch('rpg.entidades.monstro.random.random')
    def test_cooldown_habilidade_monstro(self, mock_random_func):
        """Testa se a IA do monstro respeita os cooldowns das habilidades."""
        mock_random_func.return_value = 0.0 # Garante que a IA sempre tente usar a habilidade

        self.gm.iniciar_combate(["lobo_alfa"])
        monstro = self.gm.combat_state["inimigos"][0]

        # Garante uma ordem de turno previsível para o teste
        self.gm.combat_state["todos_combatentes"] = [monstro, self.jogador]

        # TURNO 1 (Monstro): Deve usar a habilidade
        self.gm.clear_log()
        self.gm.executar_turno_combate(None)
        self.assertIn("Mordida Feroz", self.gm.game_log[0])
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 3)

        # TURNO 2 (Jogador): Passa o turno
        self.gm.executar_turno_combate({"tipo": "passar_turno"})
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 3, "Cooldown não deve mudar no turno do jogador.")

        # TURNO 3 (Monstro): Cooldown deve diminuir para 2. Habilidade não deve ser usada.
        self.gm.clear_log()
        self.gm.executar_turno_combate(None)
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 2)
        self.assertNotIn("Mordida Feroz", self.gm.game_log[0])

        # TURNO 4 (Jogador): Passa o turno
        self.gm.executar_turno_combate({"tipo": "passar_turno"})
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 2)

        # TURNO 5 (Monstro): Cooldown deve diminuir para 1.
        self.gm.clear_log()
        self.gm.executar_turno_combate(None)
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 1)
        self.assertNotIn("Mordida Feroz", self.gm.game_log[0])

        # TURNO 6 (Jogador): Passa o turno
        self.gm.executar_turno_combate({"tipo": "passar_turno"})
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 1)

        # TURNO 7 (Monstro): Cooldown deve diminuir para 0 e ser usada de novo, resetando para 3.
        self.gm.clear_log()
        self.gm.executar_turno_combate(None)
        self.assertIn("Mordida Feroz", self.gm.game_log[0])
        self.assertEqual(monstro.cooldowns_habilidades["Mordida Feroz"], 3)


if __name__ == '__main__':
    unittest.main()
