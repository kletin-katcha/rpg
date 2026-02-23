import unittest

from rpg.game import Game


class TestPhase1To25EndToEnd(unittest.TestCase):
    def test_jornada_completa_fases_1_25(self):
        g = Game()

        # Fase 1: criação
        jogador = g.criar_jogador("Arin", "humano", "guerreiro")
        self.assertEqual(jogador.nome, "Arin")

        # Fases 2-5: núcleo combate/economia/cidade
        g.executar_acao_cidade("coletar_item_inicial")
        self.assertGreaterEqual(g.state.inventario.get("pocao_cura", 0), 1)
        g.executar_acao_cidade("cacar_lobo")
        g.executar_acao_cidade("construir_oficina")
        g.executar_acao_cidade("avancar_dia")
        self.assertGreaterEqual(g.state.dia_economico, 1)

        # Fases 6-9: persistência/contratos
        g.executar_acao_cidade("contrato_aleatorio")
        self.assertIsNotNone(g.state.contrato_ativo)
        g.executar_acao_cidade("concluir_contrato")

        # Fases 10-15: facções, habilidades, imersão, diretor de mundo
        g.executar_acao_cidade("resgatar_beneficio_faccao")
        g.executar_acao_cidade("ver_arvore")
        g.executar_acao_cidade("desbloquear_postura_ofensiva")
        g.executar_acao_cidade("ver_clima")
        g.executar_acao_cidade("gerar_arco_mundo")
        g.executar_acao_cidade("aplicar_mutador")

        # Fases 16-20: validações, combate situacional e crise
        condicoes = g.executar_acao_cidade("ver_condicoes_combate")
        self.assertIn("bonus_dano_personagem", condicoes)
        g.executar_acao_cidade("iniciar_cadeia_contratos")
        self.assertEqual(len(g.state.cadeia_contratos), 3)
        g.executar_acao_cidade("gerar_tensao_faccoes")
        g.executar_acao_cidade("gerar_crise_urbana")
        self.assertTrue(isinstance(g.state.crise_urbana, dict))

        # Fases 21-25: expansão massiva
        regiao = g.executar_acao_cidade("ver_regiao")
        self.assertIn("Região atual", regiao)
        g.executar_acao_cidade("viajar_fronteira_norte")
        self.assertEqual(g.state.regiao_atual, "fronteira_norte")

        g.executar_acao_cidade("gerar_dungeon")
        xp_antes = g.state.jogador.xp
        nivel_antes = g.state.jogador.nivel
        g.executar_acao_cidade("explorar_dungeon")
        self.assertTrue(g.state.dungeon_ativa["concluida"])
        self.assertTrue(g.state.jogador.nivel > nivel_antes or g.state.jogador.xp != xp_antes)

        agenda_msg = g.executar_acao_cidade("rodar_agenda_faccoes")
        self.assertIn("tensão=", agenda_msg)

        g.executar_acao_cidade("iniciar_arco_longo")
        g.executar_acao_cidade("avancar_arco_longo")
        arco = g.executar_acao_cidade("ver_arco_longo")
        self.assertIn("Ascensão das Cinzas", arco)

        pacote = g.executar_acao_cidade("gerar_pacote_expansao")
        self.assertIn("fase25_item_", pacote)
        simulacao = g.executar_acao_cidade("simular_balance_headless")
        self.assertIn("taxa_vitoria", simulacao)


if __name__ == "__main__":
    unittest.main()
