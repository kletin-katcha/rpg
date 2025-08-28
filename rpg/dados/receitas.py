# ==============================================================================
# ARQUIVO DE DADOS: RECEITAS DE CRAFTING
# ==============================================================================
#
# Este arquivo contém as definições para todas as receitas de criação de
# itens do jogo.
#
# ==============================================================================

RECEITAS = {
    # --- Forja (Blacksmithing) ---
    "adaga_de_ferro_r": {
        "id_item_criado": "adaga_de_ferro",
        "ingredientes": [
            {"id_item": "caco_de_arma_enferrujada", "quantidade": 2},
            {"id_item": "pele_de_lobo", "quantidade": 1}
        ],
        "tipo_estacao": "forja"
    },
    "armadura_de_couro_reforcado_r": {
        "id_item_criado": "armadura_de_couro_reforcado",
        "ingredientes": [
            {"id_item": "pele_de_lobo", "quantidade": 5},
            {"id_item": "dente_de_lobo", "quantidade": 2}
        ],
        "tipo_estacao": "bancada_de_coureiro"
    },
    "escudo_de_ferro_simples_r": {
        "id_item_criado": "escudo_de_ferro_simples",
        "ingredientes": [
            {"id_item": "caco_de_arma_enferrujada", "quantidade": 4},
            {"id_item": "madeira_viva", "quantidade": 1}
        ],
        "tipo_estacao": "forja"
    },

    # --- Alquimia (Alchemy) ---
    "pocao_cura_media_r": {
        "id_item_criado": "pocao_cura_media",
        "ingredientes": [
            {"id_item": "pocao_cura_fraca", "quantidade": 2},
            {"id_item": "ervas_estranhas", "quantidade": 1}
        ],
        "tipo_estacao": "bancada_alquimia"
    },
    "antidoto_fraco_r": {
        "id_item_criado": "antidoto_fraco",
        "ingredientes": [
            {"id_item": "glandula_de_veneno_fraca", "quantidade": 1},
            {"id_item": "gosma_de_slime", "quantidade": 2}
        ],
        "tipo_estacao": "bancada_alquimia"
    },

    # --- Culinária (Cooking) ---
    "carne_cozida_r": {
        "id_item_criado": "carne_cozida",
        "ingredientes": [
            {"id_item": "carne_de_javali", "quantidade": 1}
        ],
        "tipo_estacao": "fogueira"
    }
}
