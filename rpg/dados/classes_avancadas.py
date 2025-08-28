# ==============================================================================
# ARQUIVO DE DADOS: CLASSES AVANÇADAS (TIER 1)
# ==============================================================================
#
# Este arquivo contém as definições para as primeiras evoluções das classes
# iniciais.
#
# Estrutura de cada Classe Avançada:
# ---------------------------------
# "nome": (str) Nome da classe.
# "descricao": (str) Descrição da classe.
# "classe_base": (str) ID da classe inicial necessária para esta evolução.
# "nivel_necessario": (int) Nível que o jogador deve ter para evoluir.
# "habilidades_concedidas": (list) Lista de IDs de novas habilidades.
# "bonus_stats": (dict) Bônus permanentes nos atributos base do personagem.
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
        "descricao": "Um guerreiro que abandonou a técnica em favor da fúria pura e incontrolável, tornando-se uma força da natureza no campo de batalha.",
        "classe_base": "guerreiro",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["furia_interminavel", "golpe_imprudente"],
        "bonus_stats": {"forca": 3, "constituicao": 1}
    },

    # --- Evoluções do Mago ---
    "arquimago": {
        "nome": "Arquimago",
        "descricao": "Um mestre das artes arcanas, cujo entendimento da magia permite dobrar a realidade à sua vontade.",
        "classe_base": "mago",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["chuva_de_meteoros", "teleporte_arcano"],
        "bonus_stats": {"inteligencia": 3, "sabedoria": 1}
    },
    "mago_de_batalha": {
        "nome": "Mago de Batalha",
        "descricao": "Um mago que funde poder arcano com proeza marcial, vestindo armaduras pesadas e lutando na linha de frente.",
        "classe_base": "mago",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["armadura_runica", "explosao_de_forca"],
        "bonus_stats": {"inteligencia": 2, "forca": 2}
    },

    # --- Evoluções do Ladino ---
    "assassino": {
        "nome": "Assassino",
        "descricao": "Um mestre da morte silenciosa, que estuda a anatomia e os venenos para eliminar seus alvos com eficiência letal.",
        "classe_base": "ladino",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["ataque_exposto", "veneno_debilitante"],
        "bonus_stats": {"destreza": 3, "inteligencia": 1}
    },
    "trapaceiro": {
        "nome": "Trapaceiro",
        "descricao": "Um ladino que usa de truques, distrações e carisma para controlar o campo de batalha e manipular seus inimigos.",
        "classe_base": "ladino",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["distracao", "roubar_item"],
        "bonus_stats": {"destreza": 2, "carisma": 2}
    },

    # --- Evoluções do Clérigo ---
    "sacerdote": {
        "nome": "Sacerdote",
        "descricao": "Um farol de fé, cujas preces curam os feridos e purificam os amaldiçoados com poder divino avassalador.",
        "classe_base": "clerigo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["cura_em_area", "palavra_sagrada_punicao"],
        "bonus_stats": {"sabedoria": 3, "inteligencia": 1}
    },
    "inquisidor": {
        "nome": "Inquisidor",
        "descricao": "Um caçador implacável do profano, que combina zelo divino com proeza marcial para expurgar as trevas.",
        "classe_base": "clerigo",
        "nivel_necessario": 15,
        "habilidades_concedidas": ["arma_da_fe", "julgamento_do_herege"],
        "bonus_stats": {"sabedoria": 2, "forca": 2}
    }
}
