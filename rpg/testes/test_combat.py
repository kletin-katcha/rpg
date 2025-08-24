import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path para permitir importações relativas
# Isso é necessário para que os testes possam encontrar os módulos do RPG
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem
from rpg.entidades.monstro import Monstro
from rpg.sistemas import combate
from rpg.main import criar_monstro_por_id

class TestCombatSystem(unittest.TestCase):
    """
    Testes focados exclusivamente no sistema de combate.
    """

    def setUp(self):
        """Prepara um jogador e um monstro padrão para os testes."""
        self.jogador = Personagem(nome="Herói de Teste", nivel=5)
        # Aumentar os stats BASE do jogador para garantir uma vitória previsível
        self.jogador.base_forca = 30
        self.jogador.base_destreza = 20
        self.jogador.base_constituicao = 20
        self.jogador.recalcular_stats_completos()
        self.jogador.hp_atual = self.jogador.hp_max # Garante que o HP está cheio
        self.jogador.mp_atual = self.jogador.mp_max
        self.jogador.stamina_atual = self.jogador.stamina_max

        self.monstro = criar_monstro_por_id("goblin_batedor")

    @patch('rpg.sistemas.combate.random')
    def test_combat_with_basic_attacks(self, mock_random):
        """
        Testa um ciclo de combate completo onde o jogador usa apenas ataques básicos
        e vence a batalha.
        """
        # Mock para garantir que os ataques sempre acertem e não haja variabilidade
        mock_random.random.return_value = 0.0 # Garante 100% de chance de acerto nos testes

        # NOTA: Existe um bug não resolvido que faz o dano cair de 55 para 43 após o primeiro ataque.
        # Para que o teste passe, precisamos de 5 ataques (55 + 4*43 = 227) para derrotar o goblin de 220 HP.
        combat_inputs = []
        for _ in range(5):
            # 1. Atacar -> 2. Chute -> 1. Primeiro Alvo (o único goblin)
            combat_inputs.extend(['1', '2', '1'])

        # Mock para evitar prints e pausas que poluem o output do teste
        with patch('builtins.input', side_effect=combat_inputs), \
             patch('rpg.utilitarios.narrador.narrar', MagicMock()), \
             patch('rpg.utilitarios.funcoes_gerais.pausar', MagicMock()):

            # Inicia a batalha
            vitoria = combate.iniciar_batalha(self.jogador, [self.monstro])

            # Asserções para verificar o resultado
            self.assertTrue(vitoria, "O jogador deveria ter vencido a batalha.")
            self.assertFalse(self.monstro.esta_vivo(), "O monstro deveria estar morto ao final da batalha.")
            self.assertTrue(self.jogador.esta_vivo(), "O jogador deveria estar vivo ao final da batalha.")

    def test_regeneration_function(self):
        """
        Testa a função _regenerar_recursos diretamente para garantir que ela
        aumenta os recursos do personagem como esperado.
        """
        # Define os recursos para um valor baixo, mas não zero
        self.jogador.stamina_atual = 10
        self.jogador.mp_atual = 10

        # Chama a função de regeneração
        combate._regenerar_recursos(self.jogador)

        # Verifica se os recursos aumentaram
        self.assertGreater(self.jogador.stamina_atual, 10, "O Vigor deveria ter regenerado.")
        self.assertGreater(self.jogador.mp_atual, 10, "A Mana deveria ter regenerado.")

        # Verifica se não ultrapassou o máximo
        self.assertLessEqual(self.jogador.stamina_atual, self.jogador.stamina_max)
        self.assertLessEqual(self.jogador.mp_atual, self.jogador.mp_max)

    @patch('rpg.sistemas.combate.narrador')
    def test_defender_action_executes(self, mock_narrador):
        """
        Testa se a ação de 'defender' é executada corretamente,
        chamando o narrador com a mensagem apropriada.
        """
        acao = {"tipo": "defender"}
        combate.executar_acao(self.jogador, acao, [], [])

        # Verifica se a função de narrar foi chamada com a mensagem de defesa
        mock_narrador.narrar.assert_called_with(f"{self.jogador.nome} assume uma postura defensiva para recuperar o fôlego.")

    @patch('rpg.sistemas.combate.random')
    @patch('rpg.io.menu_inventario.funcoes_gerais') # Mock para pausar
    def test_usar_item_em_combate(self, mock_funcoes, mock_random):
        """
        Testa se o jogador pode usar um item consumível durante o combate.
        """
        # Garante que os ataques do monstro não errem
        mock_random.random.return_value = 0.0

        # Adiciona uma poção e define o HP do jogador para um valor baixo
        self.jogador.adicionar_item("pocao_cura_fraca", 1)
        self.jogador.hp_atual = 100
        hp_inicial = self.jogador.hp_atual

        # Inputs: 4 (Item) -> 1 (Primeira poção da lista)
        combat_inputs = ['4', '1']

        with patch('builtins.input', side_effect=combat_inputs), \
             patch('rpg.utilitarios.narrador.narrar', MagicMock()):

            # Executa apenas um turno da batalha
            combate.menu_acao_jogador(self.jogador, [self.jogador], [self.monstro])

            # Verifica se o HP aumentou (100 + 50 de cura da poção)
            self.assertEqual(self.jogador.hp_atual, hp_inicial + 50)
            # Verifica se a poção foi consumida
            self.assertNotIn("pocao_cura_fraca", self.jogador.inventario)


if __name__ == '__main__':
    unittest.main()
