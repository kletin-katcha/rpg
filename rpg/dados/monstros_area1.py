# ==============================================================================
# ARQUIVO DE DADOS: MONSTROS DA ÁREA 1 (FLORESTA INICIAL)
# ==============================================================================
#
# Este arquivo contém as definições para todos os monstros encontrados na
# primeira área do jogo.
#
# Estrutura de cada Monstro:
# ---------------------------
# "nome": (str) Nome do monstro.
# "nivel": (int) Nível de poder do monstro.
# "familia": (str) Categoria do monstro (ex: "Besta", "Humanoide").
# "xp_recompensa": (int) XP base ganho ao derrotá-lo.
# "ouro_recompensa": (int) Ouro base ganho.
# "stats_base": (dict) Seus atributos primários.
# "habilidades": (list) Lista de IDs de habilidades que o monstro pode usar.
# "loot_table": (list) Lista de possíveis itens derrubados.
#   - "id_item": (str) ID do item.
#   - "chance": (float) Chance de derrubar o item (0.0 a 1.0).
#   - "quantidade": (list) [min, max] quantidade do item.
#
# ==============================================================================

MONSTROS_AREA1 = {
    "lobo_cinzento": {
        "nome": "Lobo Cinzento",
        "nivel": 1,
        "familia": "Besta",
        "xp_recompensa": 10,
        "ouro_recompensa": 5,
        "stats_base": {
            "forca": 12, "destreza": 14, "constituicao": 11,
            "inteligencia": 3, "sabedoria": 10, "carisma": 4
        },
        "habilidades": ["mordida_feroz"],
        "comportamento_ia": "agressivo",
        "loot_table": [
            {"id_item": "pele_de_lobo", "chance": 0.5, "quantidade": [1, 1]},
            {"id_item": "dente_de_lobo", "chance": 0.2, "quantidade": [1, 2]}
        ]
    },
    "goblin_batedor": {
        "nome": "Goblin Batedor",
        "nivel": 2,
        "familia": "Humanoide",
        "xp_recompensa": 15,
        "ouro_recompensa": 10,
        "stats_base": {
            "forca": 10, "destreza": 15, "constituicao": 10,
            "inteligencia": 8, "sabedoria": 8, "carisma": 6
        },
        "habilidades": ["arremessar_pedra", "golpe_baixo"],
        "comportamento_ia": "oportunista", # Ataca alvos com HP baixo
        "loot_table": [
            {"id_item": "caco_de_arma_enferrujada", "chance": 0.4, "quantidade": [1, 1]},
            {"id_item": "pocao_cura_fraca", "chance": 0.05, "quantidade": [1, 1]}
        ]
    },
    "javali_selvagem": {
        "nome": "Javali Selvagem",
        "nivel": 3,
        "familia": "Besta",
        "xp_recompensa": 25,
        "ouro_recompensa": 0,
        "stats_base": {
            "forca": 16, "destreza": 10, "constituicao": 15,
            "inteligencia": 2, "sabedoria": 8, "carisma": 3
        },
        "habilidades": ["investida_imprudente"],
        "comportamento_ia": "agressivo",
        "loot_table": [
            {"id_item": "carne_de_javali", "chance": 0.7, "quantidade": [1, 2]},
            {"id_item": "presa_de_javali", "chance": 0.25, "quantidade": [1, 2]}
        ]
    },
    "enxame_de_vespas": {
        "nome": "Enxame de Vespas",
        "nivel": 2,
        "familia": "Besta",
        "xp_recompensa": 12,
        "ouro_recompensa": 0,
        "stats_base": {
            "forca": 5, "destreza": 18, "constituicao": 8,
            "inteligencia": 1, "sabedoria": 6, "carisma": 1
        },
        "habilidades": ["ferroada_venenosa"],
        "comportamento_ia": "agressivo",
        "loot_table": [
            {"id_item": "ferrao_de_vespa", "chance": 0.6, "quantidade": [2, 5]},
            {"id_item": "glandula_de_veneno_fraca", "chance": 0.15, "quantidade": [1, 1]}
        ]
    },
    "slime_verde": {
        "nome": "Slime Verde",
        "nivel": 1,
        "familia": "Amorfo",
        "xp_recompensa": 8,
        "ouro_recompensa": 1,
        "stats_base": {
            "forca": 10, "destreza": 5, "constituicao": 18,
            "inteligencia": 1, "sabedoria": 1, "carisma": 1
        },
        "habilidades": ["cuspe_acido"],
        "comportamento_ia": "defensivo", # Tem alta defesa e baixo ataque
        "loot_table": [
            {"id_item": "gosma_de_slime", "chance": 0.9, "quantidade": [1, 3]}
        ]
    },

    # --- EXPANSÃO DE MONSTROS - ELITES E NOVOS TIPOS ---
    "lobo_alfa": {
        "nome": "Lobo Alfa",
        "nivel": 4,
        "familia": "Besta",
        "xp_recompensa": 50,
        "ouro_recompensa": 15,
        "stats_base": {
            "forca": 16, "destreza": 18, "constituicao": 14,
            "inteligencia": 6, "sabedoria": 12, "carisma": 8
        },
        "habilidades": ["mordida_feroz", "uivo_de_comando"], # Uivo aumenta o ataque de outros lobos
        "comportamento_ia": "lider_de_matilha", # Foca em alvos fracos e buffa aliados
        "loot_table": [
            {"id_item": "pele_de_lobo_alfa", "chance": 0.1, "quantidade": [1, 1]},
            {"id_item": "dente_de_lobo_alfa", "chance": 0.5, "quantidade": [1, 2]},
            {"id_item": "carne_de_qualidade", "chance": 0.8, "quantidade": [1, 3]}
        ]
    },
    "goblin_xama": {
        "nome": "Goblin Xamã",
        "nivel": 3,
        "familia": "Humanoide",
        "xp_recompensa": 30,
        "ouro_recompensa": 25,
        "stats_base": {
            "forca": 8, "destreza": 12, "constituicao": 9,
            "inteligencia": 14, "sabedoria": 15, "carisma": 7
        },
        "habilidades": ["seta_de_veneno", "cura_primitiva"],
        "comportamento_ia": "suporte", # Prioriza curar e buffar outros goblins
        "loot_table": [
            {"id_item": "cajado_torto_goblin", "chance": 0.2, "quantidade": [1, 1]},
            {"id_item": "ervas_estranhas", "chance": 0.7, "quantidade": [1, 4]}
        ]
    },
    "urso_coruja": {
        "nome": "Urso-Coruja",
        "nivel": 5,
        "familia": "Besta Mágica",
        "xp_recompensa": 80,
        "ouro_recompensa": 0,
        "stats_base": {
            "forca": 20, "destreza": 12, "constituicao": 18,
            "inteligencia": 4, "sabedoria": 12, "carisma": 6
        },
        "habilidades": ["patada_esmagadora", "bico_perfurante", "grito_aterrorizante"],
        "comportamento_ia": "agressivo_elite", # Usa habilidades de forma mais inteligente
        "loot_table": [
            {"id_item": "pena_de_urso_coruja", "chance": 0.5, "quantidade": [2, 5]},
            {"id_item": "bico_de_urso_coruja", "chance": 0.1, "quantidade": [1, 1]}
        ]
    },
    "bandido_humano": {
        "nome": "Bandido",
        "nivel": 3,
        "familia": "Humanoide",
        "xp_recompensa": 20,
        "ouro_recompensa": 30,
        "stats_base": {
            "forca": 14, "destreza": 13, "constituicao": 12,
            "inteligencia": 10, "sabedoria": 9, "carisma": 11
        },
        "habilidades": ["golpe_com_escudo", "arremessar_faca"],
        "comportamento_ia": "oportunista",
        "loot_table": [
            {"id_item": "armadura_de_couro_gasta", "chance": 0.2, "quantidade": [1, 1]},
            {"id_item": "garrafa_de_grogue", "chance": 0.4, "quantidade": [1, 1]}
        ]
    },
    "treant_jovem": {
        "nome": "Treant Jovem",
        "nivel": 4,
        "familia": "Planta",
        "xp_recompensa": 60,
        "ouro_recompensa": 0,
        "stats_base": {
            "forca": 18, "destreza": 8, "constituicao": 17,
            "inteligencia": 7, "sabedoria": 14, "carisma": 8
        },
        "habilidades": ["pancada_de_galho", "casca_reforçada"],
        "comportamento_ia": "defensor_territorial", # Não persegue longe, mas bate forte
        "loot_table": [
            {"id_item": "madeira_viva", "chance": 0.3, "quantidade": [1, 2]},
            {"id_item": "seiva_encantada", "chance": 0.1, "quantidade": [1, 1]}
        ]
    }
}
