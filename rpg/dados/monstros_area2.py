# ==============================================================================
# ARQUIVO DE DADOS: MONSTROS (ÁREA 2 - PÂNTANO SOMBRIO)
# ==============================================================================
#
# Este arquivo contém as definições para os monstros encontrados na segunda
# área do jogo, o Pântano Sombrio.
#
# ==============================================================================

MONSTROS_AREA2 = {
    "sanguessuga_gigante": {
        "nome": "Sanguessuga Gigante",
        "nivel": 8,
        "familia": "Besta",
        "xp_recompensa": 40,
        "ouro_recompensa": 25,
        "stats_base": {"forca": 12, "destreza": 14, "constituicao": 15, "inteligencia": 2, "sabedoria": 8, "sorte": 5},
        "habilidades_ids": ["mordida_drenante"],
        "ataques_base_ids": ["soco"],
        "loot_table": [
            {"id_item": "carne_de_monstro", "chance": 0.8, "quantidade": [1, 2]},
            {"id_item": "glandula_de_sanguessuga", "chance": 0.3, "quantidade": [1, 1]}
        ]
    },
    "homem_lagarto_guerreiro": {
        "nome": "Homem-Lagarto Guerreiro",
        "nivel": 10,
        "familia": "Reptiliano",
        "xp_recompensa": 60,
        "ouro_recompensa": 40,
        "stats_base": {"forca": 16, "destreza": 12, "constituicao": 14, "inteligencia": 7, "sabedoria": 10, "sorte": 6},
        "habilidades_ids": ["golpe_de_cauda", "golpe_com_escudo"],
        "ataques_base_ids": ["soco", "chute"],
        "loot_table": [
            {"id_item": "escama_de_homem_lagarto", "chance": 0.75, "quantidade": [1, 3]},
            {"id_item": "lanca_primitiva", "chance": 0.1, "quantidade": [1, 1]}
        ]
    },
    "espectro_do_pantano": {
        "nome": "Espectro do Pântano",
        "nivel": 12,
        "familia": "Morto-vivo",
        "xp_recompensa": 85,
        "ouro_recompensa": 10,
        "stats_base": {"forca": 5, "destreza": 16, "constituicao": 10, "inteligencia": 14, "sabedoria": 12, "sorte": 8},
        "habilidades_ids": ["toque_gelido", "assombrar"],
        "ataques_base_ids": [],
        "loot_table": [
            {"id_item": "essencia_espectral", "chance": 0.5, "quantidade": [1, 2]},
            {"id_item": "po_ectoplasmico", "chance": 0.2, "quantidade": [1, 1]}
        ]
    },
    "crocodilo_gigante": {
        "nome": "Crocodilo Gigante",
        "nivel": 15,
        "familia": "Besta",
        "xp_recompensa": 120,
        "ouro_recompensa": 70,
        "stats_base": {"forca": 22, "destreza": 8, "constituicao": 20, "inteligencia": 3, "sabedoria": 8, "sorte": 5},
        "habilidades_ids": ["mordida_mortal", "rolar_da_morte"],
        "ataques_base_ids": ["soco"],
        "loot_table": [
            {"id_item": "couro_de_crocodilo_gigante", "chance": 0.9, "quantidade": [1, 1]},
            {"id_item": "dente_de_crocodilo_gigante", "chance": 0.25, "quantidade": [1, 2]}
        ]
    },
    "hydra_jovem": {
        "nome": "Hydra Jovem",
        "nivel": 20,
        "familia": "Monstruosidade",
        "xp_recompensa": 250,
        "ouro_recompensa": 150,
        "stats_base": {"forca": 18, "destreza": 14, "constituicao": 22, "inteligencia": 6, "sabedoria": 10, "sorte": 7},
        "habilidades_ids": ["multiplas_mordidas", "sopro_acido", "regeneracao_rapida"],
        "ataques_base_ids": [],
        "loot_table": [
            {"id_item": "escama_de_hydra", "chance": 1.0, "quantidade": [2, 5]},
            {"id_item": "sangue_de_hydra", "chance": 0.5, "quantidade": [1, 3]},
            {"id_item": "coracao_de_hydra", "chance": 0.1, "quantidade": [1, 1]}
        ]
    }
}
