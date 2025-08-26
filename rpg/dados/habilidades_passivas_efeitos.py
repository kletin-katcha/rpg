# ==============================================================================
# ARQUIVO DE DADOS: EFEITOS DE HABILIDADES PASSIVAS
# ==============================================================================
#
# Este arquivo mapeia IDs de habilidades passivas (geralmente raciais)
# para os efeitos diretos que elas aplicam nos atributos de um personagem.
# A função `recalcular_stats_completos` usará este dicionário para aplicar
# estes bônus permanentes.
#
# NOTA: Habilidades que não conferem um bônus de stat passivo e constante
# (ex: voo, ataques especiais, bônus em rolagens de dados específicas) não
# são incluídas aqui e devem ser implementadas em outras partes do sistema.
#
# Estrutura:
# -----------
# "id_habilidade": {
#   "atributo": (str) O nome do atributo a ser modificado no objeto Personagem.
#   "chave": (str, opcional) Se o atributo for um dicionário, como 'resistencias'.
#   "valor": (float ou int) O valor a ser somado ao atributo/chave.
# }
# ==============================================================================

HABILIDADES_PASSIVAS_EFEITOS = {
    # Elfo
    "visao_no_escuro": {
        "atributo": "precisao",
        "valor": 10
    },
    "afinidade_arcana": {
        "atributo": "poder_magico",
        "valor": 2
    },

    # Anão
    "resistencia_a_veneno": {
        "atributo": "resistencias",
        "chave": "veneno",
        "valor": 0.50  # 50%
    },
    "artesao_de_pedra": {
        "atributo": "defesa_fisica",
        "valor": 2
    },

    # Khajiit
    "visao_noturna_superior": {
        "atributo": "precisao",
        "valor": 15
    },
    # "garras_afiadas" - Efeito em ataque desarmado, precisa de lógica de combate.

    # Argoniano
    "imunidade_a_doenca_veneno": {
        "atributo": "resistencias",
        "chave": "veneno",
        "valor": 1.0  # 100%
    },
    # "respirar_agua" - Efeito situacional.

    # Aasimar
    "resistencia_celestial": {
        "atributo": "resistencias",
        "chave": "sombra", # Dano necrótico
        "valor": 0.25
    },
    # A outra parte de resistencia_celestial (dano radiante) precisa ser adicionada.
    # Vamos adicionar como uma habilidade separada para o motor lidar com isso.
    "resistencia_celestial_radiante": {
        "atributo": "resistencias",
        "chave": "sagrado", # Dano radiante
        "valor": 0.25
    },

    # Tiefling
    "resistencia_infernal": {
        "atributo": "resistencias",
        "chave": "fogo",
        "valor": 0.50
    },

    # Goliath
    "resistencia_da_montanha": {
        "atributo": "resistencias",
        "chave": "gelo",
        "valor": 0.25
    },

    # Draconato
    # "resistencia_draconica" - Depende da ascendência, precisa de lógica na criação do personagem.

    # Povo-Lagarto
    "armadura_natural": {
        "atributo": "defesa_fisica",
        "valor": 3
    },

    # Loxodon
    "pele_grossa": {
        "atributo": "defesa_fisica",
        "valor": 4
    },

    # Shadar-kai
    "resistencia_necrotica": {
        "atributo": "resistencias",
        "chave": "sombra",
        "valor": 0.50
    },

    # Forjado (Warforged)
    "construcao_resistente": {
        "atributo": "resistencias",
        "chave": "veneno",
        "valor": 0.50 # Vantagem interpretada como 50% de resistência.
    },

    # Autômato
    "corpo_mecanico": {
        "atributo": "resistencias",
        "chave": "veneno",
        "valor": 1.0 # Imunidade
    },

    # Sylvari
    "pele_de_casca": {
        "atributo": "defesa_fisica",
        "valor": 3
    },

    # Sátiro
    "resistencia_a_magia": {
        "atributo": "defesa_magica",
        "valor": 5 # Vantagem interpretada como bônus direto.
    },

    # Tritão
    "guardiao_das_profundezas": {
        "atributo": "resistencias",
        "chave": "gelo",
        "valor": 0.50
    },

    # Yuan-ti Sangue-Puro
    "vantagem_magica": {
        "atributo": "defesa_magica",
        "valor": 5 # Vantagem interpretada como bônus direto.
    },
    "imunidade_a_veneno": {
        "atributo": "resistencias",
        "chave": "veneno",
        "valor": 1.0 # 100%
    }
}
