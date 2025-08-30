# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: MONSTROS - REGIÃO INICIAL
================================================================================================
"""
from typing import List, Dict

MONSTROS_REGIAO_INICIAL: List[Dict] = [
    {
        "id": "goblin_batedor", "nome": "Goblin Batedor", "nivel": 1, "hp": 20,
        "atributos": {"forca": 8, "destreza": 14, "defesa": 5, "inteligencia": 6},
        "habilidades": ["ataque_basico"], "comportamento": "agressivo",
        "drops": [{"item_id": "moedas_cobre", "chance": 0.8, "quantidade": "1d6"}, {"item_id": "arma_adaga_ferro", "chance": 0.05, "quantidade": 1}]
    },
    {
        "id": "lobo_jovem", "nome": "Lobo Jovem", "nivel": 2, "hp": 25,
        "atributos": {"forca": 11, "destreza": 15, "defesa": 6, "inteligencia": 3},
        "habilidades": ["ataque_basico"], "comportamento": "agressivo_em_grupo",
        "drops": [{"item_id": "pele_de_lobo", "chance": 0.5, "quantidade": 1}, {"item_id": "carne_de_lobo", "chance": 0.7, "quantidade": 1}]
    },
    {
        "id": "goblin_atirador", "nome": "Goblin Atirador", "nivel": 2, "hp": 18,
        "atributos": {"forca": 7, "destreza": 16, "defesa": 4, "inteligencia": 7},
        "habilidades": [], "comportamento": "defensivo",
        "drops": [{"item_id": "moedas_cobre", "chance": 0.8, "quantidade": "1d8"}, {"item_id": "arma_arco_curto_simples", "chance": 0.05, "quantidade": 1}]
    },
    {
        "id": "javali_selvagem", "nome": "Javali Selvagem", "nivel": 3, "hp": 35,
        "atributos": {"forca": 14, "destreza": 10, "defesa": 8, "inteligencia": 2},
        "habilidades": ["guerreiro_investida"], "comportamento": "agressivo",
        "drops": [{"item_id": "pele_de_javali", "chance": 0.6, "quantidade": 1}, {"item_id": "presa_de_javali", "chance": 0.3, "quantidade": "1d2"}]
    },
    {
        "id": "goblin_xamã", "nome": "Goblin Xamã", "nivel": 4, "hp": 28,
        "atributos": {"forca": 6, "destreza": 12, "defesa": 7, "inteligencia": 14},
        "habilidades": ["mago_seta_de_fogo", "clerigo_cura_leve"], "comportamento": "suporte",
        "drops": [{"item_id": "moedas_cobre", "chance": 0.9, "quantidade": "2d6"}, {"item_id": "erva_simples", "chance": 0.5, "quantidade": "1d4"}, {"item_id": "arma_cajado_simples", "chance": 0.05, "quantidade": 1}]
    },
    {
        "id": "lobo_alfa", "nome": "Lobo Alfa", "nivel": 5, "hp": 50,
        "atributos": {"forca": 15, "destreza": 16, "defesa": 9, "inteligencia": 5},
        "habilidades": ["ataque_basico", "guerreiro_grito_de_guerra"], "comportamento": "lider_de_matilha",
        "drops": [{"item_id": "pele_de_lobo_alfa", "chance": 1.0, "quantidade": 1}, {"item_id": "carne_de_lobo_premium", "chance": 0.8, "quantidade": "1d2"}, {"item_id": "dente_de_lobo_alfa", "chance": 0.2, "quantidade": 1}]
    }
]
