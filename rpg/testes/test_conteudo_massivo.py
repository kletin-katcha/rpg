import unittest

from rpg.io import criacao_personagem as cc_api


class TestConteudoMassivo(unittest.TestCase):
    def test_racas_massivas_tem_6_subracas(self):
        racas = cc_api.get_dados_racas()
        racas_massivas = [
            "alto_nordico", "bretao_arcano", "dunmer_cinzento", "bosmer_silvestre", "altmer_dourado",
            "redguard_desertico", "orc_ferreo", "khajiit_lunar", "argoniano_pantano", "imperial_legionario",
            "sylvano_ancestral", "draconato_primordial", "fae_crepuscular", "goliath_colosso", "tiefling_abissal",
            "aasimar_aurora", "anao_runaferro", "halfling_errante", "yuan_ti_oracular", "myconid_simbionte",
        ]
        for id_raca in racas_massivas:
            self.assertIn(id_raca, racas)
            self.assertEqual(len(cc_api.get_dados_sub_racas(id_raca)), 6)

    def test_classes_unicas_por_sub_raca(self):
        classes = cc_api.get_classes_unicas_por_sub_raca("alto_nordico", "alto_nordico_montanhes")
        self.assertIn("classe_alto_nordico_montanhes", classes)

    def test_arvores_com_500_ramificacoes(self):
        catalogo = cc_api.get_catalogo_arvores_habilidades()

        arvore_universal = catalogo["universais"]["universal_combate"]
        self.assertGreaterEqual(len(arvore_universal["ramificacoes"]), 500)

        arvore_classe = catalogo["classes"]["guerreiro"]
        self.assertGreaterEqual(len(arvore_classe["ramificacoes"]), 500)

        arvore_raca = catalogo["racas"]["alto_nordico"]
        self.assertGreaterEqual(len(arvore_raca["ramificacoes"]), 500)


if __name__ == "__main__":
    unittest.main()
