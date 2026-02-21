"""Planos de produção automática e requisitos de infraestrutura."""
PLANOS_PRODUCAO = {
    "sucata": {
        "nome": "Coleta de Sucata",
        "recompensas": {"caco_de_arma_enferrujada": 2},
    },
    "alquimia_basica": {
        "nome": "Insumos Alquímicos Básicos",
        "recompensas": {"gosma_de_slime": 2, "ferrao_de_vespa": 1},
    },
    "coleta_mista": {
        "nome": "Coleta Mista",
        "recompensas": {"caco_de_arma_enferrujada": 1, "gosma_de_slime": 1},
    },
    "refino_pesado": {
        "nome": "Refino Pesado",
        "recompensas": {"caco_de_arma_enferrujada": 2, "barra_metal_reciclado": 1},
        "estrutura_necessaria": "automacao_refino",
    },
    "alquimia_estendida": {
        "nome": "Alquimia Estendida",
        "recompensas": {"gosma_de_slime": 3, "ferrao_de_vespa": 2},
        "estrutura_necessaria": "laboratorio_alquimico",
    },
}
