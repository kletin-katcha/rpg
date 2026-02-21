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
        self.assertIn("artesao_de_pedra", jogador.habilidades)

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
        self.assertEqual(jogador.forca, 18)

        # Defesa = (constituição // 2) + bônus_equip + bônus_passiva
        # Defesa = (19 // 2) + 8 (peitoral) + 5 (escudo) + 2 (Artesão de Pedra)
        defesa_esperada = (19 // 2) + 8 + 5 + 2
        self.assertEqual(jogador.defesa_fisica, defesa_esperada)

        # HP deve estar cheio
        self.assertEqual(jogador.hp_atual, jogador.hp_max)

    def test_sub_raca_api_aplica_modificador(self):
        """Valida leitura e aplicação de sub-raças (variações)."""
        jogador = cc_api.criar_personagem_base("Eirik")
        cc_api.aplicar_raca(jogador, "humano")

        sub_racas = cc_api.get_dados_sub_racas("humano")
        self.assertIn("nordico", sub_racas)

        constituicao_antes = jogador.base_constituicao
        cc_api.aplicar_sub_raca(jogador, "nordico")

        self.assertEqual(jogador.sub_raca, "nordico")
        self.assertEqual(jogador.base_constituicao, constituicao_antes + 1)

    def test_sub_raca_padrao_para_raca_sem_variacao_explicita(self):
        jogador = cc_api.criar_personagem_base("Krag")
        cc_api.aplicar_raca(jogador, "goliath")

        sub_racas = cc_api.get_dados_sub_racas("goliath")
        self.assertIn("goliath_tradicional", sub_racas)

        constituicao_antes = jogador.base_constituicao
        cc_api.aplicar_sub_raca(jogador, "goliath_tradicional")

        self.assertEqual(jogador.sub_raca, "goliath_tradicional")
        self.assertEqual(jogador.base_constituicao, constituicao_antes + 1)

    def test_sub_raca_sem_raca_lanca_erro(self):
        jogador = cc_api.criar_personagem_base("SemRaca")
        with self.assertRaises(ValueError):
            cc_api.aplicar_sub_raca(jogador, "nordico")

    def test_classe_secundaria_api(self):
        jogador = cc_api.criar_personagem_base("Kael")
        cc_api.aplicar_raca(jogador, "humano")
        cc_api.aplicar_classe(jogador, "guerreiro")

        total_habilidades_antes = len(jogador.habilidades)
        cc_api.aplicar_classe_secundaria(jogador, "ladino")

        self.assertEqual(jogador.classe_secundaria, "ladino")
        self.assertGreaterEqual(len(jogador.habilidades), total_habilidades_antes)

    def test_classe_secundaria_igual_principal_lanca_erro(self):
        jogador = cc_api.criar_personagem_base("Rurik")
        cc_api.aplicar_raca(jogador, "anao")
        cc_api.aplicar_classe(jogador, "guerreiro")

        with self.assertRaises(ValueError):
            cc_api.aplicar_classe_secundaria(jogador, "guerreiro")

    def test_classes_secundarias_disponiveis_filtra_classe_principal(self):
        disponiveis = cc_api.get_classes_secundarias_disponiveis("guerreiro")
        self.assertNotIn("guerreiro", disponiveis)
        self.assertIn("ladino", disponiveis)


if __name__ == '__main__':
    unittest.main()
