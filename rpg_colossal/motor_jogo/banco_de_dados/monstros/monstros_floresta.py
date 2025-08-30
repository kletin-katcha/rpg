# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: MONSTROS - FLORESTA
================================================================================================
"""
from typing import List, Dict

MONSTROS_FLORESTA: List[Dict] = [
    {
        "id": "lobo_atroz", "nome": "Lobo Atroz", "nivel": 7, "hp": 60,
        "atributos": {"forca": 17, "destreza": 15, "defesa": 10},
        "habilidades": ["ataque_basico", "derrubar"],
        "comportamento": "cacador",
        "drops": [{"item_id": "pele_de_lobo_atroz", "chance": 0.6, "quantidade": 1}, {"item_id": "dente_de_lobo_atroz", "chance": 0.4, "quantidade": "1d3"}]
    },
    {
        "id": "aranha_gigante", "nome": "Aranha Gigante", "nivel": 8, "hp": 75,
        "atributos": {"forca": 14, "destreza": 18, "defesa": 9},
        "habilidades": ["ladino_golpe_venenoso", "teia"],
        "comportamento": "emboscada",
        "drops": [{"item_id": "glandula_de_veneno_potente", "chance": 0.5, "quantidade": 1}, {"item_id": "seda_de_aranha_reforcada", "chance": 0.8, "quantidade": "1d6"}]
    },
    {
        "id": "espirito_da_floresta", "nome": "Espírito da Floresta", "nivel": 9, "hp": 80,
        "atributos": {"forca": 10, "destreza": 16, "defesa": 11, "sabedoria": 18},
        "habilidades": ["clerigo_golpe_sagrado", "enraizar"],
        "comportamento": "protetor",
        "resistencias": {"perfurante": 0.5},
        "vulnerabilidades": {"fogo": 1.5},
        "drops": [{"item_id": "essencia_espiritual", "chance": 0.9, "quantidade": "1d3"}, {"item_id": "galho_retorcido_vivo", "chance": 0.2, "quantidade": 1}]
    },
    {
        "id": "troll_da_floresta", "nome": "Troll da Floresta", "nivel": 10, "hp": 120,
        "atributos": {"forca": 18, "destreza": 13, "defesa": 12, "constituicao": 20},
        "habilidades": ["ataque_basico", "regeneracao_troll"],
        "comportamento": "bruto",
        "vulnerabilidades": {"fogo": 2.0, "acido": 1.5},
        "drops": [{"item_id": "sangue_de_troll", "chance": 1.0, "quantidade": 1}, {"item_id": "pedra_estomacal_troll", "chance": 0.1, "quantidade": 1}]
    }
]
