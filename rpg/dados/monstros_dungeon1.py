# ==============================================================================
# ARQUIVO DE DADOS: MONSTROS (DUNGEON 1 - RUÍNAS DE AL'KHEM)
# ==============================================================================

MONSTROS_DUNGEON1 = {
    "construto_guardiao_quebrado": {
        "nome": "Construto Guardião Quebrado",
        "nivel": 14,
        "familia": "Construto",
        "xp_recompensa": 90,
        "ouro_recompensa": 50,
        "stats_base": {"forca": 18, "destreza": 8, "constituicao": 20, "inteligencia": 1, "sabedoria": 5, "sorte": 1},
        "habilidades_ids": ["golpe_pesado"],
        "ataques_base_ids": ["soco"],
        "loot_table": [
            {"id_item": "nucleo_de_construto_danificado", "chance": 0.7, "quantidade": [1, 1]},
            {"id_item": "placa_de_bronze_antiga", "chance": 0.2, "quantidade": [1, 2]}
        ]
    },
    "construto_arcano": {
        "nome": "Construto Arcano",
        "nivel": 16,
        "familia": "Construto",
        "xp_recompensa": 130,
        "ouro_recompensa": 60,
        "stats_base": {"forca": 10, "destreza": 14, "constituicao": 15, "inteligencia": 18, "sabedoria": 10, "sorte": 5},
        "habilidades_ids": ["raio_arcano", "barreira_de_forca"],
        "ataques_base_ids": [],
        "loot_table": [
            {"id_item": "nucleo_de_construto_intacto", "chance": 0.5, "quantidade": [1, 1]},
            {"id_item": "lente_de_cristal_focadora", "chance": 0.15, "quantidade": [1, 1]}
        ]
    },
    "construto_colosso": {
        "nome": "Construto Colosso",
        "nivel": 22,
        "familia": "Construto",
        "xp_recompensa": 400,
        "ouro_recompensa": 200,
        "stats_base": {"forca": 28, "destreza": 6, "constituicao": 25, "inteligencia": 2, "sabedoria": 8, "sorte": 3},
        "habilidades_ids": ["pisao_devastador", "raio_ocular"],
        "ataques_base_ids": ["soco"],
        "loot_table": [
            {"id_item": "nucleo_de_construto_grande", "chance": 1.0, "quantidade": [1, 1]},
            {"id_item": "fragmento_de_armadura_ancestral", "chance": 0.3, "quantidade": [1, 3]}
        ]
    }
}
