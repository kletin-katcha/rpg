# ==============================================================================
# ARQUIVO DE DADOS: EFEITOS DE STATUS (BUFFS E DEBUFFS)
# ==============================================================================
#
# Este arquivo define os detalhes de todos os efeitos de status temporários
# que podem ser aplicados a um personagem durante o combate.
#
# Estrutura:
# -----------
# "id_efeito": {
#   "nome": (str) O nome do efeito.
#   "descricao": (str) Descrição do que o efeito faz.
#   "tipo": (str) "Buff" ou "Debuff".
#   "modificadores": (dict, opcional) Bônus/penalidades de stats aplicados enquanto
#                    o efeito está ativo. Ex: {"forca": 5, "defesa_fisica": -10}
#   "efeito_por_turno": (dict, opcional) Efeitos que acontecem a cada turno.
#                       Ex: {"tipo": "dano", "dano_tipo": "veneno", "quantidade": 5}
# }
# ==============================================================================

from ..entidades.efeito import TipoEfeito

TODOS_OS_EFEITOS = {
    # --- BUFFS ---
    "buff_esforco_heroico": {
        "nome": "Esforço Heroico",
        "descricao": "O personagem está sob o efeito de um surto de adrenalina, aumentando todos os seus atributos.",
        "tipo": TipoEfeito.BUFF,
        "modificadores": {
            "forca": 2,
            "destreza": 2,
            "constituicao": 2,
            "inteligencia": 2,
            "sabedoria": 2,
            "carisma": 2,
        }
    },
    "buff_defesa_grande": {
        "nome": "Defesa Aumentada",
        "descricao": "A defesa do personagem está significativamente aumentada.",
        "tipo": TipoEfeito.BUFF,
        "modificadores": {
            "defesa_fisica": 20,
            "defesa_magica": 20
        }
    },
    "buff_dano_matilha": {
        "nome": "Frenesi da Matilha",
        "descricao": "Inspirado pelo uivo do alfa, o ataque deste personagem é aumentado.",
        "tipo": TipoEfeito.BUFF,
        "modificadores": {
            "ataque_fisico": 10
        }
    },

    # --- DEBUFFS ---
    "debuff_defesa_pequeno": {
        "nome": "Defesa Reduzida",
        "descricao": "A defesa do personagem está ligeiramente reduzida.",
        "tipo": TipoEfeito.DEBUFF,
        "modificadores": {
            "defesa_fisica": -5,
            "defesa_magica": -5
        }
    },
    "debuff_defesa_grande": {
        "nome": "Defesa Quebrada",
        "descricao": "A defesa do personagem está severamente comprometida.",
        "tipo": TipoEfeito.DEBUFF,
        "modificadores": {
            "defesa_fisica": -20
        }
    },
    "veneno_fraco": {
        "nome": "Envenenado",
        "descricao": "O personagem está sofrendo dano de veneno a cada turno.",
        "tipo": TipoEfeito.DEBUFF,
        "efeito_por_turno": {
            "tipo": "dano",
            "dano_tipo": "veneno",
            "quantidade": 5
        }
    },
    "atordoamento": {
        "nome": "Atordoado",
        "descricao": "O personagem não pode agir.",
        "tipo": TipoEfeito.DEBUFF,
        "modificadores": {
            "pode_agir": False # Necessita de lógica no loop de combate para verificar isso
        }
    },
    "medo": {
        "nome": "Amedrontado",
        "descricao": "O personagem está amedrontado e pode falhar em suas ações.",
        "tipo": TipoEfeito.DEBUFF,
        "modificadores": {
            "chance_falha_acao": 0.5 # Necessita de lógica no loop de combate
        }
    }
}
