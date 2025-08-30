# -*- coding: utf-8 -*-
"""
================================================================================================
BANCO DE DADOS: MONSTROS - CAVERNAS
================================================================================================
"""
from typing import List, Dict

MONSTROS_CAVERNAS: List[Dict] = [
    {
        "id": "rato_gigante", "nome": "Rato Gigante", "nivel": 2, "hp": 15,
        "atributos": {"forca": 7, "destreza": 15, "defesa": 5},
        "habilidades": [], "comportamento": "agressivo_em_grupo",
        "drops": [{"item_id": "rabo_de_rato", "chance": 0.9, "quantidade": 1}]
    },
    {
        "id": "morcego_vampiro", "nome": "Morcego Vampiro", "nivel": 3, "hp": 22,
        "atributos": {"forca": 8, "destreza": 16, "defesa": 6},
        "habilidades": ["drenar_vida"], "comportamento": "oportunista",
        "drops": [{"item_id": "asa_de_morcego", "chance": 0.7, "quantidade": "1d2"}]
    },
    {
        "id": "goblin_guerreiro", "nome": "Goblin Guerreiro", "nivel": 4, "hp": 40,
        "atributos": {"forca": 13, "destreza": 12, "defesa": 10},
        "habilidades": ["guerreiro_golpe_poderoso"], "comportamento": "agressivo",
        "drops": [
            {"item_id": "moedas_de_cobre", "chance": 0.9, "quantidade": "2d8"},
            {"item_id": "arma_espada_curta_ferro", "chance": 0.1, "quantidade": 1},
            {"item_id": "escudo_de_madeira", "chance": 0.1, "quantidade": 1}
        ]
    },
    {
        "id": "slime_corrosivo", "nome": "Slime Corrosivo", "nivel": 4, "hp": 50,
        "atributos": {"forca": 10, "destreza": 6, "defesa": 7},
        "habilidades": [], "comportamento": "passivo",
        "resistencias": {"cortante": 0.5, "perfurante": 0.5},
        "imunidades": ["veneno"],
        "drops": [{"item_id": "gosma_acida", "chance": 1.0, "quantidade": "1d3"}]
    },
    {
        "id": "aranha_de_caverna", "nome": "Aranha de Caverna", "nivel": 5, "hp": 35,
        "atributos": {"forca": 12, "destreza": 17, "defesa": 8},
        "habilidades": ["ladino_golpe_venenoso"], "comportamento": "emboscada",
        "drops": [{"item_id": "glandula_de_veneno", "chance": 0.5, "quantidade": 1}, {"item_id": "seda_de_aranha", "chance": 0.8, "quantidade": "1d4"}]
    },
    {
        "id": "chefe_goblin", "nome": "Rei Goblin Grão-Piolho", "nivel": 6, "hp": 80,
        "tipo": "chefe",
        "atributos": {"forca": 16, "destreza": 14, "defesa": 12},
        "habilidades": ["guerreiro_golpe_poderoso", "guerreiro_grito_de_guerra"],
        "comportamento": "chefe_simples",
        "drops": [
            {"item_id": "moedas_de_prata", "chance": 1.0, "quantidade": "3d10"},
            {"item_id": "arma_martelo_guerra_aco", "chance": 0.1, "quantidade": 1},
            {"item_id": "pocao_cura_fraca", "chance": 1.0, "quantidade": "1d2"},
            {"item_id": "coroa_de_latao_do_rei_goblin", "chance": 1.0, "quantidade": 1}
        ]
    }
]
