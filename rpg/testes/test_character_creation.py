import unittest
import os
import sys

# Adiciona o diretório raiz do projeto ao sys.path
if os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from rpg.io import criacao_personagem as cc_api
from rpg.entidades.personagem import Personagem

class TestCharacterCreationAPI(unittest.TestCase):
    """
    Testa a API de lógica de criação de personagem.
    """

    def test_character_creation_api_flow(self):
        """
        Testa o fluxo de criação de personagem através das novas funções da API,
        verificando se o personagem final tem os atributos corretos.
        """
        # 1. Cria o personagem base
        jogador = cc_api.criar_personagem_base("Durin")
        self.assertEqual(jogador.nome, "Durin")

        # 2. Aplica a raça
        cc_api.aplicar_raca(jogador, "anao")
        self.assertEqual(jogador.raca, "anao")
        # Verifica bônus racial: Força base 5 + 3 = 8
        self.assertEqual(jogador.base_forca, 8)
        self.assertIn("resistencia_a_veneno", jogador.habilidades)

        # 3. Aplica a classe
        cc_api.aplicar_classe(jogador, "guerreiro")
        self.assertEqual(jogador.classe, "guerreiro")
        self.assertIn("ataque_poderoso", jogador.habilidades)
        # Verifica se o equipamento inicial foi equipado
        self.assertIsNotNone(jogador.equipamentos.get("arma_principal"))
        self.assertEqual(jogador.equipamentos["arma_principal"].id_item, "espada_curta_ferro")

        # 4. Aplica os atributos
        pontos = {"forca": 10, "constituicao": 10}
        cc_api.aplicar_atributos(jogador, pontos)
        # Força: 8 (base racial) + 10 (distribuído) = 18
        self.assertEqual(jogador.base_forca, 18)
        # Constituição: 5 (padrão) + 4 (racial) + 10 (distribuído) = 19
        self.assertEqual(jogador.base_constituicao, 19)

        # 5. Finaliza a criação
        jogador = cc_api.finalizar_criacao(jogador)

        # Verifica os stats finais (calculados)
        # Força total deve ser igual à base, pois não há itens com bônus de força
        self.assertEqual(jogador.forca, 18)
        # Defesa deve ser calculada a partir da constituição total
        # Defesa = constituição // 2 = 19 // 2 = 9
        # Mais bônus de armadura e escudo
        defesa_esperada = (19 // 2) + 8 + 5 # 9 (base) + 8 (peitoral) + 5 (escudo)
        self.assertEqual(jogador.defesa_fisica, defesa_esperada)
        # HP deve estar cheio
        self.assertEqual(jogador.hp_atual, jogador.hp_max)


if __name__ == '__main__':
    unittest.main()
