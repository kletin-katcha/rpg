# ==============================================================================
# ARQUIVO DE DADOS: CLASSES AVANÇADAS (TIER 1)
# ==============================================================================
#
# Este arquivo contém as definições para as primeiras evoluções das classes
# iniciais.
#
# ==============================================================================

CLASSES_AVANCADAS = {
    # --- Evoluções do Guerreiro ---
    "mestre_de_armas": {
        "nome": "Mestre de Armas",
        "descricao": "Um guerreiro que alcançou o auge da técnica com sua arma escolhida, transformando o combate em uma arte.",
        "classe_base": "guerreiro",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["postura_de_mestre", "golpe_mortal"],
        "bonus_stats": {"forca": 2, "destreza": 2}
    },
    "berserker": {
        "nome": "Berserker",
        "descricao": "Um guerreiro que abandonou a técnica em favor da fúria pura e incontrolável.",
        "classe_base": "guerreiro",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["furia_interminavel", "golpe_imprudente"],
        "bonus_stats": {"forca": 3, "constituicao": 1}
    },

    # --- Evoluções do Mago ---
    "arquimago": {
        "nome": "Arquimago",
        "descricao": "Um mestre das artes arcanas.",
        "classe_base": "mago",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["chuva_de_meteoros", "teleporte_arcano"],
        "bonus_stats": {"inteligencia": 3, "sabedoria": 1}
    },
    "mago_de_batalha": {
        "nome": "Mago de Batalha",
        "descricao": "Um mago que funde poder arcano com proeza marcial.",
        "classe_base": "mago",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["armadura_runica", "explosao_de_forca"],
        "bonus_stats": {"inteligencia": 2, "forca": 2}
    },

    # --- Evoluções do Ladino ---
    "assassino": {
        "nome": "Assassino",
        "descricao": "Um mestre da morte silenciosa.",
        "classe_base": "ladino",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["ataque_exposto", "veneno_debilitante"],
        "bonus_stats": {"destreza": 3, "inteligencia": 1}
    },
    "trapaceiro": {
        "nome": "Trapaceiro",
        "descricao": "Um ladino que usa de truques e distrações.",
        "classe_base": "ladino",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["distracao", "roubar_item"],
        "bonus_stats": {"destreza": 2, "carisma": 2}
    },

    # --- Evoluções do Clérigo ---
    "sacerdote": {
        "nome": "Sacerdote",
        "descricao": "Um farol de fé, cujas preces curam os feridos.",
        "classe_base": "clerigo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["cura_em_area", "palavra_sagrada_punicao"],
        "bonus_stats": {"sabedoria": 3, "inteligencia": 1}
    },
    "inquisidor": {
        "nome": "Inquisidor",
        "descricao": "Um caçador implacável do profano.",
        "classe_base": "clerigo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["arma_da_fe", "julgamento_do_herege"],
        "bonus_stats": {"sabedoria": 2, "forca": 2}
    },

    # --- Evoluções do Bárbaro ---
    "berserker_barbaro": {
        "nome": "Berserker",
        "descricao": "Um bárbaro que se entregou completamente à fúria.",
        "classe_base": "barbaro",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["frenesi_de_batalha", "golpe_temerario"],
        "bonus_stats": {"forca": 4}
    },
    "protetor_ancestral": {
        "nome": "Protetor Ancestral",
        "descricao": "Um bárbaro que canaliza os espíritos de seus ancestrais.",
        "classe_base": "barbaro",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["totem_de_protecao", "espirito_do_urso"],
        "bonus_stats": {"constituicao": 3, "sabedoria": 1}
    },

    # --- Evoluções do Ranger ---
    "arqueiro_arcano": {
        "nome": "Arqueiro Arcano",
        "descricao": "Um ranger que imbui suas flechas com poder mágico.",
        "classe_base": "ranger",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["flecha_elemental", "disparo_enfraquecedor"],
        "bonus_stats": {"destreza": 2, "inteligencia": 2}
    },
    "mestre_das_feras_avancado": {
        "nome": "Mestre das Feras",
        "descricao": "Um ranger cujo vínculo com seu companheiro animal é profundo.",
        "classe_base": "ranger",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["ataque_coordenado_aprimorado", "furia_bestial"],
        "bonus_stats": {"destreza": 1, "carisma": 3}
    },

    # --- Evoluções do Bardo ---
    "virtuoso": {
        "nome": "Virtuoso",
        "descricao": "Um bardo cuja música e palavras podem inspirar exércitos.",
        "classe_base": "bardo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["sonata_da_inspiracao", "balada_da_confusao"],
        "bonus_stats": {"carisma": 4}
    },
    "dancarino_das_laminas": {
        "nome": "Dançarino das Lâminas",
        "descricao": "Um bardo que transformou o combate em uma dança mortal.",
        "classe_base": "bardo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["danca_das_laminas", "finta_ritmica"],
        "bonus_stats": {"destreza": 3, "carisma": 1}
    }
}
