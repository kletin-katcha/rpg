import unittest
from unittest.mock import patch
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.entidades.personagem import Personagem

class TestEquipmentSystem(unittest.TestCase):
    """
    Testes focados no sistema de equipamentos e seus efeitos nos status.
    """

    def setUp(self):
        """Prepara um jogador padrão para os testes."""
        # Mockando o print para evitar poluir a saída do teste com logs de inventário
        patcher = patch('builtins.print')
        self.addCleanup(patcher.stop)
        self.mock_print = patcher.start()

        self.jogador = Personagem(nome="Testador de Equipamentos", nivel=5)
        # Adiciona alguns itens para testar
        self.jogador.adicionar_item("espada_curta_ferro", 1)
        self.jogador.adicionar_item("peitoral_de_couro_batido", 1)

    def test_equip_weapon_and_apply_damage_bonus(self):
        """
        Testa se equipar uma arma aumenta o dano_arma_bonus sem alterar
        o ataque_fisico base, e se desequipar remove o bônus.
        """
        # Stats antes de equipar
        ataque_fisico_antes = self.jogador.ataque_fisico
        dano_bonus_antes = self.jogador.dano_arma_bonus
        self.assertEqual(dano_bonus_antes, 0)

        # Equipa a espada
        self.jogador.equipar_item("espada_curta_ferro")

        # Stats depois de equipar
        ataque_fisico_depois = self.jogador.ataque_fisico
        dano_bonus_depois = self.jogador.dano_arma_bonus

        # O ataque físico base (de Força) não deve mudar
        self.assertEqual(ataque_fisico_antes, ataque_fisico_depois)
        # O bônus de dano da arma deve ter sido adicionado
        self.assertEqual(dano_bonus_depois, 8) # Valor da "espada_curta_ferro"

        # Desequipa a espada
        self.jogador.desequipar_item("arma_principal")

        # O bônus de dano deve voltar a zero
        self.assertEqual(self.jogador.dano_arma_bonus, 0)

    def test_equip_armor_and_apply_stat_bonus(self):
        """
        Testa se equipar uma armadura aumenta um atributo primário (Constituição)
        e, consequentemente, os atributos derivados (defesa_fisica, hp_max).
        """
        # Stats antes de equipar
        constituicao_antes = self.jogador.base_constituicao
        defesa_antes = self.jogador.defesa_fisica
        hp_max_antes = self.jogador.hp_max

        # Equipa o peitoral
        self.jogador.equipar_item("peitoral_de_couro_batido")

        # Stats depois de equipar
        constituicao_depois = self.jogador.constituicao
        defesa_depois = self.jogador.defesa_fisica
        hp_max_depois = self.jogador.hp_max

        # A constituição total deve ser a base + bônus do item (que não tem, mas vamos checar defesa)
        # O peitoral dá +8 de defesa_fisica diretamente.
        self.assertGreater(defesa_depois, defesa_antes)
        self.assertEqual(defesa_depois, defesa_antes + 8)

        # O HP não deve mudar, pois o item não dá constituição
        self.assertEqual(hp_max_depois, hp_max_antes)

        # Desequipa o peitoral
        self.jogador.desequipar_item("peitoral")

        # Stats devem voltar ao normal
        self.assertEqual(self.jogador.defesa_fisica, defesa_antes)


if __name__ == '__main__':
    unittest.main()
